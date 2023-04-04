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
![Neurosky](https://github.com/prahalad12345/Electroencephalogram-Seizure-Predictor/blob/main/image/Neurosky-MindWave-Mobile-device.ppm.png)


## Core Capabilities
1. Extracts raw values from mindwave
2. Calculate the extracted raw values in the form of STFT spectrogram
3. Predicts if the user is having a seizure or not
4. The model gave a 0.96 accuracy on the test set 

## Prerequisites
Make sure you have installed all of the following prerequisites on your development machine:
* Dataset - [dataset](https://www.kaggle.com/competitions/seizure-prediction/data).
* Git - [Download & Install Git](https://git-scm.com/downloads). OSX and Linux machines typically have this already installed.
* Python - [Download & Install Python3](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) - Minimum requirement 3.8.x
* Pybluez - [Bluetooth Configuration](https://github.com/pybluez/pybluez)
* Mindwave Configuration with python - [Mindwave configuration](https://github.com/robintibor/python-mindwave-mobile)

## Installation

Refer each of the code files to check on the modules

## Running YaDV
YaDV can be executed used following command:

```bash
python mindwavechecker.py
```

## Development

```bash
git clone https://github.com/prahalad12345/Electroencephalogram-Seizure-Predictor.git
```


## Reference

| Topic      | Reference Link |
| ----------- | ----------- |
| Introduction to EEG and Speech based Emotion Recognition | Book from Dr Babasaheb Ambedkar Marathwada University  Aurangabad, India |
| Python library to read data from Mindwave Neurosky | https://github.com/robintibor/python-mindwave-mobile 
| Reference the project | https://www.hackster.io/cnns4eegs/deep-learning-for-seizure-prediction-wearable-5ad2d3 


