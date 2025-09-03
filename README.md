# Speech & Text Processing with OCR, TTS, and G-code Conversion  

## 📌 Overview  
This project demonstrates:  
- Extracting text from images using **Tesseract OCR**.  
- Converting extracted text into **speech**.  
- Capturing **live speech input** and converting it to text.  
- Mapping recognized text into **G-code commands** (useful for CNC/plotters).  

It contains two scripts:  
- **`img.py`** → Image-to-Text + Text-to-Speech.  
- **`txt.py`** → Speech-to-Text + Text-to-Gcode.  

---

## ⚙️ Installation  

1. Create a virtual environment (recommended):  
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
```

2. Install dependencies:  
```bash
pip install -r requirements.txt
```

---

## 📦 Requirements  

`requirements.txt` should contain:  
```
pillow
pytesseract
pyttsx3
speechrecognition
googletrans==4.0.0-rc1
pyaudio
```

Additionally, install **Tesseract OCR**:  

- **Linux (Debian/Ubuntu):**  
  ```bash
  sudo apt install tesseract-ocr
  ```
- **Windows:**  
  Download and install from [Tesseract OCR for Windows](https://github.com/UB-Mannheim/tesseract/wiki).  

---

## 🚀 Usage  

### 1. Extract text from image + TTS  
```bash
python image_to_Speech.py
```
- Loads `final.PNG` (edit script to change file).  
- Extracts text → Reads it aloud.  

### 2. Speech to G-code  
```bash
python text_to_Gcode.py
```
- Listens from microphone (up to 40s).  
- Converts speech → text.  
- Maps text characters to **G-code commands**.  

---

## 🛠️ Project Structure  
```
speech-text-gcode/
│── img.py        # Image OCR + TTS
│── txt.py        # Speech Recognition + G-code mapping
│── requirements.txt
│── README.md
```

---

## 🔮 Future Improvements  
- Expand G-code mapping for full alphabets & shapes.  
- Add **translation step** for multilingual support.  
- GUI integration for user-friendly interface.  
- CNC/Plotter hardware integration.  

