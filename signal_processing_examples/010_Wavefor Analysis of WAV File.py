"""
#=====This Frame is generated by DRPython ===================================================#
#                                                                                            #
#                                                         :::.                               #
#    .+++++++=-:   +++++++=-  -+++++++-.            .:-.  +++-                               #
#    .+++---=+++=  +++-:-+++= -+++-:-+++:...   .....+++:. +++-.::.     .:::.    .....::.     #
#    .+++.   :+++: +++-.:+++- -+++. .+++=+++.  ++++++++++.++++++++=  :+++++++-..++++++++=    #
#    .+++.   .+++: +++++++=:  -++++++++: :++= -++-..+++:. +++=..+++.:+++:..+++=.+++-.:+++.   #
#    .+++.  .=+++  +++-.=++=. -+++-::.    -++=++-   +++:  +++-  +++:-++=   ++++.+++:  +++.   #
#    .+++==++++=.  +++:  =+++.-+++.        =+++=    +++== +++-  +++:.=++=-=+++:.+++:  +++.   #
#    .------::     ---.   ----:---.        :+++.    .-==- ---:  ---.  .--=--:   ---.  ---.   #
#                                       .==+++:                                              #
#                                       .---:                                                #
#                                                                                            #
#============================================================================================#
"""
#Add current Python working path, remove it, if you original python is ok.
import drvi.drviAppendPath as mPath
mPath.appendPythonPath()
#====================================================================

import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import filedialog
from tkinter import colorchooser
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
from pylab import mpl
from matplotlib import cm
import numpy as np
import drvi.drviDSP as dsp
import drvi.drviControlls as dr
import drvi.drviSimpleAudio as sa


#==Event response function of controls====
def setValueSingle(v):
    global Fs,N,CH,data
    mfile=filedialog.askopenfilename(title="Select File",filetypes=(("WAV files", "*.wav"),("all files", "*.*")))
    if not mfile: return 1
    [Fs,N,CH,data]=sa.readWavFile(mfile)
    if CH==2:data=data[:,0] #Stero, use channel one
    mPlotWave.setValue2DX(1/Fs,data)
    myWorking()

def setLength(v):
    global mLength
    if v==0: mLength=1024
    if v==1: mLength=2048
    if v==2: mLength=4096
    if v==3: mLength=8192
    if v==4: mLength=16384
    if v==5: mLength=32768
    if v==6: mLength=64535
    myWorking()
    
def setPos(v):
    global mPosition
    mPosition=v
    myWorking()

def setMove(v):
    global N,mLength,mPosition,mHSlider1
    if N==0: return;
    if v==201: d=-mLength/6
    if v==202: d=mLength/6
    d=100*d/N
    mPosition=mPosition+d
    if mPosition<0: mPosition=0
    if mPosition>100: mPosition=100
    mHSlider1.setValueSingle(mPosition)
    myWorking()

def myWorking():
    global Fs,N,CH,data,xdata,mPosition,mLength
    if N==0: return;
    K=int(mPosition*0.01*N)
    if K<0: K=0    
    xdata=data[K:K+mLength]
    mPlotWave1.setValue2DX(1/Fs,xdata)

def setPlay(v):
    global Fs,N,CH,data,mPosition,mLength
    if N==0: return;
    sa.play(CH,Fs,data,0) 

def setAmplify(v):
    global Fs,N,CH,data,xdata,mPosition,mLength
    s='0.0 Hz'
    T=dsp.findPeriod(Fs,len(xdata),xdata)
    if T>0: s=format(1/T,'.2f')+' Hz'
    mTxt1.setValueString(s)
        

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
win.wm_title('Waveform Analysis of WAV File')

#==Layout of controls=====================
mInfo1=dr.DRInfo(win,540*wRate,25*hRate,40*wRate,40*hRate,'#00bbbb','#000000','#ffffff','DRPython.pdf')
dr.DRLabelX(win,20*wRate,25*hRate,500*wRate,40*hRate,'#440000','#ffffff','Waveform Analysis of WAV',20)
mBut1=dr.DRButton(win,20*wRate,80*hRate,100*wRate,36*hRate,'#003355','#eeee00','Open',101)
mPlotWave=dr.DRPlotX(win,20*wRate,130*hRate,1060*wRate,260*hRate,'','#113344','#000000','#ffffff','#00eeff','#ffff00',0,0,-1,1,0,0)
mPlotWave1=dr.DRPlotX(win,20*wRate,380*hRate,1060*wRate,260*hRate,'','#113344','#000000','#ffffff','#00eeff','#ffff00',0,0,-1,1,0,0)
mOMenu1=dr.DROptionMenu(win,130*wRate,80*hRate,100*wRate,36*hRate,'#003355','#eeee00','1024,2048,4096,8192,16384,32768,64535',3)
mHSlider1=dr.DRHSlider(win,310*wRate,82*hRate,590*wRate,30*hRate,'#444444','#004466','#008822',8,20,0,100,0)
mBut2=dr.DRButton(win,270*wRate,86*hRate,30*wRate,24*hRate,'#003355','#eeee00','<<',201)
mBut3=dr.DRButton(win,900*wRate,86*hRate,30*wRate,24*hRate,'#003355','#eeee00','>>',202)
mBut4=dr.DRButton(win,970*wRate,80*hRate,100*wRate,36*hRate,'#005533','#eeee00','Play',101)
mBut9=dr.DRButton(win,930*wRate,370*hRate,100*wRate,26*hRate,'#005533','#ffffff','Calculate',400)
mTxt1=dr.DRLabelX(win,860*wRate,410*hRate,180*wRate,30*hRate,'#000000','#00ffaa','0.0 Hz',14)

mOMenu1.addCallBackSingle(setLength)
mBut1.addCallBackSingle(setValueSingle)
mHSlider1.addCallBackSingle(setPos)
mBut2.addCallBackSingle(setMove)
mBut3.addCallBackSingle(setMove)
mBut4.addCallBackSingle(setPlay)
mBut9.addCallBackSingle(setAmplify);

#==========================================
mPosition=0
mLength=8192
Fs=0
N=0
CH=0
data=0
xdata=0

#==Main Loop=====================
win.mainloop()

#==End of APPp=====================
