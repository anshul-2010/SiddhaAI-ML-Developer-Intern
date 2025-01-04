import streamlit as st
# Importing the various libraries that play an essential role for extracting text from driving license.
import cv2  # Importing the OpenCV library for image processing
import numpy as np  # Importing the NumPy library for numerical computations
import pytesseract as pt  # Importing the pytesseract library for text recognition
import json  # Importing the json module for working with JSON data
from PIL import Image
from PIL import ImageEnhance
from datetime import datetime
import time
import pickle
import re

#Loading up the Regression model we created
with open("YOLO_Final.pickle", 'rb') as f:
    model1 = pickle.load(f)

# All the essential functions to be used here
def extract_text_from_image(image_array):
    """Extract text from an image using Tesseract OCR

    Args:
        image_array (numpy.ndarray): Input image as a NumPy array

    Returns:
        str: Extracted text from the image
    """
    text = []
    # Set DPI information for the image
    image = image_array
    image = Image.fromarray(image)
    image.info["dpi"] = (300,300)
    
    # Apply image contrast enhancement
    enhancement_factor = 1.5
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(enhancement_factor)
    image = np.array(enhanced_image)
    
     # Covert enhanced image to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    resized_image = cv2.resize(image, None, fx=2, fy=2)

    # Perform OCR to extract text
    extracted_txt = pt.image_to_string(resized_image)
    text.append(extracted_txt)
    return text

def starts_with_digit_and_number(input_string):
    pattern = r'^([\da-zA-Z]) (\d+)'
    return bool(re.match(pattern, input_string))

def has_digits(input_string):
    return any(char.isdigit() for char in input_string)

def extract_content(ocr_content, type_of_data):
    """Apply regex expression on obtained OCR for each section

    Args:
        ocr_content (str): Contains the OCR output for each criteria
        type_of_data (str): Contains the criteria of ocr_content

    Returns:
        str: Extracted content after regex evaluation
    """
    if type_of_data == "address":
        search_term = "Address"    
        index = ocr_content.lower().find(search_term.lower())
        if index != -1:
            ocr_content = ocr_content[:index] + ocr_content[index+len(search_term):]
        ocr_content = ocr_content.rstrip("\n")  # Remove trailing newline characters
        split_ocr_content = ocr_content.split("\n")  # Split the ocr_content at newline characters
        for j in range(len(split_ocr_content)):
          split_ocr_content[j] = re.sub(r"[^\w\s]", " ", split_ocr_content[j])
          split_ocr_content[j] = re.sub(r"\W+", " ", split_ocr_content[j]) # Check if this can be omitted
        split_ocr_content = [item for item in split_ocr_content if not(item == '' or item == ' ')]
        if len(split_ocr_content) == 0:
            return None
        
        if not has_digits(split_ocr_content[-1]):
            split_ocr_content = split_ocr_content[:-1]
    
        try:
            updated_content = re.sub(r"[^\w\s]", " ", split_ocr_content[-1])
            updated_content = re.sub(r'\W+', ' ', updated_content) # Check if this can be omitted
            last_line = re.sub(r"\s+", " ", updated_content)

            last_line = last_line.split(" ")
            integer_contents = [s for i, s in enumerate(last_line) if s.isdigit() and len(s) == 5]
            indices = [i for i, s in enumerate(last_line) if s in integer_contents]

            state = last_line[min(indices)-1]
            get_city = last_line[0:min(indices)-1]
            city = ' '.join(get_city)
            if(split_ocr_content[0].startswith("8 ")):
                split_ocr_content[0] = split_ocr_content[0][2:]
            if starts_with_digit_and_number(split_ocr_content[0]):
                split_ocr_content[0] = split_ocr_content[0][2:]
            streets = split_ocr_content[0:len(split_ocr_content)-1]
            full_street = ' '.join(streets)
            
            if state == "AZ" or state == "MN" or state == "HI" or state == "WA" or state == "MO":
                if full_street[0] == "8":
                    full_street = full_street[1:] 
            
            return full_street, city, state, integer_contents[0]
        except ValueError:
            return None
    
    elif type_of_data == "date_of_birth":
        ocr_content = ocr_content.replace("\n","")
        ocr_content = ocr_content.replace(" ", "")
        pattern = r"\d{1,2}[-./]\d{1,2}[-./]\d{2,4}" # Define a pattern to match special characters such that they represent dob
        matches = re.findall(pattern, ocr_content)
        if matches:
            for j in range(len(matches)):
                matches[j] = matches[j].replace("-","/")
                matches[j] = matches[j].replace(".","/")
            years = []
            # Extract years and compare
            try:
                for match in matches:
                    date_object = datetime.strptime(match, "%m/%d/%Y")  # Convert match to datetime object
                    years.append(date_object.year)  # Get the year value
                val = years.index(min(years))
                return matches[val]
            except ValueError:
                    return None
        else:
            return None
    
    elif type_of_data == "name":
        array = ocr_content.split("\n")
        array = [item for item in array if item is not '']
        name_length = len(array)
        pattern = r"[^\w\s]" # Define a pattern to match special characters.
        name = []
        try:
            for j in range(len(array)):
                name_part = re.sub(pattern, "", array[j])
                letters_only = re.sub(r'[^a-zA-Z\W]', '', name_part)
                name_part = letters_only.strip()
                name_parts = name_part.split(" ")   
                name_part = []             
                for alpha in range(len(name_parts)):
                    if(name_parts[alpha] == "FN" or name_parts[alpha] == "LN"):
                        continue
                    name_part.append(name_parts[alpha])
                if j==0:
                    name = name + name_part
                else:
                    name = name + name_part
            name = [item for item in name if not(item == '')]
            names = [content for content in name if content.isupper()]
            if len(names) is 2:
                names.append("")  
            if len(names) > 3:
                mid = names[2:]
                mid_names = ' '.join(mid)
                names = names[:2]
                names.append(mid_names)   
            
            if name_length == 1 and names[-1] == "":
                temp = names[0]
                names[0] = names[1]
                names[1] = temp
            elif name_length == 1 and len(names) == 3:
                temp = names[2]
                names[2] = names[1]
                names[1] = names[0]
                names[0] = temp
                
            for i in range(len(names)):
                if names[i].startswith("LN") or names[i].startswith("FN"):
                    names[i] = names[i][2:]
                       
            return names
        except ValueError:
            return None

def working_model(image):
    
    """It uses the model weights to predict the bounding boxes for the regions we are interested in

    Returns:
        json dictionary: This contains the values recorded by the AI module. It includes all the features we
                         wish to extract with respect to name, date of birth and address
    """
    
    prediction_list1 = model1.predict(image, confidence=1, overlap=30).json()
    pred_list1 = prediction_list1["predictions"]

    output_ai = {"name":("", 0.0), "date_of_birth":("", 0.0), "address":("", 0.0)}

    for i in pred_list1:
        x = i["x"]
        y = i["y"]
        width = i["width"]
        height = i["height"]
        confidence = i["confidence"]
        class_name = i["class"]
        
        left = x - width // 2
        top = y - height // 2
        right = x + width // 2
        bottom = y + height // 2

        # Ensure the coordinates are within the image bounds
        left = int(max(0, left))
        top = int(max(0, top))
        right = int(min(image.shape[1], right))
        bottom = int(min(image.shape[0], bottom))

        cropped = image[top:bottom, left:right]
        alpha = 1.5 # Contrast control (1.0-3.0)
        beta = 0 # Brightness control (0-100)
        crop = cv2.convertScaleAbs(cropped, alpha=alpha, beta=beta)
        if(output_ai[class_name][1]<confidence):
            text = extract_text_from_image(crop)
            output_ai[class_name] = (extract_content(str(text[0]), class_name), confidence)
    dob_all = output_ai["date_of_birth"][0]


    arr = {"last_name":"","first_name":"","middle_name":"","date_of_birth":"","street1":"","city":"","state":"","pincode":""}
    print(output_ai)
    if(output_ai["name"][0] is not None):
        if(len(output_ai["name"][0])>=1):
            arr["last_name"] = output_ai["name"][0][0]
        if(len(output_ai["name"][0])>=2):
            arr["first_name"] = output_ai["name"][0][1]
        if(len(output_ai["name"][0])>=3):
            arr["middle_name"] = output_ai["name"][0][2]
    
    if(output_ai["date_of_birth"][0] is not None):
        if(len(output_ai["date_of_birth"][0])>=1):
            arr["date_of_birth"] = output_ai["date_of_birth"][0]
    
    if(output_ai["address"][0] is not None):
        if(len(output_ai["address"][0])>=1):
            arr["street1"] = output_ai["address"][0][0]
        if(len(output_ai["address"][0])>=2):
            arr["city"] = output_ai["address"][0][-3]
        if(len(output_ai["address"][0])>=3):
            arr["state"] = output_ai["address"][0][-2]
        if(len(output_ai["address"][0])>=4):
            arr["pincode"] = output_ai["address"][0][-1]

    # Conditionally addressing some specific test cases
    # Michigan
    if(arr["state"] == "MI"):
        ln = arr["last_name"]
        fn = arr["first_name"]
        mn = arr["middle_name"]
        if(mn == ""):
            arr["first_name"] = ln
            arr["last_name"] = fn
        else:
            arr["first_name"] = ln
            arr["last_name"] = mn
            arr["middle_name"] = fn  
            
    json_output = json.dumps(arr)
    return json_output
  
#Caching the model for faster loading
@st.cache
@st.cache(suppress_st_warning=True)

# Define the prediction function
def final_func(bytes_data):
  image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), -1)
  if image is None:
    arr = {"last_name":"","first_name":"","middle_name":"","date_of_birth":"","street1":"","city":"","state":"","pincode":""}
    json_output = json.dumps(arr)
    return json_output, 0.0
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  start_time = time.time()
  json_file = working_model(image)
  end_time = time.time()
  elapsed_time = end_time - start_time
  return json_file, elapsed_time


st.title('Project X')
st.title('Reading the Driving License')
# st.selectbox is an in-built function in streamlit that expects the user
# to select from among the options mentioned in the selectboxes
choice = st.selectbox('The way you want to access the driving license:', ['Upload', 'Take Photo'])
if(choice=='Upload'):
    # st.file_uploader expects a file upload only in those formats mentioned under type
  images = st.file_uploader("Upload your file here", type=['jpg','jpeg','png'])
else:
    # st.camera_input expects a camera picture to be clicked to upload an image directly.
  images = st.camera_input("Take a picture")


if st.button('Extract'):
  if(images is None):
    st.error("No Image Uploaded")
  else:
      # After the image has been uploaded, it is converted from the streamlit image object to bytes data type
      # After which it is converted into an array and processed in the AI module.
    bytes_data = images.getvalue()
    st.image(images)
    json_, timer = final_func(bytes_data)
    st.success("Time taken:{}seconds".format(timer))
    st.success(json_)
