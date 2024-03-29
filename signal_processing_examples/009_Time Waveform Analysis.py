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
from scipy import signal
from scipy.stats import kurtosis 
import matplotlib.pyplot as plt
import numpy as np
import drvi.drviDSP as dsp
import drvi.drviControlls as dr

#=========================================
def setValueTimer(v):
 pha=v*0.01*10
 mSignal.setSignalPha(pha)

def setValue2D(t,x):
 Fs=1/(t[1]-t[0]);
 N=len(x)
 mPlotWave.setValue2D(t,x)
 T=dsp.findPeriod(Fs,N,x)
 if T==0: s='Fre: ----'
 if T>0:  s='Fre:'+format(1/T,'.2f')
 mTxt.setValueString(s)
 pp=np.max(x)-np.min(x)
 s='P-P:'+format(pp,'.2f')
 mTxt1.setValueString(s)
 R=np.sqrt(np.mean(x**2))
 R=np.sqrt(np.sum(x**2)/N)
 s='RMS:'+format(R,'.2f')
 mTxt2.setValueString(s)
 std=np.std(x)
 s='STD:'+format(std,'.2f')
 mTxt3.setValueString(s) 
 M=np.mean(x)
 s='AVE:'+format(M,'.2f')
 mTxt4.setValueString(s)
 kk=(np.sum(x**4)/N)/pow(R,4)
 s='Kur:'+format(kk,'.2f')
 mTxt5.setValueString(s)  
 
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
win.wm_title('Time Waveform Analysis')

#==Layout of controls=====================
mTimer1=dr.DRTimer(win,200*wRate,30*hRate,120*wRate,36*hRate,'#000000','#ffffff',100)
mLab1=dr.DRLabelX(win,20*wRate,30*hRate,400*wRate,40*hRate,'#003355','#ffffff','Time Waveform Analysis',20)
mPlotWave=dr.DRPlotX(win,20*wRate,80*hRate,900*wRate,520*hRate,'','#003355','#000000','#ffffff','#00eeff','#ffff00',0,0.05,-1,1,0,0)
mLab1=dr.DRLabelX(win,20*wRate,590*hRate,900*wRate,50*hRate,'#003355','#ffffff','',20)
mVButType=dr.DRRadioButX(win,940*wRate,80*hRate,140*wRate,140*hRate,'#004466','#000000','#ffffff','#00ccff','#eeee44','Sine Wave,Square Wave,Triangle Wave,White Noise',11,4,0)
mKnobA=dr.DRKnob(win,930*wRate,280*hRate,130*wRate,130*hRate,'#004466','#222222','#aaaaaa','0,1',0,1,0.5)
mKnobFre=dr.DRKnob(win,930*wRate,400*hRate,130*wRate,130*hRate,'#004466','#222222','#aaaaaa','1,1000',1,1000,50)
mSwitch1=dr.DRSwitch(win,960*wRate,600*hRate,80*wRate,36*hRate,'#004466','#aaddee')
mTxt=dr.DRLabelX(win,60*wRate,595*hRate,130*wRate,30*hRate,'#000000','#00ffaa','0',14)
mTxt1=dr.DRLabelX(win,200*wRate,595*hRate,130*wRate,30*hRate,'#000000','#00ffaa','0',14)
mTxt2=dr.DRLabelX(win,350*wRate,595*hRate,130*wRate,30*hRate,'#000000','#00ffaa','0',14)
mTxt3=dr.DRLabelX(win,490*wRate,595*hRate,130*wRate,30*hRate,'#000000','#00ffaa','0',14)
mTxt4=dr.DRLabelX(win,630*wRate,595*hRate,130*wRate,30*hRate,'#000000','#00ffaa','0',14)
mTxt5=dr.DRLabelX(win,770*wRate,595*hRate,130*wRate,30*hRate,'#000000','#00ffaa','0',14)
#=================================================================
mType=0; Fs=44100; N=4096; A=0.6; Fre=100; Pha=0
mSignal=dsp.DRGenerator(mType,Fs,N,A,Fre,Pha)

#==DataStream Binding=====================
mTimer1.addCallBackSingle(setValueTimer)
mSwitch1.addCallBackSingle(mTimer1.setValueSingle)
mSignal.addCallBackValue2D(setValue2D)
mVButType.addCallBackSingle(mSignal.setSignalType)
mKnobA.addCallBackSingle(mSignal.setSignalAmp)
mKnobFre.addCallBackSingle(mSignal.setSignalFre)

setValueTimer(0)
    
#==Main Loop=====================
win.mainloop()

#==End of APPp=====================

