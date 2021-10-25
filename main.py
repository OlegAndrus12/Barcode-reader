import os
import cv2
from pyzbar.pyzbar import decode

IMAGE_EXTENSIONS = [".png", ".jpg"]

def iterate_images(directory, extensions):
    pathes = list()
    for filename in os.listdir(directory):
        if filename.endswith(tuple(extensions)):
            pathes.append(os.path.join(directory, filename))
        else:
            continue
    return pathes

def BarcodeReader(image):
    img = cv2.imread(image)
    detectedBarcodes = decode(img)    
    barcodes_data = list()
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        barcodes_data = [barcode.data.decode('UTF-8') for barcode in detectedBarcodes if barcodes_data != ""]
    return " or ".join(barcodes_data)

def assign_codes_to_clients(clients_filename):
    global IMAGE_EXTENSIONS
    clients = open(clients_filename, "r").read().splitlines()
    images = iterate_images("images/", IMAGE_EXTENSIONS)
    with open("barcodes_for_clients", "w") as file:
        file.write("Client name" + "    " + "Barcode" + "\n")    
        for image in enumerate(images): 
            barcode = BarcodeReader(image[1])
            try:
                client = clients[image[0]]
            except IndexError:
                print("There are more barcodes than users")
                break
            file.write(client + "    " + barcode + "\n")

if __name__ == "__main__":
    assign_codes_to_clients("clients.txt")