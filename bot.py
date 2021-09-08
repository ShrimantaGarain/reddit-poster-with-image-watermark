import os
from os.path import isfile, join

from PIL import Image
def automation():
    # required initializations
    file_extensions = ('.jpg', '.jpeg')
    in_directory = f"{os.path.dirname(os.path.abspath(__file__))}/{'pre'}"
    out_directory = f"{os.path.dirname(os.path.abspath(__file__))}/{'post'}"
    onlyfiles = [f for f in os.listdir(in_directory) if isfile(join(in_directory, f))]
    pre_pictures=[f for f in onlyfiles if f.endswith(file_extensions)]


    # replacing jpg and jpeg with png
    for p in pre_pictures:
        if 'jpg' in p:
            image = Image.open(f'{in_directory}/{p}')
            x = p.replace("jpg", "png")
            image.save(f'{in_directory}/{x}')
        if 'jpeg' in p:
            image = Image.open(f'{in_directory}/{p}')
            x = p.replace("jpeg", "png")
            image.save(f'{in_directory}/{x}')
    for image in pre_pictures:
        os.remove(f'{in_directory}/{image}') 
    onlyfiles = [f for f in os.listdir(in_directory) if isfile(join(in_directory, f))]           
    pictures=[f for f in onlyfiles if f.endswith(".png")]
    # inserting images in templates
    for p in pictures:
        image = Image.open(f'{in_directory}/{p}')
        watermark = Image.open(r"D:\instabot\automarkwithtemp\mom.png")
        new_image=image.resize((720,507))
        watermark.paste(new_image,(0,120))
        watermark.save(f'{out_directory}/{p}')

    # deleting images from pre folder
    for image in pictures:
        os.remove(f'{in_directory}/{image}')


