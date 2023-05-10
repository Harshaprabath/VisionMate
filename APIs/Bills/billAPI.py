from fastapi import FastAPI, File, UploadFile, APIRouter

from Services.BillServices.billService import billValue,billType

router = APIRouter()

@router.post("/bill/type/")
async def bill_value(file: UploadFile = File(...)):
    filename = "billtype.jpg"
    folder_name = "Storage/Bill"
    filename = billType(file, folder_name, filename)
    return {"filename": filename}

@router.post("/bill/value/")
async def bill_value(file: UploadFile = File(...)):
    filename = "billvalue.jpg"
    folder_name = "Storage/Bill"
    res = billValue(file, folder_name, filename)
    return res
