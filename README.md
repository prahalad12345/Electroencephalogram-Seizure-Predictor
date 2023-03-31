# Electroencephalogram-Seizure-Predictor

**Prediction of Seizure using Mindwave Neurosky..**

## Glossary
| Term      | Description |
| ----------- | ----------- |
| Spectrogram     | A spectrogram is a visual representation of the spectrum of frequencies of a signal as it varies with time.  |
| Fourier Transform     | the Fourier transform is a transform that converts a function into a form that describes the frequencies present in the original function.  |
| Seizure | A seizure is a sudden, uncontrolled burst of electrical activity in the brain. It can cause changes in behavior, movements, feelings and levels of consciousness.|

Seizure prediction is a critical area of research that aims to improve the quality of life for individuals living with epilepsy. Epilepsy is a neurological disorder that affects millions of people worldwide, and seizures can have a significant impact on a person's daily life. Predicting when a seizure might occur can provide individuals with epilepsy and their caregivers with advanced warning, allowing them to take appropriate precautions and potentially reduce the risk of injury. In recent years, machine learning and artificial intelligence have shown promise in accurately predicting seizures before they occur. In this project, we aim to develop a model that can predict seizures with high accuracy, using data from wearable devices, Mindwave Neurosky.



## Mindwave Neurosky
![YaDV Architecture](https://www.researchgate.net/profile/Kishore-Kashyap/publication/335799153/figure/fig1/AS:802856919654400@1568427414660/Neurosky-MindWave-Mobile-EEG-Headset-It-resides-five-main-parts-namely-Rubber-sensor.jpg)


## Core Capabilities
1. Load and View DICOM Image
2. View DICOM Head Metadata Information
3. Basic DICOM Image Operation – i.e. Rotation, Zoom, Measurement etc.
4. Image Classification
5. 3D image rendering using Marching Cube
6. Anonymize during export
7. Cloud Deployed (Demo purpose deployed in AWS EC2 instance)

## Prerequisites
Make sure you have installed all of the following prerequisites on your development machine:

* Git - [Download & Install Git](https://git-scm.com/downloads). OSX and Linux machines typically have this already installed.
* Python - [Download & Install Python3](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) - Minimum requirement 3.8.x


## Installation
YaDV is based on streamlit and streamlit can also be installed in a virtual environment on Windows, Mac and Linux. 

```bash
pip install -r requirement.txt
```

[OR]


```bash
pip install streamlit
pip install numpy
pip install fastai
pip install -Uqq fastbook
pip install pytorch
pip install streamlit-drawable-canvas
pip install cryptohash
pip install pandas
pip install pydicom
pip install opencv-python
pip install skimage
pip install matplotlib
pip install plotly
pip install mplot3d-dragger
pip install graphviz
pip install scikit-image
```

## Running YaDV
YaDV can be executed used following command:

```bash
cd yadv-dicom-imageprocessing
mkdir overlayimage
mkdir Exportfile
streamlit run yadv.py
```

## Development

```bash
git clone https://github.com/prahalad12345/yadv-dicom-imageprocessing.git
```

## 3rd Party Library Dependencies 
YaDV uses following 3rd party tools/libraries:

| 3rd Party      | Reference Link |
| ----------- | ----------- |
| OpenCV | https://opencv.org/|
| PyDICOM | https://pydicom.github.io/ |
| Fast.ai | https://www.fast.ai/ |
| Streamlit | https://streamlit.io/ |
| Numpy | https://numpy.org/ |
| Pandas | https://pandas.pydata.org/ |
| Matplot | https://matplotlib.org/ |
| Mplot3d | https://matplotlib.org/ |
| Plotly | https://plotly.com/ |
| SkImage | https://scikit-image.org/ |
| Cryptohash | https://www.cryptohash.net/ |

## Next Step
1. The Value Of Interest Lookup (VOI LUT - 0028, 3010) Table Implementation
2. Hand Gesture based Image operation - End Goal (New viewer different from YaDV tech stack)
3. Open multiple image in parallel and compare
4. Predict COVID cases based on CT Images
5. Predict COVID cases based on XRays
6. Integration with PACS
7. Scan patient, auto face detect and pull patient history from PACS
8. Advance measurement overlay on top of images

## Reference

| Topic      | Reference Link |
| ----------- | ----------- |
| Digital Image Communication in Medicine | Book from Oleg S. Pianykh |
| National Electrical Manufacturers Association (NEMA) | http://dicom.nema.org/medical/dicom/current/output/chtml/part10/chapter_7.html |
| Python library for DICOM | https://pypi.org/project/pydicom/  |
| FAST.AI for Medical Image Processing | https://docs.fast.ai/medical.imaging |
| User Interface for Image Viewer | https://streamlit.io/ |
| Heroku Deployment | https://towardsdatascience.com/deploying-a-basic-streamlit-app-to-heroku-be25a527fcb3 |
| AWS Deployment | https://towardsdatascience.com/how-to-deploy-a-streamlit-app-using-an-amazon-free-ec2-instance-416a41f69dc3|

## FAQ
1.  If you get "ImportError: libGL.so.1: cannot open shared object file" error message install following package:
    ```bash
    sudo apt install libgl1-mesa-glx
    ```

## License

YaDV is completely free and open-source 
