import cv2
from pyzbar import pyzbar

def read_qr_code(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Detect QR codes in the image
    qr_codes = pyzbar.decode(image)

    if not qr_codes:
        print("No QR code found.")
        return

    for qr_code in qr_codes:
        # Extract the bounding box location of the QR code and draw a rectangle around it
        (x, y, w, h) = qr_code.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # The QR code data is a bytes object, so convert it to a string
        qr_code_data = qr_code.data.decode("utf-8")
        qr_code_type = qr_code.type

        # Print the QR code data and type
        print(f"Decoded {qr_code_type}: {qr_code_data}")

        # Display the result
        cv2.putText(image, qr_code_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the image with QR codes highlighted
    cv2.imshow("QR Code Reader", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")
    read_qr_code(image_path)
