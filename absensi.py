import qrcode

# Data siswa
student_id = "S1234"
student_name = "Rasya"

# Membuat data QR dari ID siswa
data = f"ID: {student_id}, Name: {student_name}"

# Membuat QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Membuat gambar dari QR Code
img = qr.make_image(fill='black', back_color='white')

# Menyimpan gambar QR Code
img.save(f"{student_name}_{student_id}.png")
import cv2
from pyzbar.pyzbar import decode

# Membaca gambar QR Code
image_path = "Rasya_S1234.png"
img = cv2.imread(image_path)

# Mendekode QR Code
decoded_objects = decode(img)

# Menampilkan hasil dekode
for obj in decoded_objects:
    print("Data:", obj.data.decode("utf-8"))
import datetime

# Mencatat kehadiran ke file
for obj in decoded_objects:
    student_info = obj.data.decode("utf-8")
    with open("attendance_log.txt", "a") as log_file:
        log_file.write(f"{student_info}, Time: {datetime.datetime.now()}\n")
