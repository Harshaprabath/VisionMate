import os
import shutil

import cv2
from fastapi import FastAPI, File, UploadFile, APIRouter
from pytesseract import pytesseract

from Services.BillServices.billService import billValue

router = APIRouter()

# @router.post("/bill/type/")
# async def bill_value(file: UploadFile = File(...)):
#     filename = "billvideo.mp4"
#     folder_name = "Storage/Bill"
#     filename = billType(file, folder_name, filename)
#     return {"filename": filename}

@router.post("/bill/value/")
async def bill_value(file: UploadFile = File(...)):
    filename = "billvalue.jpg"
    folder_name = "Storage/Bill"
    res = billValue(file, folder_name, filename)
    return res

@router.post("/bill/type/")
async def bill_values(file: UploadFile = File(...)):
    filename = "billvideo.mp4"
    folder_name = "Storage/Bill"

    res = billValue(file, folder_name, filename)

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Save the video file to the folder
    file_path = os.path.join(folder_name, filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Perform text detection on the video
    detected_text = []
    video_capture = cv2.VideoCapture(file_path)
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        text = pytesseract.image_to_string(frame)
        detected_text.append(text)

    # Process the detected text as required
    # ...

    # Return the detected text or any other desired response
    return {"detected_text": detected_text}