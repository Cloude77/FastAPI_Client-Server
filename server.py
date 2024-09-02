from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()
UPLOAD_DIRECTORY = "./uploaded_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@app.post("/upload")
async def uploaded_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

    with open(file_path, "wb") as buffer:
        for chunk in iter(lambda: file.file.read(1024), b""):
            buffer.write(chunk)

    return {"filename": file.filename}

@app.get("/download")
async def download_file(filename: str):
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)

    if not os.path.join(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(path=file_path, filename=filename)



