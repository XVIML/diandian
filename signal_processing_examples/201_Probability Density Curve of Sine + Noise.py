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

def myWorking():
    global A,A1,Fre,pha
    Fs=44100;
    N=8192;
    dt=1.0/Fs;
    t=np.arange(N)*dt
    x=A*np.sin(2*np.pi*Fre*t+pha*np.pi/180)
    x1=0.3333*A1*np.random.randn(N)
    x=x+x1    
    M=64
    abin=np.linspace(-1.5,1.5,num=M)
    [mHist,bins]=np.histogram(x,bins=abin)
    mPdf=mHist/N
    mPlotWave.setValue2D(t,x)
    mPlotPDF.setValue2D(abin[0:M-1],mPdf)  

def setValue(v):
    global A,A1,Fre,pha
    global mKnobA,mKnobFre,mKnobA1
    A=mKnobA.getValueSingle()
    Fre=mKnobFre.getValueSingle()
    A1=mKnobA1.getValueSingle()
    myWorking()
 
def setValueTimer(v):
    global A,A1,Fre,pha
    pha=v*0.01*10
    myWorking()    

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
win.wm_title('Probability Density Curve of Sine + Noise')


#==Layout of controls=====================
mTimer1=dr.DRTimer(win,200*wRate,30*hRate,120*wRate,36*hRate,'#000000','#ffffff',100)
mLab1=dr.DRLabelX(win,20*wRate,30*hRate,600*wRate,40*hRate,'#003355','#ffffff','Probability Density Curve of Sine + Noise',20)
mPlotWave=dr.DRPlotX(win,20*wRate,80*hRate,900*wRate,280*hRate,'','#003355','#000000','#ffffff','#00eeff','#ffff00',0,0.05,0,0,0,0)
mPlotPDF=dr.DRPlotX(win,20*wRate,350*hRate,900*wRate,280*hRate,'','#003355','#000000','#ffffff','#00eeff','#ffff00',0,0,0,0,0,0)

mKnobA=dr.DRGKnob(win,930*wRate,80*hRate,130*wRate,130*hRate,'#001133','#0088aa','#222222','#aaaaaa','0,1',0,1,0.5)
mKnobFre=dr.DRGKnob(win,930*wRate,210*hRate,130*wRate,130*hRate,'#001133','#0088aa','#222222','#aaaaaa','1,1000',1,1000,50)
mKnobA1=dr.DRGKnob(win,930*wRate,360*hRate,130*wRate,130*hRate,'#002211','008844','#222222','#aaaaaa','0,1',0,1,0.5)

mSwitch1=dr.DRSwitch(win,960*wRate,580*hRate,80*wRate,36*hRate,'#002266','#aaddee')

#==DataStream Binding=====================
mTimer1.addCallBackSingle(setValueTimer)
mSwitch1.addCallBackSingle(mTimer1.setValueSingle)
mKnobA.addCallBackSingle(setValue)
mKnobFre.addCallBackSingle(setValue)
mKnobA1.addCallBackSingle(setValue)

A=0.5
Fre=50
A1=0.5
pha=0;

setValueTimer(0)

#==Main Loop=====================
win.mainloop()

#==End of APPp=====================
