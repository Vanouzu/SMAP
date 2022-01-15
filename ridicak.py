import cv2
import argparse
import pytesseract

#Parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input file", required=True)
parser.add_argument("-o", "--output", help="Output base")
parser.add_argument("-l", "--lang", help="Language; must be existing one from installed Tesseract models (check tesseract --list-langs)", required=True)
args = parser.parse_args()

#Read file
image = cv2.imread(args.input)

#Preprocess - grayscale, blur and threshold
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#Set config from Tesseract
custom_config="--oem 1 --psm 6"

if args.output is not None:
    with open(args.output, 'w') as f:
        print(pytesseract.image_to_string(threshold, args.lang, config=custom_config), file=f)

else:
    print(pytesseract.image_to_string(threshold, args.output, args.lang, config=custom_config))

