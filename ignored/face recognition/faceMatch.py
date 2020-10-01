from modules import *

img_bill = face_recognition.load_image_file('./img/known/bill-gates.jpg')
bill_face_encoding = face_recognition.face_encodings(img_bill)[0]

unknown_img = face_recognition.load_image_file('./img/unknown/unknown6.jpg')
unknown1_face_encoding = face_recognition.face_encodings(unknown_img)[0]

#compare faces
results = face_recognition.compare_faces([bill_face_encoding], unknown1_face_encoding)
#print(bill_face_encoding)

if results[0]:
    print('This is Bill Gates')
else:
    print('Unidentified person')