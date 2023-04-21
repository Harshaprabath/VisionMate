import os
import shutil
from fastapi import UploadFile, APIRouter , File

router = APIRouter()

@router.post("/test/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # get the filename
    filename = file.filename


    # create the folder if it doesn't exist
    folder_name = "Storage/Test"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # save the file to the folder
    with open(os.path.join(folder_name,filename), "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # return a JSON response
    return {"filename": filename}
