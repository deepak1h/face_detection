# Face Detection using OpenCV


**Introduction:**

This is a sub-project from 2018 that focuses on face detection using OpenCV. It's a simple yet effective demonstration of how to detect faces and eyes in images or video streams. OpenCV is a powerful computer vision library, and with it installed, you can easily run this project.

**Getting Started:**

To run this project, you'll need to install OpenCV. You can typically install it using `pip`:

```bash
pip install opencv-python
```

**Classifiers:**

This project utilizes trained XML classifiers for detecting faces and eyes. You can find them here:

- Trained XML file for detecting faces: [haarcascade_frontalface_default.xml](https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
- Trained XML file for detecting eyes: [haarcascade_eye.xml](https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)

These classifiers describe specific features of the objects we want to detect (faces and eyes). A cascade function is trained from a dataset containing both positive (faces) and negative (non-faces) examples.

**Running the Project:**

You can run this project by executing either the provided Python file or notebook. Make sure you have OpenCV installed before running the code.

**Usage:**

This project is a valuable resource for anyone interested in learning about face detection with OpenCV. It serves as a starting point for more advanced computer vision applications.

Thank you for using OpenCV to explore the exciting world of computer vision!
