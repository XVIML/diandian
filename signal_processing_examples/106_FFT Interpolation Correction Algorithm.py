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


#==CallBack Function==============
def myWorking(v):
 Fs1=1024;
 N1=1024 
 dt1=1.0/Fs1; 
 t1=np.arange(N1)*dt1
 x1=0.8*np.sin(2*np.pi*v*t1)
 mPlotWave1.setValue2D(t1,x1)
 [mFre,mAmp]=dsp.AmpSpetrum(N1,Fs1,x1)
 mPlotAmp.setValue2D(mFre,mAmp)
 [mFre,A1]=dsp.AmpSpetrumX(N1,Fs1,x1)
 mPlotAmp1.setValue2D(mFre,A1)
 return 1

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
win.wm_title('FFT Interpolation Correction Algorithm')

#==Layout of controls=====================
dr.DRLabelX(win,20*wRate,30*hRate,600*wRate,40*hRate,'#440000','#ffffff','FFT Interpolation Correction Algorithm',20)
mPlotWave1=dr.DRPlotX(win,20*wRate,90*hRate,1000*wRate,200*hRate,'','#113344','#000000','#ffffff','#00eeff','#ffff00',0,1,-1,1,0,0)
mPlotAmp=dr.DRStemX(win,20*wRate,275*hRate,1000*wRate,190*hRate,'','#113344','#000000','#ffffff','#00eeff','#ffff00',30,60,0,1,0,0)
mPlotAmp1=dr.DRStemX(win,20*wRate,450*hRate,1000*wRate,190*hRate,'','#113344','#000000','#ffffff','#00eeff','#ffff00',30,60,0,1,0,0)
dr.DRLabelX(win,660*wRate,40*hRate,140*wRate,40*hRate,'#ddeeee','#000000','Frequency',12)
mDigital1=dr.DRDigital(win,780*wRate,40*hRate,120*wRate,40*hRate,'#000000','#00ffaa',45.5,2,22)
mSpin1=dr.DRSpinBox(win,920*wRate,40*hRate,100*wRate,36*hRate,'#ffffff','#000000',45.5,0.1,40,50)
dr.DRLabelX(win,820*wRate,465*hRate,175*wRate,24*hRate,'#441100','#ffffff','Corrected Spectrum',12) 

#==DataStream Binding=====================
mSpin1.addCallBackSingle(mDigital1.setValueSingle)
mSpin1.addCallBackSingle(myWorking)

myWorking(45.5)

#==Main Loop=====================
win.mainloop()

#==End of APPp=====================

