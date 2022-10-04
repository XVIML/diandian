# DRVI
DRVI is a python GUI package that is based on Tkinter, it contains a group of virtual instrument widgets. You can install it by:

pip install drvi

DRVI and DRPython are also depended on six third packages. So you also need to install them yourself.

  pip install numpy
  
  pip install scipy
  
  pip install matplotlib
  
  pip install simpleaudio
  
  pip install PyAudio
  
  pip install Pyserial

Original python only support WAV format of audio file. If you want to analysis audio data in MP3 or MP4 files, you need to download and install an exectable ffmpeg, and change the ffmpeg.txt file's content to your ffmpeg path, like.

d:\ffmpeg511


To easy for useing of the drvi package, we write a APP designer and some examples here.

DRPythonIDE.py: an APP designer, you can layout a virtual instrument style GUI by drag, and then export it to python codes for quick design.   

![DRPython](https://user-images.githubusercontent.com/9141129/193712249-f4e485d4-8567-4165-b5cd-c8a81e3a53de.gif)


And some examples of virtual instrument style APP that is designed by drvi package are also aviable here.

![009_Time Waveform Analysis](https://user-images.githubusercontent.com/9141129/193711011-9578d7e3-0a2e-4802-80f7-5d76690e9475.gif)


A event driven and data driven architecture are includeed in the drvi package, which means a APP that is consist of drvi widgets and their callback functions can be driven by an event stream or a data stream. Thus, Using addCallBack to link event streams or data stream to other callback functions or other widget's set method, a event driven and data driven program is finished.

![DRVIExample_Play](https://user-images.githubusercontent.com/9141129/193713792-57d4527c-b2e6-44db-a2b9-6f45918c43a4.gif)


Below are codes of the WAV player, not so much comparing to its functions.

![DRVIExample_PlayCode](https://user-images.githubusercontent.com/9141129/193714957-97e855ee-7018-4cf9-aec5-6380d36eb1d2.png)


Whish you like it. 

And any suggestions are welcomed.

