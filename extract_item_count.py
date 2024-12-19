import os
import cv2
import pytesseract
from dotenv import load_dotenv

load_dotenv()

pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")

def find_images_and_read_number(screen_img_path, item_img_path):
    screen_img = cv2.imread(screen_img_path)
    item_img = cv2.imread(item_img_path)

    if screen_img is None or item_img is None:
        print("画像読み込みに失敗しちゃった...")
        return
    
    # グレースケールへの変換
    gray_screen = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)
    gray_item = cv2.cvtColor(item_img, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray_screen, gray_item, cv2.TM_CCOEFF_NORMED)
    threshold = 0.0
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        print(f"マッチした箇所:{max_loc}, 類似度:{max_val}")
        x, y = max_loc
        w, h = item_img.shape[:2]

        cv2.rectangle(screen_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imwrite("output.png", screen_img)

        
if __name__ == "__main__":
    find_images_and_read_number(screen_img_path="screen_test.png", item_img_path="item_list\CrystallineComponent.png")