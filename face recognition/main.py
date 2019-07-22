from modules import *

image = face_recognition.load_image_file("./img/unknown/unknown3.jpg")
face_locations = face_recognition.face_locations(image)

#Array of coordinates for each face
print(face_locations)
print(f'There are {len(face_locations)} people in this image')