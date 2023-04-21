from fastapi import FastAPI, File, UploadFile, APIRouter
import os
import shutil

router = APIRouter()


@router.post("/bill/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # get the filename
    #filename = file.filename
    filename = "bill.jpg"

    # create the folder if it doesn't exist
    folder_name = "Storage/Bill"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # save the file to the folder
    with open(os.path.join(folder_name,filename), "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # return a JSON response
    return {"filename": filename}
