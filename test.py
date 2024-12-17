"""
動作チェックをするためのPythonコードです。
以下のように出力される場合、きちんと設定ができています。
OpenCV version: 4.10.0
Pytesseract version: 5.5.0.20241111
"""

import os
import cv2
import pytesseract
from dotenv import load_dotenv

load_dotenv()

pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")

print(f"OpenCV version: {cv2.__version__}")
print(f"Pytesseract version: {pytesseract.get_tesseract_version()}")