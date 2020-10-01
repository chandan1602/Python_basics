from modules import *

# img_bill = face_recognition.load_image_file('./img/known/bill-gates.jpg')
# bill_face_encoding = face_recognition.face_encodings(img_bill)[0]

# img_mark = face_recognition.load_image_file('./img/known/mark-zuckerberg.jpg')
# mark_face_encoding = face_recognition.face_encodings(img_mark)[0]

# img_elon = face_recognition.load_image_file('./img/known/elon-musk.jpg')
# elon_face_encoding = face_recognition.face_encodings(img_elon)[0]

img_sunil = face_recognition.load_image_file('./img/known/sunil-grover.jpeg')
sunil_face_encoding = face_recognition.face_encodings(img_sunil)[0]

#print('JOBS FACE ENCODINGS : ', jobs_face_encoding)
#Create an array of encodings and names

known_face_encodings = [
    # bill_face_encoding,
    # mark_face_encoding,
    # elon_face_encoding,
    sunil_face_encoding
]

known_face_names = [
    "Sunil Grover"
]

#Load test image to find faces in
test_image = face_recognition.load_image_file('./img/unknown/unknown8.jpeg')

#Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)
#print('TEST IMAGE ENCODINGs', face_encodings)


#Convert to PIL format
pil_image = Image.fromarray(test_image)

#Create a image draw instance
draw = ImageDraw.Draw(pil_image)


#Loop through faces in test image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.70)

    name = "Unknown person".upper()

    #If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index].upper()

    #Draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    #Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255))

del draw

#Display the image
pil_image.show()
