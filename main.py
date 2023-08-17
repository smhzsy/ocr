import uvicorn

from image_reader import read_text_from_img
from testfile import veri_bul

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI()


upload_temp_dir = "upload_temp"
os.makedirs(upload_temp_dir, exist_ok=True)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_path = os.path.join(upload_temp_dir, file.filename)
        with open(image_path, "wb") as image_file:
            shutil.copyfileobj(file.file, image_file)

        recognized_text = read_text_from_img(image_path)
        if recognized_text.strip() != "":

            return veri_bul(recognized_text)
        else:
            return "Metin tespit edilemedi."
    except Exception:
        return JSONResponse(content={"message": "Error uploading image"}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)