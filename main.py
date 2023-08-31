import hashlib
import json

import uvicorn
from redis import Redis
from image_reader import read_text_from_img
from analyzer import find_credentials

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI()
redis = Redis(host='redis', port=6379, db=0)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}
upload_temp_dir = "upload_temp"


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    """
    FastAPI endpoint for upload and analyze image.
    :param file: The Image.
    :return: Response
    """
    if not allowed_file(file.filename):
        return JSONResponse(content={"status": "bad request. wrong file format."}, status_code=400)

    image_path = os.path.join(upload_temp_dir, file.filename)
    with open(image_path, "wb") as image_file:
        shutil.copyfileobj(file.file, image_file)

    image_data = open(image_path, 'rb').read()
    image_hash = hashlib.md5(image_data).hexdigest()

    cached_result = redis.get(image_hash)
    if cached_result is not None:
        byte_res = bytes(cached_result)
        cleaned_string = byte_res.decode("utf-8")
        json_data = json.loads(cleaned_string)
        return JSONResponse(content=json_data)

    recognized_text = read_text_from_img(image_path)
    if recognized_text.strip() != "":
        result = find_credentials(recognized_text)
        json_string = json.dumps(result)
        redis.set(image_hash, json_string)
        return result
    else:
        return JSONResponse(content={"status": "No text found."}, status_code=204)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
