import os, sys
from PIL import Image

source = sys.argv[1]
dest = sys.argv[2]

if os.path.exists(source):
    print(True)
    
if not os.path.exists(dest):
    os.mkdir(dest)

for filename in os.listdir(source):
    with Image.open(os.path.join(source,filename)) as img:
        clean_name = os.path.splitext(filename)[0]
        target_file = os.path.join(dest,f'{clean_name}.png')
        print(target_file)
        img.save(target_file, "png")
        print("Done")
