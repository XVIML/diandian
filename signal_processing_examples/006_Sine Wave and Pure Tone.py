#===This Frame is generated by DRPython ===============================
import sys
import os
import drvi.drviAppendPath as mPath
mPath.appendPythonPath()
#=================================================

import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import filedialog
import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import drvi.drviDSP as dsp
import drvi.drviControlls as dr
import drvi.drviSimpleAudio as sa

#=========================================
def setValue1(v):
 Fs=44100;
 dt=1.0/Fs;
 N=40000;
 mF=500*1.13**v
 tData=np.arange(N)*dt
 xData=0.8*np.sin(2*np.pi*mF*tData)
 mPlotWave.setValue2D(tData,xData)
 [mFre,mAmp]=dsp.AmpSpetrumX(N,Fs,xData)
 mPlotAmp.setValue2D(mFre,mAmp)
 mDigital1.setValueSingle(mF)

def setValue(v):
 Fs=44100;
 dt=1.0/Fs;
 N=40000;
 mF=500*1.13**v
 tData=np.arange(N)*dt
 xData=0.8*np.sin(2*np.pi*mF*tData)
 mPlotWave.setValue2D(tData,xData)
 [mFre,mAmp]=dsp.AmpSpetrumX(N,Fs,xData)
 mPlotAmp.setValue2D(mFre,mAmp)
 mDigital1.setValueSingle(mF)
 
 w=signal.windows.tukey(N,0.1);   
 y=xData*w
 sa.play(1,Fs,y,0)

 
#==Main Window=====================
win= tk.Tk()
sWOld=1920
sHOld=1080
sWidth=win.winfo_screenwidth()
sHeight=win.winfo_screenheight()
wRate=sWidth/sWOld
hRate=sHeight/sHOld
winWidth=int(1100*wRate)
winHeight=int(670*hRate)
x=(sWidth-winWidth)/2;
y=(win.winfo_screenheight()-winHeight)/2
win.geometry("%dx%d+%d+%d" %(winWidth,winHeight,x,y))
win.config(bg="#ddeeee")
win.wm_title('Sine Wave and Pure Tone')

#==Layout of controls=====================
mLab1=dr.DRLabelX(win,20*wRate,30*hRate,400*wRate,40*hRate,'#003355','#ffffff','Sine Wave and Pure Tone',20)
mPlotWave=dr.DRPlotX(win,20*wRate,80*hRate,1000*wRate,250*hRate,'','#003355','#000000','#ffffff','#00eeff','#ffff00',0,0.01,-1,1,0,0)
mPlotAmp=dr.DRPlotX(win,20*wRate,320*hRate,1000*wRate,250*hRate,'','#003355','#000000','#ffffff','#00eeff','#ffff00',0,2500,0,1,0,0)
mHBut2=dr.DRHButtonGroup(win,20*wRate,580*hRate,1000*wRate,50*hRate,'#002233','#ffffff','1,2,3,4,5,6,7,8,9',9,1)
mDigital1=dr.DRDigital(win,920*wRate,40*hRate,100*wRate,36*hRate,'#000000','#00ffaa',0,0,22)

#==DataStream Binding=====================
mHBut2.addCallBackSingle(setValue)
setValue1(1)
    
#==Main Loop=====================
win.mainloop()

#==End of APPp=====================

