import os
import shutil
from msilib.schema import File

from fastapi import UploadFile
import pyttsx3
import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "env\\Tesseract-OCR\\tesseract.exe"

from Models.Bill.response import Response





def billValue(file: UploadFile, folder_name: str, filename: str) -> Response:
    # create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # save the file to the folder
    with open(os.path.join(folder_name, filename), "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    img = cv2.imread(os.path.join(folder_name, filename))
    if img is None:
        # handle case where file could not be read
        return {"issuccess": False, "message": "Could not read image file"}

    total = 'payable'
    text = pytesseract.image_to_string(img)
    words = text.split()

    if "slt" in text or "SLT" in text or "Telecom" in text or "Sri Lanka Telecom" in text:
        type = "Sri Lanka Telecom"
    else:
        type = "404"

    try:
        is_index = words.index(total)
    except ValueError:
        # handle case where 'DUE' keyword does not exist
        return {"billType": type, "Value": "total not found"}

    is_index = words.index(total)

    if is_index + 1 < len(words):
        next_word = words[is_index + 1]
    else:
        response = {"billType": type, "Value": ' No number found after total.'}

    # response = {"billType": type, "Value": text}
    response = {"billType": type, "Value": next_word}
    print(text);
    return response
