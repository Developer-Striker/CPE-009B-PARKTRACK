# This PyFile exist to convert PNG to ICO
import os
from PIL import Image

path_input = "ParkTrack_Icon.png"
path_output = "ParkTrack_Icon.ico"
image = Image.open(path_input)
image.save(path_output, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), 
(64, 64), (128, 128), (256, 256)])

print("Created 'ParkTrack_Icon.ico'")