#===This Frame is generated by DRPython ===============================
import sys
import os
import drvi.drviAppendPath as mPath
mPath.appendPythonPath()
#=================================================

import tkinter as tk
import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import numpy as np
import drvi.drviDSP as dsp
import drvi.drviControlls as dr
import drvi.drviSimpleAudio as ply

#=========================================
def setValue2DX(dx,x):
 CH=x.ndim
 if CH==2:x=x[:,0] #立体声，取一通道数据
 mPlotF.setValue2DX(dx,x)
 mFs=1/dx
 mLen=len(x)
 [mFre,mAmp]=dsp.AmpSpetrum(mLen,mFs,x)
 df=mFs/mLen
 mPlot1F.setValue2DX(df,mAmp)

        
#==Main Window=====================
winDir=os.getcwd()
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
win.wm_title('WAV文件放音样例程序')

#==Layout of controls=====================
mInfo1=dr.DRInfo(win,440*wRate,30*hRate,40*wRate,40*hRate,'#00bbbb','#000000','#ffffff','DRPython.pdf')
mLab1=dr.DRLabelX(win,20*wRate,30*hRate,400*wRate,40*hRate,'#445577','#ffffff','WAV文件放音样例程序',20)
dr.DRLabelX(win,20*wRate,80*hRate,1020*wRate,570*hRate,'#003355','#ffffff','',20)
mHBut2=dr.DRHButtonGroup(win,690*wRate,30*hRate,200*wRate,36*hRate,'#006688','#ffffff','播放,停止',2,0)
pp=winDir+"\\ffmpeg511"
mPlay=ply.DRPlayX(win,920*wRate,30*hRate,120*wRate,36*hRate,'#002244','#ffffff',pp)
mPlotF=dr.DRPlotFast(win,30*wRate,90*hRate,1000*wRate,280*hRate,'#003355','#000000','#ffffff','#006677','#ffff00',12,0,0.2,-1,1,0,0)
mPlot1F=dr.DRPlotFast(win,30*wRate,365*hRate,1000*wRate,280*hRate,'#003355','#000000','#ffffff','#006677','#ffff00',12,0,6000,0,0.25,0,0)
#====================================
mHBut2.addCallBackSingle(mPlay.setValueSingle)
mPlay.addCallBack2DX(setValue2DX)

#==Main Loop=====================
win.mainloop()

#==End of APPp=====================

