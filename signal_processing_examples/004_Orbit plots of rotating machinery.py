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
import drvi.drviSimpleAudio as sa
 
#==CallBack Function==============
def myWorking(v):
 A1=mK1.getValueSingle()
 Q1=mK2.getValueSingle()
 A2=mK3.getValueSingle()
 Q2=mK4.getValueSingle()
 A3=mK5.getValueSingle()
 Q3=mK6.getValueSingle()
 A4=mK7.getValueSingle()
 Q4=mK8.getValueSingle()
 Fs=44100;
 dt=1.0/Fs;
 N=500;
 tData=np.arange(N)*dt
 x11=A1*np.sin(2*np.pi*800*tData+Q1*np.pi/180)
 x12=A2*np.sin(2*np.pi*2*800*tData+Q2*np.pi/180)
 x=x11+x12
 mPlotWave1.setValue2D(tData,x)
 y11=A3*np.sin(2*np.pi*800*tData+Q3*np.pi/180)
 y12=A4*np.sin(2*np.pi*2*800*tData+Q4*np.pi/180)
 y=y11+y12
 mPlotWave2.setValue2D(tData,y)
 mPlotOrbit.setValue2D(x,y)
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
win.wm_title('Orbit plots of rotating machinery')

#==Layout of controls=====================
mInfo1=dr.DRInfo(win,460*wRate,20*hRate,40*wRate,40*hRate,'#00bbbb','#000000','#ffffff','DRPython.pdf')
dr.DRLabelX(win,20*wRate,20*hRate,420*wRate,40*hRate,'#440000','#ffffff','Orbit Analysis',20)
mPlotWave1=dr.DRPlotX(win,20*wRate,70*hRate,520*wRate,230*hRate,'','#002f5e','#000000','#ffffff','#00eeff','#ffff00',0,0.01,-1,1,0,0)
mPlotWave2=dr.DRPlotX(win,20*wRate,290*hRate,520*wRate,230*hRate,'','#002f5e','#000000','#ffffff','#00eeff','#ffff00',0,0.01,-1,1,0,0)
mPlotOrbit=dr.DRPlotX(win,540*wRate,70*hRate,520*wRate,450*hRate,'','#002f5e','#000000','#ffffff','#00eeff','#ffff00',-1,1,-1,1,0,0)
mK1=dr.DRKnob(win,40*wRate,525*hRate,120*wRate,120*hRate,'#004466','#222222','#aaaaaa','0,1',0,1,0.5)
mK2=dr.DRKnob(win,150*wRate,525*hRate,120*wRate,120*hRate,'#006644','#222222','#aaaaaa','0,180',0,180,0)
mK3=dr.DRKnob(win,260*wRate,525*hRate,120*wRate,120*hRate,'#004466','#222222','#aaaaaa','0,1',0,1,0.3)
mK4=dr.DRKnob(win,370*wRate,525*hRate,120*wRate,120*hRate,'#006644','#222222','#aaaaaa','0,180',0,180,0)
mK5=dr.DRKnob(win,590*wRate,525*hRate,120*wRate,120*hRate,'#004466','#222222','#aaaaaa','0,1',0,1,0.2)
mK6=dr.DRKnob(win,700*wRate,525*hRate,120*wRate,120*hRate,'#006644','#222222','#aaaaaa','0,180',0,180,45)
mK7=dr.DRKnob(win,810*wRate,525*hRate,120*wRate,120*hRate,'#004466','#222222','#aaaaaa','0,1',0,1,0.5)
mK8=dr.DRKnob(win,920*wRate,525*hRate,120*wRate,120*hRate,'#006644','#222222','#aaaaaa','0,180',0,180,0)

#==Binding==================================================
mK1.addCallBackSingle(myWorking)
mK2.addCallBackSingle(myWorking)
mK3.addCallBackSingle(myWorking)
mK4.addCallBackSingle(myWorking)
mK5.addCallBackSingle(myWorking)
mK6.addCallBackSingle(myWorking)
mK7.addCallBackSingle(myWorking)
mK8.addCallBackSingle(myWorking)

myWorking(0)

#==Main Loop=====================

win.mainloop()

#==End of APPp=====================

