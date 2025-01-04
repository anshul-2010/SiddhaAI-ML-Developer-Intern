from fastapi import FastAPI
from auth.router import router as auth_router
from patient.router import router as patient_router

app = FastAPI()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get("/")
async def home():
    return {"status": 200}


app.include_router(auth_router)
app.include_router(patient_router)
