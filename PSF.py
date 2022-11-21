"""Image convolution using kernel of a matrix which is generated on the fly."""

from typing import List

from PIL import Image

import cv2 as cv

from skimage.util import random_noise


def main() -> None:
    image = cv.imread("samples/Untitled.png", 0)
    image_sigma_005 = random_noise(image, var=0.05) * 200
    image_sigma_01 = random_noise(image, var=0.1) * 200
    image_sigma_005 = cv.GaussianBlur(image_sigma_005, (5, 5), 2) * 1.5
    image_sigma_01 = cv.GaussianBlur(image_sigma_01, (5, 5), 2) * 1.5
    image_sigma_01.round(2)
    image_sigma_005.round(2)
    image_sigma_01.astype(int)
    image_sigma_005.astype(int)
    cv.imwrite("samples/Untitled-Edited-Sigma-005.png", image_sigma_005)
    cv.imwrite("samples/Untitled-Edited-Sigma-01.png", image_sigma_01)


if __name__ == "__main__":
    main()
