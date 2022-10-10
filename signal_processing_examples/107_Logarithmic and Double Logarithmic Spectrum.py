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
import drvi.drviDSP as dsp
import drvi.drviControlls as dr

#=========================================

def setValue2D(t,x):
 Fs=1/(t[1]-t[0]);
 N=len(x)
 mPlotWave.setValue2D(t,x)
 [mFre,mAmp]=dsp.AmpSpetrum(N,Fs,x)
 mPlotAmp.setValue2D(mFre,mAmp)
 mPlotSemiX.setValue2D(mFre,mAmp)
 mPlotSemiY.setValue2D(mFre,mAmp)
 mPlotLoglog.setValue2D(mFre,mAmp)
 
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
win.wm_title('Linear, Logarithmic and Double Logarithmic Spectrum')


#==Layout of controls=====================
dr.DRLabelX(win,570*wRate,35*hRate,60*wRate,36*hRate,'#ddeeee','#000000','Fre',14)
mLab1=dr.DRLabelX(win,20*wRate,30*hRate,480*wRate,40*hRate,'#003355','#ffffff','Linear, Log and LogLog Spectrum',20)
mPlotWave=dr.DRPlotX(win,20*wRate,80*hRate,1040*wRate,200*hRate,'','#003355','#000000','#ffffff','#00eeff','#ffff00',0,0.05,-1,1,0,0)
mPlotAmp=dr.DRPlotX(win,20*wRate,265*hRate,520*wRate,190*hRate,'','#003355','#000000','#ffffff','#00eeff','#ffff00',0,5000,0,1,0,0)
mPlotSemiX=dr.DRSemilogXX(win,20*wRate,450*hRate,520*wRate,190*hRate,'','#003355','#000000','#ffffff','#00eeff','#ffff00',10,10000,0,1,0,0)
mPlotSemiY=dr.DRSemilogYX(win,540*wRate,265*hRate,520*wRate,190*hRate,'','#003355','#000000','#ffffff','#00eeff','#ffff00',10,10000,0,0,0,0)
mPlotLoglog=dr.DRLoglogX(win,540*wRate,450*hRate,520*wRate,190*hRate,'','#003355','#000000','#ffffff','#00eeff','#ffff00',10,10000,0,0,0,0)
mVButType=dr.DRComboBox(win,940*wRate,35*hRate,120*wRate,36*hRate,'1.Sine,2.Square,3.Trangle,4.Noise',0,4)
mKnobFre=dr.DRHSlider(win,630*wRate,35*hRate,300*wRate,36*hRate,'#444444','#880000','#008822',8,20,1,1000,50)

mType=0; Fs=44100; N=4096; A=0.6; Fre=100; Pha=0
mSignal=dsp.DRGenerator(mType,Fs,N,A,Fre,Pha)

#==DataStream Binding=====================
mSignal.addCallBackValue2D(setValue2D)
mVButType.addCallBackSingle(mSignal.setSignalType)
mKnobFre.addCallBackSingle(mSignal.setSignalFre)

 
    
#==Main Loop=====================
win.mainloop()

#==End of APPp=====================
