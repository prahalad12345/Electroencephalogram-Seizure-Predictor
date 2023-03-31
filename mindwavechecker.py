import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
import textwrap
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Flatten 
from tensorflow.keras.layers import Conv2D,MaxPooling2D 

import scipy.io 
from scipy.signal import spectrogram
import matplotlib.pyplot as plt
import os
import random
import numpy as np

def model_init(inputshape):
	model = Sequential() 
	model.add(Conv2D(16,(3,3),activation='relu',input_shape=inputshape))
	model.add(Conv2D(16,(3,3),activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.25))
	model.add(Flatten())
	model.add(Dense(32, activation='relu'))
	model.add(Dropout(0.5))
	model.add(Dense(2, activation='sigmoid'))

	model.compile(loss=tf.keras.losses.binary_crossentropy,
		      optimizer=tf.keras.optimizers.RMSprop(),
		      metrics=['accuracy'])
	return model
	

if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    try:
        if (mindwaveDataPointReader.isConnected()):
            time=5000
            dpoints=[]
            print("REading")
            while time>0:
                dataPoint = mindwaveDataPointReader.readNextDataPoint()
                if (dataPoint.__class__ is RawDataPoint):  #Only want the raw vals
                    dataPoint = str(dataPoint)
                    print(dataPoint)
                    dataPoint=dataPoint[11:len(dataPoint)]
                    dataPoint=int(dataPoint)
                    print(dataPoint)
                    dpoints.append(dataPoint)
                    time-=1
                
                 
            dpoints=np.array(dpoints)
            dpoints=dpoints.T 

            p_f,p_t,p_sxx = spectrogram(dpoints,fs=5000,return_onesided=False)
            p_ss = np.log1p(p_sxx)
            arr=p_ss[:]/np.max(p_ss)


            input_shape = (256,22,1)
            checkpoint_path='./training/training.ckpt'
            model=model_init(input_shape)
            model.load_weights(checkpoint_path)
            print(arr.shape)
            arr=np.reshape(arr,(256,22,1))
            
            arr=np.reshape(arr,(1,256,22,1))

            prediction=model.predict(arr)
            classess= np.argmax(arr)
            print(classess)
            if classes==1: 
                print('No Seizure')
            else:
                print("Alert : Seizure")



        else:
            print((textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " ")))
    except KeyboardInterrupt:
        sys.exit()