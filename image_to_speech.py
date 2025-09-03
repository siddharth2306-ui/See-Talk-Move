from PIL import Image
import pytesseract
import pyttsx3

# Load the image
image = Image.open('final.PNG')

# Use Tesseract to extract text
text = pytesseract.image_to_string(image)
print("Extracted Text:", text)

# Initialize the TTS engine
engine = pyttsx3.init()

# Convert text to speech
engine.say(text)
engine.runAndWait()