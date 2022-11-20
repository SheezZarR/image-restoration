"""Image convolution using kernel of a matrix which is generated on the fly."""

from typing import List

import numpy
import numpy as np
from PIL import Image
from PIL import ImageFilter as IFil


def generate_conv_matrix(size: int) -> List[List]:
    pass


def matrix_convolution(img_data_vec: List) -> List:
    box_blur = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    pass


def gaussian_convolution(image_as_vec: List) -> List:
    pass




def main() -> None:
    image = Image.open("samples/pic1.png")
    print(image.getbands())
    image_colors = list(image.getdata())    # List of (R, G, B) pixel by pixel

    for row in image_colors:
        print(row)

    i_filtered = image.filter(IFil.BoxBlur(radius=0.5))
    i_filtered.show(title="AfterBoxBlur")
    i_filtered.filter(IFil.GaussianBlur(radius=1)).show(title="AfterGauBlur")
    print("La Finalle")
    for row in i_filtered.getdata():
        print(row)


if __name__ == "__main__":
    main()
