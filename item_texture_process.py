from pathlib import Path
from PIL import Image


def resize_png_images(input_path, size=(360, 360)):
    input_path = Path(input_path)

    for file_path in input_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() == '.png':
            with Image.open(file_path) as img:
                img_resized = img.resize(size, Image.LANCZOS)

                save_path = input_path / file_path.name
                img_resized.save(save_path)
                print(f"Resized and saved: {save_path}")


if __name__ == "__main__":
    resize_png_images('D:\\My Downloads\\dfence_items_texture')
