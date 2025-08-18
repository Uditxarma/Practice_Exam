from config import allowed_extension
import os
from pathlib import Path


# path = "Sample file"
# def allowed_ext():
#     for file in os.listdir(path):
#         print(file)
#         print(type(file))               #str
#         ext = file.rsplit(".",1)[-1]
#         print(ext)
#         if ext in allowed_extension:
#             print("Proceed")

# allowed_ext()

from fastapi import UploadFile, File, FastAPI
app = FastAPI()
@app.post("Upload_file")
def upload_file(resumefile: UploadFile =  File(...)):
    print(resumefile.filename)
    name = resumefile.filename
    if '.' in name:
        print("Exist")
        ext = name.rsplit(".",1)[-1].lower()
        if ext in allowed_extension:
            print("Allowed Extension")