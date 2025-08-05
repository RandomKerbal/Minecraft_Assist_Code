from pathlib import Path
from PIL import Image, ImageOps


def resize_png_images(input_path, size=(360, 360)):
    input_path = Path(input_path)

    for file_path in input_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() == '.png':
            with Image.open(file_path) as img:

                # resize canvas to a square, centering the original and filling with transparency
                img = ImageOps.pad(
                    img,
                    (max_l := max(img.size), max_l),
                    color=(0, 0, 0, 0),  # transparent fill
                    centering=(0.5, 0.5)  # middle of both axes
                )
                # rescale to 360*360
                img_resized = img.resize(size, Image.LANCZOS)

                # remove alpha translucency
                try:
                    r, g, b, a = img_resized.split()
                except ValueError:
                    print('Image does not have an alpha channel. Please save it in RGBA mode.')

                def a_round(a: int) -> int:
                    return 255 if a > 170 else 0

                a_opaque = a.point(a_round)
                img_opaque = Image.merge('RGBA', (r, g, b, a_opaque))

                save_path = input_path / file_path.name
                img_opaque.save(save_path)
                print(f"Resized and removed translucency: {save_path}")


if __name__ == "__main__":
    resize_png_images('D:\\My Downloads\\dwall_item_textures')
