import os
import shutil
from fastapi import UploadFile
import pyttsx3
import cv2
from pytesseract import pytesseract

pytesseract.tesseract_cmd = "env\\Tesseract-OCR\\tesseract.exe"

from Models.Bill.response import Response


def billType(file: UploadFile, folder_name: str, filename: str) -> str:
    """
    Saves the uploaded file to the specified folder and returns the filename
    """
    # create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # save the file to the folder
    with open(os.path.join(folder_name, filename), "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # return the filename
    return filename


# def billValue(file: UploadFile, folder_name: str, filename: str) -> Response:
#
#     # create the folder if it doesn't exist
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)
#
#     # save the file to the folder
#     with open(os.path.join(folder_name, filename), "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)
#
#     response = {"issuccess": True, "message": filename}
#
#     return response

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

    due = 'DUE'
    text = pytesseract.image_to_string(img)
    words = text.split()

    try:
        is_index = words.index(due)
    except ValueError:
        # handle case where 'DUE' keyword does not exist
        return {"issuccess": False, "message": "total not found"}

    is_index = words.index(due)

    if is_index + 1 < len(words):
        next_word = words[is_index + 1]
    else:
        response = {"issuccess": True, "message": ' No number found after total.'}

    response = {"issuccess": True, "message": next_word}

    return response
