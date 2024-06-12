import cv2
import os

# Read the image
img = cv2.imread("scenery.jpg")

# Input secret message and passcode
secret_message = input("ENTER SECRET MESSAGE: ")
password = input("ENTER A PASSCODE: ")

char_to_int = {chr(i): i for i in range(256)}
int_to_char = {i: chr(i) for i in range(256)}

height, width, _ = img.shape

# Encrypt the message into the image
row, col, channel = 0, 0, 0
for i in range(len(secret_message)):
    img[row, col, channel] = char_to_int[secret_message[i]]
    col += 1
    if col == width:
        col = 0
        row += 1
    channel = (channel + 1) % 3

# Saving the encrypted image
cv2.imwrite("encryptedimage.jpg", img)
os.startfile("encryptedimage.jpg")

# Decrypting the message from the encrypted image
decoded_message = ""
row, col, channel = 0, 0, 0
passcode = input("ENTER PASSCODE FOR DECODE: ")
if password == passcode:
    for i in range(len(secret_message)):
        decoded_message += int_to_char[img[row, col, channel]]
        col += 1
        if col == width:
            col = 0
            row += 1
        channel = (channel + 1) % 3
    print("Decoded message is:", decoded_message)
else:
    print("You entered a wrong passcode.")
