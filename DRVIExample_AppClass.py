"""
# DRPython
# Copyright (C) 2022
# Author: Lingsong HE
# Organization: Huazhong University of Science and Technology
# Contact: helingsong@hust.edu.cn
                                                       :::.                               
  .+++++++=-:   +++++++=-  -+++++++-.            .:-.  +++-                               
  .+++---=+++=  +++-:-+++= -+++-:-+++:...   .....+++:. +++-.::.     .:::.    .....::.     
  .+++.   :+++: +++-.:+++- -+++. .+++=+++.  ++++++++++.++++++++=  :+++++++-..++++++++=    
  .+++.   .+++: +++++++=:  -++++++++: :++= -++-..+++:. +++=..+++.:+++:..+++=.+++-.:+++.   
  .+++.  .=+++  +++-.=++=. -+++-::.    -++=++-   +++:  +++-  +++:-++=   ++++.+++:  +++.   
  .+++==++++=.  +++:  =+++.-+++.        =+++=    +++== +++-  +++:.=++=-=+++:.+++:  +++.   
  .------::     ---.   ----:---.        :+++.    .-==- ---:  ---.  .--=--:   ---.  ---.   
                                     .==+++:                                              
                                     .---:
                                                                                          
                            %                                                             
                            **          :==.                                              
                             *.        +@@@@@*                                            
                              +        :@@@@=                                             
                               +        *#@@=                                             
                               :=       .%@@@-                                            
                                =.      #@@@@@:                                           
                                 +     #@@@@@@+                                           
                                  +   %@*@@@@@#                                           
                                  :++@%:%@@@@#@.                                          
                                :*%#=   %@@@@=@=                 .-=-.                    
                *      .:-::=*#@#:  -   %@@@@%%*     ..:.   ..-+%@%%@@                    
              :%@#++%@@@@@@@@@@@@@+::#*%@@@@@= ::-+%@@@@@%@@@%*=:   +*                    
             *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@%*+   .%-       .            
           -%@@@@@@%@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-  +@%:   :-**=-          
          =@@@@@@+.-%:@:%@-+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. +@@@@@@%%%###:         
        :#@@@#+=:.  : .:=- :@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@-  :+*##*=--**%+         
        @@@%-...           .+@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@             *#*:        
        -=:                 -@@@@@@@%-=++##*+=-.  +#@@@@@%@@%@@@@-           =#=-         
                         #@%#@@@@%%@@-    +         .*@@@=-@@@@@@@*:                      
                       :#=.  .@@@#.:@@*   .=          :@@=  :-=+#@@@%+-                   
                     :#%.  :=#@@%*+=-:     -:          %@@=        :%@#                   
                     +@=   .  +@=           *         :@#-           =@-                  
                   *+%@#-:::.:=@*-==:.       +       =@=...:::::::-:::+@.. 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                     
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

#===Start APP Class==========================================================================
class myAPPClass:
    def start(self,wRate,hRate):
        self.tMain=tk.Frame(self.win,bg=win.cget('bg'))
        self.tMain.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        self.innerOpen(self.tMain,wRate,hRate);
            
    def startAlone(self,w,h,bgc,title):
        self.tMain=tk.Toplevel(bg=bgc);
        self.tMain.title(title);
        s=str(w)+'x'+str(h);
        self.tMain.geometry(s)
        self.innerOpen(self.tMain);
        self.tMain.mainloop()

    def destroy(self):
        self.tMain.destroy();

    def __init__(self,win):
        self.win=win
        self.tMain=0
        #your var=====
        self.Fs=1000
        self.N=8192
        
    #==Your App GUI Layout====
    def innerOpen(self,win,wRate,hRate):
        self.txt=dr.DRLabelX(win,20*wRate,25*hRate,500*wRate,40*hRate,'#440000','#ffffff','APP Class Sample',20)
        self.mPlotWave=dr.DRPlotX(win,20*wRate,70*hRate,900*wRate,260*hRate,'','#113344','#000000','#ffffff','#00eeff','#ffff00',0,1,-1,1,0,0)
        self.mPlotAmp=dr.DRPlotX(win,20*wRate,280*hRate,900*wRate,260*hRate,'','#113344','#000000','#ffffff','#00eeff','#ffff00',0,120,0,1,0,0)
        self.mKnobA=dr.DRGKnob(win,930*wRate,100*hRate,150*wRate,150*hRate,'#001122','#226688','#222222','#aaaaaa','0,100',0,100,5)
        self.txt3=dr.DRLabelX(win,930*wRate,360*hRate,140*wRate,30*hRate,'#ddeeee','#000000','Frequency：',14)
        self.mDigital1=dr.DRDigital(win,940*wRate,400*hRate,120*wRate,40*hRate,'#000000','#00ffaa',5,2,22)
        self.mKnobA.addCallBackSingle(self.mDigital1.setValueSingle)
        self.mKnobA.addCallBackSingle(self.myWorking)
        self.myWorking(5)

    #==Any Your App function=======
    def myWorking(self,v):
        Fre=v
        dt=1.0/self.Fs;
        t=np.arange(self.N)*dt
        x=0.8*np.sin(2*np.pi*Fre*t)
        [mFre,mAmp]=dsp.AmpSpetrumX(self.N,self.Fs,x)
        self.mPlotWave.setValue2D(t,x)
        self.mPlotAmp.setValue2D(mFre,mAmp)

    def setValueSingle(self,v):
        print(v)

    def setValueString(self,txt):
        print(txt)

#====End of APP Class=============================================================

#==Main Program to test App Class==========================================================    
def mExit():
    win.destroy()
    return 1

def mAbout():
    k=msgbox.askyesno('About','This is a APP Class frame exportd by DRPython !')
    return 1

#=Insert a APP class in main window===
def mAppClass():
    global myAPP1,appst,wRate,hRate;
    if appst==1: return
    myAPP1.start(wRate,hRate);
    appst=1;

#=Delete the APP Class===
def delAppClass():
    global myAPP1,appst;
    if appst==0: return
    myAPP1.destroy();
    appst=0

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
win.wm_title('APP Class Sample')

#==MenuBar========================
menubar=tk.Menu(win)
fmenu=tk.Menu(menubar,tearoff=False)
fmenu.add_command(label="About",command=mAbout)
fmenu.add_command(label="Start App Class",command=mAppClass)
fmenu.add_command(label="Del App Class",command=delAppClass)
fmenu.add_command(label="Close",command=mExit)
menubar.add_cascade(label="File",menu=fmenu)
win.config(menu=menubar)

#==ToolBar条===========================================
tbar=tk.Frame(win)
tbar.pack(side=tk.TOP,fill=tk.X)
bt1=tk.Button(tbar,text='Start App Class',command=mAppClass)
bt1.pack(side=tk.LEFT)
bt1=tk.Button(tbar,text='Del App Class',command=delAppClass)
bt1.pack(side=tk.LEFT)

#==init APP Class================
appst=0;
myAPP1=myAPPClass(win);

#==Main Loop=====================
win.mainloop()

#==End of Main Program===========================================================

