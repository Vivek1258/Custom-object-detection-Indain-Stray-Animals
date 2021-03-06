# Indian Stray Animal Detection

### End to End | YOLO_V5 | Custom Dataset | REST API  

[![License: FDL 1.3](https://img.shields.io/badge/License-FDL%20v1.3-blue.svg)](https://www.gnu.org/licenses/fdl-1.3)
![Code Coverage](https://img.shields.io/badge/coverage-80%25-green)
![python Version](https://img.shields.io/pypi/pyversions/Django)
 
## Table of content

- [Project Overview ](#Project-Overview )
- [Output](#Output)
- [Algothrim](#Algothrim)
- [DataSet](#DataSet) 
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Get Help](#get-help)
- [Contact](#contact)


## Project Overview

In this project, I have developed and deployed  a custom object detection model that can be used to detect stray animals (cow and dogs ). The dataset is created by taking custom images from google image search. The Machine Learning Model is developed, trained, and deployed(as a REST API ) on Heroku Cloud using Python-Flask.  

## Output

### Real Time Inference 

![demo](/images/output.gif)

video used for inference source : [wildfilmsindia](https://www.youtube.com/watch?v=pit4FU2lxZQ&t=52s)

### Deployed API 

![image](https://user-images.githubusercontent.com/53163419/120688561-d1f21400-c4c0-11eb-9917-cb29a0f2d059.png)

Image used for inference source : [Getty Images](https://media.gettyimages.com/photos/indian-domestic-stray-animals-picture-id1082294270?s=2048x2048)

## Algothrim

YOLO an acronym for 'You only look once', is an object detection algorithm that divides images into a grid system. Each cell in the grid is responsible for detecting objects within itself.

YOLO algorithm is an algorithm based on regression, instead of selecting the interesting part of an Image, it predicts classes and bounding boxes for the whole image in one run of the Algorithm.
 
YOLO is one of the most famous object detection algorithms due to its speed and accuracy.

[YOLO_V5 Documentation](https://docs.ultralytics.com/)

## DataSet

### Data Collection:
Various images of cows and dogs are collected from Google Image search under [creative common lisences](https://support.google.com/websearch/answer/29508?hl=en&co=GENIE.Platform%3DAndroid). 

### Data Lebeling:

#### lebaling tool : [makesence.ai](https://www.makesense.ai/)

#### YOLO format:   one *.txt file per image (if no objects in image, no *.txt file is required). 

#### The *.txt file specifications are:

- One row per object
- Each row is class x_center y_center width height format.
- Box coordinates must be in normalized xywh format (from 0 - 1). {If your boxes are in pixels, divide x_center and width by image width, and y_center and height by image height.}
- Class numbers are zero-indexed (start from 0).

## Built With

Python

Pytorch

Flask 


## Contributing

#### Issues

In the case of a bug report, bugfix or suggestions, please feel free to open an issue.

#### Pull request

Pull requests are always welcome, and I will do my best to do reviews as fast as we can.


## License

This project is licensed under the [GNU General Public License](https://github.com/Vivek1258/Custom-object-detection-Indain-Stray-Animals/blob/main/LICENSE)

## Get Help

- If appropriate, [open an issue](https://github.com/Vivek1258/Custom-object-detection-Indain-Stray-Animals/issues) on GitHub. 
- Or contact me on linkedin 

## Contact 

- Contact me on [LinkedIn](https://www.linkedin.com/in/vivek-mankar-182735184/) 
- Email mankarvivek172000@gmail.com
 





