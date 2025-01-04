# Introduction 
This AI module is designed to extract the text from a driver's license using advanced deep learning techniques to automatically recognize and extract relevant information from the images of driver's licenses. This module can greatly streamline the processes that require manual data entry or verification.

# Details
YOLO_All_3.pickle - This is the pickle file that contains the weights of the YOLO deep learning model, which is being employed to identify the region of interest for the different categories of input desired.

YOLO_DOB.pickle - This is the pickle file that contains the weights of the YOLO deep learning model, which is being employed to identify only the date of birth format on the license image.

Project X - Ai.py - This is the python script file that contains the code to take in the driving license image as input and return the json file with the extracted text for different categories.

streamlit.py - This contains the code of a simple deployment of the above AI module, wherein, the image, on obtaining from the user, is first converted into bytes string and then processed.

Project X - Ai.ipynb - This is the jupyter notebook that contains the code to take in the driving license image as input and return the json file with the extracted text for different categories.

# Installation of libraries.
1. On Ubuntu, or a Linux based system, we use two libraries tesseract-ocr and libtesseract-dev, which help in setting up the configuration for the OCR module to extract text from the image.
2. PIL and OpenCV library for image processing.
3. Numpy library for numerical computations.
4. Pandas library for data manipulation and analysis.
5. os module for interacting with the operating system.
6. json module for working with JSON data. This will be the format of files that is returned.
7. Python datetime module for time tracking.