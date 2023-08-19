# Image Processing Template Matching for Object Detection and Digit Recognition

This GitHub repository contains two distinct projects focused on image processing using template-matching techniques. The first part involves using various template matching algorithms such as `cv2.TM_CCOEFF`, `cv2.TM_CCOEFF_NORMED`, `cv2.TM_CCORR`, `cv2.TM_CCORR_NORMED`, `cv2.TM_SQDIFF`, and `cv2.TM_SQDIFF_NORMED` from the OpenCV library (`cv2`) to locate an object within an image. The identified object is then enclosed within a rectangle.

The second part of the project deals with image recognition. It involves loading an image of a handwritten digit and utilizing template matching in conjunction with the k-nearest neighbors (KNN) algorithm to predict the digit represented by the image. The program matches the input digit image against a dataset of digits and provides a prediction of the corresponding number.

## Table of Contents
- [Object Detection using Template Matching](#object-detection-using-template-matching)
- [Handwritten Digit Recognition](#handwritten-digit-recognition)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Object Detection using Template Matching

In this section, the template matching algorithms from OpenCV are applied to locate a specific object within an image. The algorithms consider various matching methods, and upon detection, a rectangle is drawn around the found object.

Two images are uploaded in this program one complete image and the other template that is to be matched in the image. The prgram shows the 5 closest matches not just the best one 
an example of the matched template is given below

**Image**

**Template**

## Handwritten Digit Recognition

This segment of the project is dedicated to recognizing handwritten digits using template matching and the KNN algorithm. An input image containing a handwritten digit is compared against a dataset of digits. The algorithm then predicts the digit represented by the input image based on the closest matches in the dataset.

The complete dataset can be downloaded from the following link:

https://www.kaggle.com/competitions/digit-recognizer/data?select=train.csv


## Usage

1. Clone this repository to your local machine:
```
git clone https://github.com/Muhammad-Wajahat/Image-Processing-Template-Matching-for-Object-Detection-and-Digit-Recognition.git
```

2. Navigate to the project directory:

```
cd Image-Processing-Template-Matching-for-Object-Detection-and-Digit-Recognition
```


4. Install the required dependencies using `pip`:

```
pip install opencv-python
pip install pandas

```

