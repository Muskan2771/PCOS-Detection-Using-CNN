from PIL import Image
import os

folders = [
    "dataset/train",
    "dataset/test"
]

for folder in folders:
    print(f"\nChecking {folder}")

    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)

            try:
                img = Image.open(path)
                img.verify()

            except Exception as e:
                print(f"Bad file: {path}")
                print(e)