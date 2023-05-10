import os
import shutil
from fastapi import UploadFile


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


def billValue(file: UploadFile, folder_name: str, filename: str) -> str:
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