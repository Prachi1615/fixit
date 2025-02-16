from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/api/input")
async def process_input(
    text: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
):
    """
    Handles different input types:
    - Text (as a form field)
    - File (image, video, or audio)
    """
    
    # Handle text input
    if text:
        return {"type": "text", "message": "Text received", "data": text}

    # Handle file input (image, video, audio)
    if file:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {"type": "file", "message": "File received", "filename": file.filename}

    return {"message": "No valid input received"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
