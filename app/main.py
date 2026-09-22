from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health_check():
    return{"status":"Everything is working perfectly fine!"}