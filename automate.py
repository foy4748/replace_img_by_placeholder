import os
from PIL import Image

from placeholder import create_placeholder_image

BASE_DIR = os.getcwd()

operation_directory = os.path.join(BASE_DIR, "input")

 
def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            listdirs(it)
        else:
            img = Image.open(it.path)
            w, h = img.size
            placeholder = create_placeholder_image(w,h)
            placeholder.save(it.path)


listdirs(operation_directory)
