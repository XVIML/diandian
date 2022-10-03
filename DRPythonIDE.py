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
          
import os
import sys
import os.path

idlelib_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if idlelib_dir not in sys.path: sys.path.insert(0, idlelib_dir)
from idlelib import editor
from idlelib.pyshell import main as IDLE

import drvi.drviAppendPath as mPath
mPath.appendPythonPath()
    
#==========================================================================
import threading
from decimal import Decimal
import re
import os
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import math
import base64 
from tkinter import colorchooser
import tkinter.messagebox as msgbox
from tkinter import filedialog
import numpy as np
import subprocess
import drvi.drviControlls as dr
import drvi.drviDSP as dsp
import drvi.drviCodeGenerator as code
from drvi import drColorWin as colorWin
#import webbrowser as web
import drvi.DRhtml as web1
import drvi.drffmpeg as mPlayer
import serial.tools.list_ports

#==========================================================
def insertIcon(win,data,txt,fun):
 img = tk.PhotoImage(file=data)
 L=tk.Label(win,image=img)
 L.pack(side=tk.LEFT) 
 L.bind('<Button-1>',fun)
 L.bind('<Motion>',fun)
 L_ttp = dr.ToolTip(L,txt)
 return L,img

def listCOM():
    listCOM=list(serial.tools.list_ports.comports())
    S=''
    for i in range(0,len(listCOM)):
        S=S+listCOM[i][0]+'  :  '+listCOM[i][1]+'\n'
    k=msgbox.askyesno('COM List',S)


def mp3ToWav():
    global winDir
    mfile=filedialog.askopenfilename(title="Select Files",filetypes=(("mp3 files", "*.mp3"),("all files", "*.*")))
    if not mfile: return 1
    mfile1=mfile.replace('.mp3','.wav');    
    fPath=winDir+'\\ffmpeg511'
    abc=mPlayer.DRffmpeg(fPath)
    abc.getWavFile(mfile,mfile1)    

def mp4ToWav():
    global winDir
    mfile=filedialog.askopenfilename(title="Select Files",filetypes=(("mp4 files", "*.mp4"),("all files", "*.*")))
    if not mfile: return 1
    mfile1=mfile.replace('.mp4','.wav');    
    fPath=winDir+'\\ffmpeg511'
    abc=mPlayer.DRffmpeg(fPath)
    abc.getWavFile(mfile,mfile1)    

def mp4Play():
    global winDir
    mfile=filedialog.askopenfilename(title="Select Files",filetypes=(("mp4 files", "*.mp4"),("all files", "*.*")))
    if not mfile: return 1
    fPath=winDir+'\\ffmpeg511'
    abc=mPlayer.DRffmpeg(fPath)
    abc.playVideoX(mfile,480,320,0)

def mp3Play():
    global winDir
    mfile=filedialog.askopenfilename(title="Select Files",filetypes=(("mp3 files", "*.mp3"),("all files", "*.*")))
    if not mfile: return 1
    fPath=winDir+'\\ffmpeg511'
    abc=mPlayer.DRffmpeg(fPath)
    abc.playVideoX(mfile,480,320,0)
    
#======================================================================     
def gettvID(event):
    global mFirst,tvItem; 
    mFirst=mFirst+1; #DEL LOGO
    ss=tvItem.item(event.widget.selection(),'text')
    if ss=='Button':  setInsertControlls(1) 
    if ss=='HBGroup': setInsertControlls(101)
    if ss=='VBGroup': setInsertControlls(102)    
    if ss=='Label':   setInsertControlls(2)    
    if ss=='Entry':   setInsertControlls(3)
    if ss=='HScale':  setInsertControlls(4)    
    if ss=='VScale':  setInsertControlls(5)
    if ss=='RadioBut':setInsertControlls(6)
    if ss=='CheckBut':setInsertControlls(7)    
    if ss=='ListBox': setInsertControlls(8)
    if ss=='Combobox':   setInsertControlls(9)    
    if ss=='OptionMenu': setInsertControlls(14) 
    if ss=='Text':       setInsertControlls(10)     
    if ss=='SpinBox':  setInsertControlls(11) 
    if ss=='Progress': setInsertControlls(13) 
    if ss=='Switch':   setInsertControlls(35) 
    if ss=='Knob':     setInsertControlls(30)     
    if ss=='HSlider': setInsertControlls(32)
    if ss=='VSlider': setInsertControlls(33)
    if ss=='GButton': setInsertControlls(41)
        
    if ss=='Plot':      setInsertControlls(51)
    if ss=='Stem':      setInsertControlls(59)
    if ss=='SemilogX':  setInsertControlls(60)
    if ss=='SemilogY':  setInsertControlls(61)
    if ss=='LogLog':    setInsertControlls(62)
    if ss=='PlotBar':   setInsertControlls(52)
    if ss=='PlotPie':   setInsertControlls(53)
    if ss=='PlotPolar': setInsertControlls(56)
    if ss=='Plot3D':    setInsertControlls(54)
    if ss=='PlotSurf':  setInsertControlls(55)    
    if ss=='PlotContour':setInsertControlls(57)
    if ss=='PlotFast':   setInsertControlls(58)
    
    if ss=='Ruler':  setInsertControlls(31) 
    if ss=='HRuler': setInsertControlls(40) 
    if ss=='Gauge':  setInsertControlls(34) 
    if ss=='Digital':setInsertControlls(36) 
    if ss=='Lamp':   setInsertControlls(39) 
    if ss=='Tab':    setInsertControlls(37) 
    if ss=='Info':   setInsertControlls(38) 
    if ss=='IconButton': setInsertControlls(12) 
    
    if ss=='List':     setInsertControlls(42) 
    if ss=='Timer':    setInsertControlls(70) 
    if ss=='Recorder': setInsertControlls(71) 
    if ss=='Play':     setInsertControlls(72) 
    if ss=='ArduinoAD':setInsertControlls(73) 
    if ss=='TCPS':  setInsertControlls(74) 
    if ss=='UDPS':  setInsertControlls(75) 
    if ss=='UDPBS': setInsertControlls(76)
    if ss=='PlayX': setInsertControlls(77)     
    return 1


#帮助文件===============================
def tvmouseRightUP(event):
 global controlType,winDir
 s=''
 x=event.x;
 if x<0: return
 if controlType==1:  s='Button'  
 if controlType==101:s='HBGr' 
 if controlType==102:s='VBGr' 
 if controlType==2:  s='Label' 
 if controlType==3:  s='Entry' 
 if controlType==4:  s='HScale' 
 if controlType==5:  s='VScale' 
 if controlType==6:  s='RadioBut' 
 if controlType==7:  s='CheckBut' 
 if controlType==8:  s='ListBox' 
 if controlType==9:  s='ComboBox' 
 if controlType==10: s='Text' 
 if controlType==11: s='SpinBox' 
 if controlType==12: s='IconButton' 
 if controlType==13: s='Progress' 
 if controlType==14: s='OMenu' 
 if controlType==30: s='Knob' 
 if controlType==31: s='Ruler' 
 if controlType==32: s='HSlide' 
 if controlType==33: s='VSlide' 
 if controlType==34: s='Gauge' 
 if controlType==35: s='Switch' 
 if controlType==36: s='Digital' 
 if controlType==37: s='Tab' 
 if controlType==38: s='Info' 
 if controlType==39: s='Lamp' 
 if controlType==40: s='HRuler' 
 if controlType==41: s='GButton' 
 if controlType==42: s='List' 
 if controlType==51: s='Plot' 
 if controlType==52: s='PlotBar' 
 if controlType==53: s='PlotPie' 
 if controlType==54: s='Plot3D' 
 if controlType==55: s='PlotSurf' 
 if controlType==56: s='PlotPolar' 
 if controlType==57: s='PlotContour' 
 if controlType==58: s='PlotFast' 
 if controlType==59: s='Stem' 
 if controlType==60: s='SemilogX' 
 if controlType==61: s='SemilogY' 
 if controlType==62: s='LogLog' 
 if controlType==70: s='Timer' 
 if controlType==71: s='Recorder' 
 if controlType==72: s='Play'
 if controlType==73: s='Arduino'
 if controlType==74: s='TCPS' 
 if controlType==75: s='UDPS'
 if controlType==76: s='UDPBS'
 if controlType==77: s='PlayX' 
 path=winDir+'\\html'
 name=s+'.html'
 fpath=path+'\\'+name
 st=os.path.exists(fpath)
 if st==False: name='working.html'
 #npath=path+"\\"+name; web.open(npath, 1)
 web1.htmlBrowser(980,700,path,name)
 return
 
def tvmouseUP(event):
 global currentN,controlN,controlType
 global controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 x=event.x; y=event.y
 if x>0: return
 x=controlWGroup[0]+x-120
 y=y+30
 
 controlN=controlN+1
 w=0; h=0; bg=''; fg=''  
 if controlType==1:
  s='Button'+str(controlN);   w=100; h=40; bg='#00aacc'; fg='#eeee00'  
 if controlType==101:
  s='HBGr'+str(controlN);     w=400; h=36; bg='#000000'; fg='#ffffff'  
 if controlType==102:
  s='VBGr'+str(controlN);     w=100; h=128; bg='#008800'; fg='#ffffff'  
 if controlType==2:
  s='Label'+str(controlN);    w=100; h=30; bg='#bbeeff'; fg='#000000'  
 if controlType==3:
  s='Entry'+str(controlN);    w=100; h=30; bg='#ffffff'; fg='#000000'  
 if controlType==4:
  s='HScale'+str(controlN);   w=200; h=50; bg='#002266'; fg='#000000'  
 if controlType==5:
  s='VScale'+str(controlN);   w=50; h=200; bg='#002266'; fg='#000000'  
 if controlType==6:
  s='RadioBut'+str(controlN); w=120; h=100; bg='#003355'; fg='#ffffff'  
 if controlType==7:
  s='CheckBut'+str(controlN); w=120; h=30; bg='#003355'; fg='#007799'  
 if controlType==8:
  s='ListBox'+str(controlN);  w=140; h=100; bg='#ddffdd'; fg='#000000'  
 if controlType==9:
  s='ComboBox'+str(controlN); w=120; h=30; bg='#0099aa'; fg='#ffffff'  
 if controlType==10:
  s='Text'+str(controlN);     w=120; h=100; bg='#ffffff'; fg='#000000'
 if controlType==11:
  s='SinBox'+str(controlN);   w=120; h=32; bg='#ccffcc'; fg='#000000'
 if controlType==12:
  s='Icon'+str(controlN);     w=60; h=60; bg='#ffffff'; fg='#000000'
 if controlType==13:
  s='Progress'+str(controlN); w=200; h=40; bg='#00dd00'; fg='#000000'
 if controlType==14:
  s='OMenu'+str(controlN);    w=100; h=40; bg='#00aacc'; fg='#eeee00'

 if controlType==30:
  s='Knob'+str(controlN);     w=120; h=120; bg='#004466'; fg='#222222'
 if controlType==31:
  s='Ruler'+str(controlN);    w=110; h=200; bg='#ffffff'; fg='#aaaaaa'
 if controlType==32:
  s='HSlider'+str(controlN);  w=260; h=30; bg='#444444'; fg='#880000'
 if controlType==33:
  s='VSlider'+str(controlN);  w=30; h=260; bg='#444444'; fg='#880000'
 if controlType==34:
  s='Gauge'+str(controlN);    w=160; h=160; bg='#ffffff'; fg='#444444'
 if controlType==35:
  s='Switch'+str(controlN);   w=80; h=36; bg='#004466'; fg='#aaddee'
 if controlType==36:
  s='Digital'+str(controlN);  w=100; h=36; bg='#000000'; fg='#00ffaa'
 if controlType==37:
  s='Tab'+str(controlN);      w=600; h=400; bg='#dddddd'; fg='#888888'
 if controlType==38:
  s='Info'+str(controlN);     w=40; h=40; bg='#00bbbb'; fg='#000000'
 if controlType==39:
  s='Lamp'+str(controlN);     w=60; h=60; bg='#00aa00'; fg='#cccc00'
 if controlType==40:
  s='HRuler'+str(controlN);   w=200; h=80; bg='#eeeeee'; fg='#aaaaaa'
 if controlType==41:
  s='GButton'+str(controlN);  w=100; h=40; bg='#00ccaa'; fg='#eeee00'
 if controlType==42:
  s='List'+str(controlN);     w=300; h=90; bg='#eeeeff'; fg='#000000'

 if controlType==51:
  s='Plot'+str(controlN);        w=700; h=210; bg='#003355'; fg='#000000'
 if controlType==52:
  s='PlotBar'+str(controlN);     w=700; h=210; bg='#003355'; fg='#000000'
 if controlType==53:
  s='PlotPie'+str(controlN);     w=300; h=300; bg='#ffffff'; fg='#000000'
 if controlType==54:
  s='Plot3D'+str(controlN);      w=420; h=380; bg='#ffffff'; fg='#000000'
 if controlType==55:
  s='PlotSurf'+str(controlN);    w=500; h=380; bg='#ffffff'; fg='#000000'
 if controlType==56:
  s='PlotPolar'+str(controlN);   w=300; h=300; bg='#005599'; fg='#ffffff'
 if controlType==57:
  s='PlotContour'+str(controlN); w=640; h=480; bg='#ffffff'; fg='#000000'
 if controlType==58:
  s='FastPlot'+str(controlN);    w=700; h=200; bg='#003355'; fg='#000000'
 if controlType==59:
  s='Stem'+str(controlN);        w=700; h=210; bg='#003355'; fg='#000000'
 if controlType==60:
  s='SemilogX'+str(controlN);    w=700; h=210; bg='#003355'; fg='#000000'
 if controlType==61:
  s='SemilogY'+str(controlN);    w=700; h=210; bg='#003355'; fg='#000000'
 if controlType==62:
  s='LogLog'+str(controlN);      w=700; h=210; bg='#003355'; fg='#000000'  
  
 if controlType==70:
  s='Timer'+str(controlN);    w=100; h=40; bg='#00aacc'; fg='#eeee00'
 if controlType==71:
  s='Recorder'+str(controlN); w=100; h=40; bg='#00aacc'; fg='#eeee00' 
 if controlType==72:
  s='Player'+str(controlN);   w=100; h=40; bg='#00aacc'; fg='#eeee00'
 if controlType==73:
  s='Arduino'+str(controlN);  w=900; h=40; bg='#003355'; fg='#000000'
 if controlType==74:
  s='TCPS'+str(controlN);  w=500; h=40; bg='#003355'; fg='#000000'
 if controlType==75:
  s='UDPS'+str(controlN);  w=500; h=40; bg='#003355'; fg='#000000'
 if controlType==76:
  s='UDPBS'+str(controlN);  w=500; h=40; bg='#003355'; fg='#000000'
 if controlType==77:
  s='PlayerX'+str(controlN);   w=100; h=40; bg='#00aacc'; fg='#eeee00'
 pushControlPar(controlN,controlType,1,s,x,y,w,h,bg,fg); 
 insertDRControlls(controlN);
 controlType=0
 return 1          

#用控件组数据刷新属性窗参数============================
def setProtiesWin(i):
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 global pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8
 S=controlNameGroup[i]; x=controlX0Group[i]; y=controlY0Group[i]; w=controlWGroup[i]; h=controlHGroup[i]; b=controlbgGroup[i]; f=controlfgGroup[i]
 pt2.delete(0,20); pt2.insert(0,S)
 pt3.delete(0,20); pt3.insert(0,str(x))
 pt4.delete(0,20); pt4.insert(0,str(y))
 pt5.delete(0,20); pt5.insert(0,str(w))
 pt6.delete(0,20); pt6.insert(0,str(h))
 pt7.delete(0,20); pt7.insert(0,b)
 pt8.delete(0,20); pt8.insert(0,f)    
 return 1

#===插入尺寸可调整控件=====================================
def posChanged(ID,x,y,w,h):
    global currentN
    N=ID; currentN=ID
    controlX0Group[N]=x; controlY0Group[N]=y;
    controlWGroup[N]=w;  controlHGroup[N]=h
    setProtiesWin(N)
    return 1

def insertControl(win,x0,y0,w,h,cb,cf,data):
 global currentN
 x=dr.DRSize(win,currentN,x0,y0,w,h,cb,cf,data)
 x.addCallBackSize(posChanged)  
 return x

#删除界面上所有的布局控件
def delAllControls():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 global controlN;
 for i in range(1,500):
  C=controlGroup[i]
  if C!=0:
   C.ax.destroy(); controlGroup[i]=0; controlTypeGroup[i]=0
 controlN=0   
 return 1

#将从文本文件读取的内容转换为控件布局
def insertFromFile(S):
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 global controlN;
 S=S.split('\n')
 N=int(S[0])
 if N<2:
  return 1
 #插入控件
 for i in range(0,N):
  controlTypeGroup[i]=int(S[2+i*9])
  controlNameGroup[i]=S[3+i*9]
  controlX0Group[i]=int(S[4+i*9])
  controlY0Group[i]=int(S[5+i*9])
  controlWGroup[i]=int(S[6+i*9])
  controlHGroup[i]=int(S[7+i*9])
  controlbgGroup[i]=S[8+i*9]
  controlfgGroup[i]=S[9+i*9]  
  # 0 是主窗口数据,无控件  
  if i>0: insertDRControlls(i);
 controlN=N; 
 #刷新主窗口
 ss=str(controlWGroup[0])+'x'+str(controlHGroup[0])
 win.geometry(ss)
 win.config(bg=controlbgGroup[0])
 setProtiesWin(0)
 return 1

def initAll():
    global x0Control,y0Control,editStatus,mouseStatus,controlType,currentN,controlN
    global controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
    x0Control=0;   y0Control=0; editStatus=0; mouseStatus=0
    controlType=0; currentN=0;  controlN=0
    controlTypeGroup=[0 for x in range(0,511)]
    controlGroup=[0 for x in range(0,511)]
    controlNameGroup=['A' for x in range(0,511)]
    controlX0Group=[0 for x in range(0,511)]
    controlY0Group=[0 for x in range(0,511)]
    controlWGroup=[0 for x in range(0,511)]
    controlHGroup=[0 for x in range(0,511)]
    controlbgGroup=['0' for x in range(0,511)]
    controlfgGroup=['0' for x in range(0,511)]
    currentN=0; controlTypeGroup[0]=0
    controlGroup[0]=win
    controlNameGroup[0]='Main';
    controlX0Group[0]=0;
    controlY0Group[0]=0;
    controlWGroup[0]=1000;
    controlHGroup[0]=600
    controlbgGroup[0]='#ddeeee'
    controlfgGroup[0]='#000000'    
    return 1;

#新建文件
def tNew(event):
    if event.num==1: mNew();return;
    statusbar.config(text=' Create a New GUI layout')

def mNew():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 [N,S]=code.toScript(controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup)
 if N>1:
  k=msgbox.askyesno('Operation', 'This operation will delete current layput !')
  if k==False:
   return 1
 delAllControls(); initAll(); setProtiesWin(0)
 return 1

#读文件
def tOpen(event):
    if event.num==1: mOpen();return;
    statusbar.config(text=' Open a TXT GUI layout file')
    
def mOpen():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 [N,S]=code.toScript(controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup)
 if N>1:
  k=msgbox.askyesno('Operation', 'This operation will delete current layput !')
  if k==False:
   return 1
 delAllControls(); initAll(); setProtiesWin(0)
 mfile=filedialog.askopenfilename(title="Select file",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
 if not mfile:
  return 1
 text_file = open(mfile,"r",encoding='utf-8')
 S=text_file.read()
 text_file.close()
 insertFromFile(S)
 return 1

#保存文件
def tSave(event):
    if event.num==1: mSave();return;
    statusbar.config(text=' Save GUI layout to a TXT file.')
    
def mSave():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 [N,S]=code.toScript(controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup)
 if N<2:
  return 1 
 mfile=filedialog.asksaveasfile(title="Select file",defaultextension=".txt",initialfile = "Untitled.txt",filetypes=(("txt files", "*.txt"),("all files", "*.*")))
 if not mfile:
  return 1
 text_file = open(mfile.name,"w", encoding="utf-8")
 text_file.write(S)
 text_file.close()    
 return 1

#转化为PY脚本
def tPython(event):
    if event.num==1: mToPython();return;
    statusbar.config(text=' Export GUI to Python codes')

def mToPython():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 global sWidth,sHeight
 [N,S]=code.toPythonScriptNew(sWidth,sHeight,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup)
 if N<2: return 1 
 mfile=filedialog.asksaveasfile(title="Select file",defaultextension=".py",initialfile = "Untitled.py",filetypes=(("Python files", "*.py"),("all files", "*.*"))) 
 if not mfile: return 1
 text_file = open(mfile.name,"w", encoding="utf-8")
 text_file.write(S)
 text_file.close()    
 return 1

def tPython1(event):
    if event.num==1: mToPython1();return;
    statusbar.config(text=' Export a proportional GUI to Python codes')
    
def mToPython1():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 global sWidth,sHeight
 [N,S]=code.toPythonScriptNew1(sWidth,sHeight,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup)
 if N<2: return 1 
 mfile=filedialog.asksaveasfile(title="Select file",defaultextension=".py",initialfile = "Untitled.py",filetypes=(("Python files", "*.py"),("all files", "*.*"))) 
 if not mfile: return 1
 S=S+'#Original Screen Size=========================\n'
 S=S+'#ScreenWidth='+str(sWidth)+'\n'
 S=S+'#ScreenHeight='+str(sHeight)+'\n'
 text_file = open(mfile.name,"w", encoding="utf-8")
 text_file.write(S)
 text_file.close()    
 return 1

def tPythonClass(event):
    if event.num==1: mToPythonClass();return;
    statusbar.config(text=' Export TUI to a Python Class')

def mToPythonClass():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 [N,S]=code.toPythonScriptClass(currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup)
 if N<2: return 1 
 mfile=filedialog.asksaveasfile(title="Select file",defaultextension=".py",initialfile = "Untitled.py",filetypes=(("Python files", "*.py"),("all files", "*.*"))) 
 if not mfile:
  return 1
 text_file = open(mfile.name,"w", encoding="utf-8")
 text_file.write(S)
 text_file.close()    
 return 1


#============================================================
#运行Python或IDLE编辑器
def runBatFile(name1,name2):
 global winDir
 mOrder=name1+' '+name2+'\n'
 abc=mPlayer.runCMD(mOrder)
 abc.start()
 return 1

#启动IDLE调试导出的Python程序
def tEditPython(event):
    if event.num==1: mEditPython();return;
    statusbar.config(text=' Edit Python APP')
    
def mEditPython():
 global winDir
 mfile=filedialog.askopenfilename(title="Select file",filetypes=(("Python files", "*.py"),("all files", "*.*")))
 if not mfile: return 1
 name=winDir+'\\temp.bat'
 mfile='"'+mfile+'"'
 runBatFile(dsp.getIDLEPath(),mfile)
 return 1

#启动IDLE编辑器
def tIDLE(event):
    if event.num==1: mIDLE();return;
    statusbar.config(text=' Command Window')

def mIDLE():
    mfile=""
    runBatFile(dsp.getIDLEPath(),mfile)

#典型代码
def typicalScript(mfile):
 runBatFile(dsp.getPythonPath(),mfile)
 return 1

#典型代码预览
def viewtypicalScript(mfile):
 text_file = open(mfile,"r",encoding='utf-8')
 S=text_file.read()
 text_file.close()
 dr.textWindow('Codes Window',800,600,S)
 return 1

#退出程序
def mExit():
 win.destroy()
 return 1

#关于DRPython
def tAbout(event):
    if event.num==1: mAbout();return;
    statusbar.config(text=' About DRPython')
    
def mAbout():
    global winDir
    path=winDir+'\\html'
    npath=path+"\\"+"about.html"
    #web.open(npath, 1)
    web1.htmlBrowser(980,700,path,"about.html")
    
#在线帮助
def tHelp(event):
    if event.num==1: mHelp();return;
    statusbar.config(text=' Helps')
    
def mHelp():
    global winDir
    path=winDir+'\\html'
    npath=path+"\\"+"drpythonhelp.html"
    #web.open(npath, 1)
    web1.htmlBrowser(980,700,path,"drpythonhelp.html")
    
    
#进入编辑状态，在该状态可以插入新控件
def tEditControl(event):
    if event.num==1: editControl();return;
    statusbar.config(text=' Insert status')

def editControl():
 global editStatus,statusbar1
 editStatus=0
 statusbar1.config(text="____Insert status____")   
 return 1

#进入删除控件状态
def tDelControl(event):
    global currentN
    if event.num==1:
        currentN=0;
        delControl();
        return;
    statusbar.config(text=' Delete status')

def delControl():
 global editStatus,statusbar1
 editStatus=1
 statusbar1.config(text="____Delete status____")   
 return 1

#色彩选择
def tColor(event):
    if event.num==1: selColor();return;
    statusbar.config(text=' Color code Window')
    
def selColor():
 c=colorchooser.askcolor(title ="Choose color")
 if c[0]==None: return 
 statusbar.config(text=' Delected color code : '+c[1]) 
 return 1

#设计预览
def tPreview(event):
    if event.num==1: mPreview(); return;
    statusbar.config(text=' Preview of APP')
    
def mPreview():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 global sWidth,sHeight
 [N,S]=code.toPythonScriptNew(sWidth,sHeight,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup)
 if N<2: return 1
 global winDir
 mfile=winDir+'\\temp.py'
 text_file = open(mfile,"w", encoding="utf-8")
 text_file.write(S)
 text_file.close()
 mfile='"'+mfile+'"'
 runBatFile(dsp.getPythonPath(),mfile)
 return 1

#设计代码预览
def tPreviewCode(event):
    if event.num==1: mPreviewCode();return;
    statusbar.config(text=' Preview of Python code')
    
def mPreviewCode():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 global sWidth,sHeight
 [N,S]=code.toPythonScriptNew(sWidth,sHeight,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup)
 if N<2: return 1
 a=dr.textWindow('代码预览',800,600,S)

#==工具条插入控件回调函数===========================================
def setInsertControlls(k):
 global controlType,statusbar,mFirst,mLogo
 if mFirst>1: mFirst=0; mLogo.ax.destroy() 
 controlType=k
 if k==1:
     statusbar.config(text=' Current Widget : Button')
 if k==101:
     statusbar.config(text=' Current Widget : Horizontal Button Group')
 if k==102:
     statusbar.config(text=' Current Widget : Vertical Button Group')          
 if k==2:
     statusbar.config(text=' Current Widget : Label')
 if k==3:
     statusbar.config(text=' Current Widget : Entry')    
 if k==4:
     statusbar.config(text=' Current Widget : Horizontal Scale')   
 if k==5:
     statusbar.config(text=' Current Widget : Vertical Scale')   
 if k==6:
     statusbar.config(text=' Current Widget : RadioButton')   
 if k==7:
     statusbar.config(text=' Current Widget : CheckButton')   
 if k==8:
     statusbar.config(text=' Current Widget : ListBox')   
 if k==9:
     statusbar.config(text=' Current Widget : ComboBox')   
 if k==10:
     statusbar.config(text=' Current Widget : Text')
 if k==11:
     statusbar.config(text=' Current Widget : SpinBox')
 if k==12:
     statusbar.config(text=' Current Widget : IconButton')
 if k==13:
     statusbar.config(text=' Current Widget : ProgressBar')
 if k==14:
     statusbar.config(text=' Current Widget : OptionMenu')

 if k==30:
     statusbar.config(text=' Current Widget : Knob')
 if k==31:
     statusbar.config(text=' Current Widget : Ruler')
 if k==32:
     statusbar.config(text=' Current Widget : Horizontal Slider')
 if k==33:
     statusbar.config(text=' Current Widget : Vertical Slider')
 if k==34:
     statusbar.config(text=' Current Widget : Gauge')         
 if k==35:
     statusbar.config(text=' Current Widget : Switch')
 if k==36:
     statusbar.config(text=' Current Widget : Digital Meter')
 if k==39:
     statusbar.config(text=' Current Widget : Warning Lamp')       
 if k==37:
     statusbar.config(text=' Current Widget : Tabs')   
 if k==38:
     statusbar.config(text=' Current Widget : Info Button')   
 if k==40:
     statusbar.config(text=' Current Widget : Horizontal Ruler')
 if k==41:
     statusbar.config(text=' Current Widget : Gradient Button')
 if k==42:
     statusbar.config(text=' Current Widget : List')          
          
 if k==51:
     statusbar.config(text=' Current Widget : Plot')
 if k==52:
     statusbar.config(text=' Current Widget : PlotBar')
 if k==53:
     statusbar.config(text=' Current Widget : PlotPie')
 if k==54:
     statusbar.config(text=' Current Widget : Plot3D')     
 if k==55:
     statusbar.config(text=' Current Widget : PlotSurface')
 if k==56:
     statusbar.config(text=' Current Widget : PlotPolar')
 if k==57:
     statusbar.config(text=' Current Widget : PlotContour')
 if k==58:
     statusbar.config(text=' Current Widget : Plot_fast')
 if k==59:
     statusbar.config(text=' Current Widget : Stem')
 if k==60:
     statusbar.config(text=' Current Widget : SemilogX')
 if k==61:
     statusbar.config(text=' Current Widget : SemilogY')
 if k==62:
     statusbar.config(text=' Current Widget : LogLog')     
     
 if k==70:
     statusbar.config(text=' Current Widget : Timer')
 if k==71:
     statusbar.config(text=' Current Widget : Recorder')
 if k==72:
     statusbar.config(text=' Current Widget : Player')
 if k==73:
     statusbar.config(text=' Current Widget : Arduino AD Card')
 if k==74:
     statusbar.config(text=' Current Widget : TCP Server of 4 Channel signals')
 if k==75:
     statusbar.config(text=' Current Widget : UDP Server of 4 Channel signals')
 if k==76:
     statusbar.config(text=' Current Widget : UDP broadcast Server of 4 Channel signals')
 if k==77:
     statusbar.config(text=' Current Widget : MP4 Player')
     
 return 1


#=Toolbar1 CallBack=====================================================

#==通过右侧属性表更改控件函数=================
def insertDRControlls(N):
    global win,statusbar
    global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
    currentN=N
    controlGroup[N]=insertControl(win,controlX0Group[N],controlY0Group[N],controlWGroup[N],controlHGroup[N],controlbgGroup[N],controlfgGroup[N],controlNameGroup[N])
    return

#右侧属性表回调函数
def setControlls(event):
 global win,statusbar
 global pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 statusbar.config(text=' Current Status: Set properties of widget')
 mName=pt2.get()
 mX0=int(pt3.get()); mY0=int(pt4.get())
 mW=int(pt5.get());  mH=int(pt6.get())
 mbg=pt7.get();      mfg=pt8.get()
 N=currentN
 controlNameGroup[N]=mName; controlX0Group[N]=mX0; controlY0Group[N]=mY0; controlWGroup[N]=mW; controlHGroup[N]=mH; controlbgGroup[N]=mbg; controlfgGroup[N]=mfg

 if N==0:
  controlNameGroup[N]='Main'
 if mName=='Main':
  s=str(mW)+'x'+str(mH)
  win.geometry(s)
  win.config(bg=mbg)
  return 1

 controlGroup[N].ax.destroy()
 insertDRControlls(N)
 
 return 1


#=Bind Event CallBack=====================================================

#==保存当前插入的控件参数到控件数组=============
def pushControlPar(N,T,C,S,x,y,w,h,b,f):
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 global pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9
 currentN=N
 controlTypeGroup[N]=T; controlGroup[N]=C; controlNameGroup[N]=S; controlX0Group[N]=x; controlY0Group[N]=y; controlWGroup[N]=w; controlHGroup[N]=h; controlbgGroup[N]=b; controlfgGroup[N]=f
 setProtiesWin(N) 
 return 1

#==主窗口回调函数，控件插入================ 
def clickInsert(event):
 global controlType,statusbar,mouseStatus,editStatus
 global controlN,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
  
 mouseStatus=1
 v=controlType
 x=event.x; y=event.y

 if x>(controlWGroup[0]-140): return;  #控件窗口

 s='  Mouse Position :   '+str(x)+' , '+str(y)
 statusbar.config(text=s)

 #删除状态===================
 if editStatus==1:
     if y<20: return;  #工具条
     if currentN==0: return;  #无控件
     k=msgbox.askyesno('Operation', 'Delete this widget ?')
     if k==True:
         i=currentN;
         controlGroup[i].ax.destroy();
         controlGroup[i]=0;
         controlTypeGroup[i]=0;
         setProtiesWin(0)
         currentN=0;         
     return 1     
 return ;

#主窗口鼠标释放回调函数
def releaseInsert(event):
 global mouseStatus 
 mouseStatus=0
 return 1

#主窗口鼠标拖动改变尺寸大小回调函数
def winResize(event):
 global win,sWidth,sHeight 
 global controlN,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 w=win.winfo_width()
 h=win.winfo_height()
 if (w==controlWGroup[0]) and (h==controlHGroup[0]) : return
 currentN=0; controlWGroup[0]=w; controlHGroup[0]=h;
 setProtiesWin(0)
 
#==GUI Laylout=============================================
winDir=os.getcwd()
sys.path.append(winDir) #添加当前路径到系统目录中
win= tk.Tk()
win.config(bg= "#ddeeee")
win.wm_title('Python APP Designer — DRPython   by Lingsong HE of HUST, China')
sWidth=win.winfo_screenwidth()
sHeight=win.winfo_screenheight()
sWrate=0.7; sHrate=0.7;
wWin=sWidth*sWrate; hWin=sHeight*sHrate
x=(sWidth-wWin)/2; y=(sHeight-hWin)/2
win.geometry("%dx%d+%d+%d" %(wWin,hWin,x,y))

#画网格
for i in range(20):
 vf=tk.Frame(win, bg='#888888',height=2000,width=1)
 vf.place(x=i*100, y=30)
 hf=tk.Frame(win, bg='#888888',height=1,width=4000)
 hf.place(x=0, y=i*100)

#==CallBack Binding======================================== 
#主窗口点击鼠标插入控件
win.bind('<Configure>',winResize)
win.bind('<ButtonPress-1>',clickInsert)
win.bind('<ButtonRelease-1>',releaseInsert)

#==Global Variables========================================
x0Control=0
y0Control=0
editStatus=0
mouseStatus=0
controlType=0
currentN=0
controlN=0
controlTypeGroup=[0 for x in range(0,511)]
controlGroup=[0 for x in range(0,511)]
controlNameGroup=['A' for x in range(0,511)]
controlX0Group=[0 for x in range(0,511)]
controlY0Group=[0 for x in range(0,511)]
controlWGroup=[0 for x in range(0,511)]
controlHGroup=[0 for x in range(0,511)]
controlbgGroup=['0' for x in range(0,511)]
controlfgGroup=['0' for x in range(0,511)]

#主窗口参数===
currentN=0
controlTypeGroup[0]=0
controlGroup[0]=win
controlNameGroup[0]='Main';
controlX0Group[0]=0;
controlY0Group[0]=0;
controlWGroup[0]=wWin;
controlHGroup[0]=hWin;
controlbgGroup[0]='#ddeeee'
controlfgGroup[0]='#000000'

#==菜单条============================================
menubar=tk.Menu(win)
menu1=tk.Menu(menubar,tearoff=False)
menu1.add_command(label="New GUI",command=mNew)
menu1.add_command(label="Open a GUI layout file",command=mOpen)
menu1.add_command(label="Save GUI to a layout file",command=mSave)
menu1.add_separator()
menu1.add_command(label="Export GUI to Python",command=mToPython)
menu1.add_command(label="Export a proportional GUI to Python",command=mToPython1)
menu1.add_command(label="Export GUI to Python Class",command=mToPythonClass)
menu1.add_separator()
menu1.add_command(label="Edit Python APP",command=mEditPython)
menu1.add_separator()
menu1.add_command(label="Python Commond Window",command=mIDLE)
menu1.add_separator()
menu1.add_command(label="Close",command=mExit)
menubar.add_cascade(label="File",menu=menu1)

menu2=tk.Menu(menubar,tearoff=False)
menu2.add_command(label="Insert widgets",command=editControl)
menu2.add_separator()
menu2.add_command(label="Delete widgets",command=delControl)
menu2.add_separator()
menu2.add_command(label="APP Preview",command=mPreview)
menu2.add_command(label="Codes Preview",command=mPreviewCode)
menubar.add_cascade(label="Edit",menu=menu2)

menu3=tk.Menu(menubar,tearoff=False)
menu3.add_command(label="MIC recording",command=lambda:typicalScript('DRVIExample_Recording.py'))
menu3.add_command(label="WAV playing",command=lambda:typicalScript('DRVIExample_Play.py'))
menu3.add_command(label="SineWave and Piano",command=lambda:typicalScript('DRVIExample_Piano.py'))
menu3.add_command(label="Signal waveform and spectrum",command=lambda:typicalScript('DRVIExample_Spectrum.py'))
menu3.add_command(label="Roles of Window function",command=lambda:typicalScript('DRVIExample_Window.py'))
menu3.add_command(label="Load and save signals",command=lambda:typicalScript('DRVIExample_SaveLoad.py'))
menu3.add_command(label="APP Class",command=lambda:typicalScript('DRVIExample_AppClass.py'))
menu3.add_separator()
menu3.add_command(label="MIC recording codes",command=lambda:viewtypicalScript('DRVIExample_Recording.py'))
menu3.add_command(label="WAV playing codes",command=lambda:viewtypicalScript('DRVIExample_Play.py'))
menu3.add_command(label="SineWave and Piano codes",command=lambda:viewtypicalScript('DRVIExample_Piano.py'))
menu3.add_command(label="Signal waveform and spectrum codes",command=lambda:viewtypicalScript('DRVIExample_Spectrum.py'))
menu3.add_command(label="Roles of Window function codes",command=lambda:viewtypicalScript('DRVIExample_Window.py'))
menu3.add_command(label="Load and save signals",command=lambda:viewtypicalScript('DRVIExample_SaveLoad.py'))
menu3.add_command(label="APP Class codes",command=lambda:viewtypicalScript('DRVIExample_AppClass.py'))
menubar.add_cascade(label="APP-Samples",menu=menu3)

menu5=tk.Menu(menubar,tearoff=False)
menu5.add_command(label="MP3 to WAV(By ffmpeg)",command=mp3ToWav)
menu5.add_command(label="MP4 get WAV(By ffmpeg)",command=mp4ToWav)
menu5.add_separator()
menu5.add_command(label="Play MP3(By ffmpeg)",command=mp3Play)
menu5.add_command(label="Play MP4(By ffmpeg)",command=mp4Play)
menu5.add_separator()
menu5.add_command(label="Color code",command=selColor)
menu5.add_separator()
menu5.add_command(label="COM List",command=listCOM)
menubar.add_cascade(label="Tools",menu=menu5)

menu4=tk.Menu(menubar,tearoff=False)
menu4.add_command(label="About DRPython",command=mAbout)
menu4.add_separator()
menu4.add_command(label="Helps",command=mHelp)
menubar.add_cascade(label="About",menu=menu4)

win.config(menu=menubar)

#==新工具条============================================
xBar=tk.Frame(win,highlightbackground = "#666666",highlightthickness=1);
xBar.pack(side=tk.TOP,fill=tk.X)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt1=insertIcon(xBar,winDir+'\\imgs\\new.png','New GUI',tNew)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt2=insertIcon(xBar,winDir+'\\imgs\\open.png','Open GUI',tOpen)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt3=insertIcon(xBar,winDir+'\\imgs\\save.png','Save GUI',tSave)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt4=insertIcon(xBar,winDir+'\\imgs\\export.png','Export GUI to APP',tPython)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt42=insertIcon(xBar,winDir+'\\imgs\\export1.png','Export proportional GUI to APP',tPython1)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt41=insertIcon(xBar,winDir+'\\imgs\\class.png','Export GUI to APP Class',tPythonClass)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt5=insertIcon(xBar,winDir+'\\imgs\\debug.png','Edit Python APP',tEditPython)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt6=insertIcon(xBar,winDir+'\\imgs\\insert.png','Insert widgets',tEditControl)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt7=insertIcon(xBar,winDir+'\\imgs\\del.png','Delete widgets',tDelControl)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt9=insertIcon(xBar,winDir+'\\imgs\\color.png','Color code',tColor)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bta=insertIcon(xBar,winDir+'\\imgs\\preview.png','APP Preview',tPreview)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
btb=insertIcon(xBar,winDir+'\\imgs\\code.png',' Codes Preview',tPreviewCode)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt55=insertIcon(xBar,winDir+'\\imgs\\command.png','Command Window',tIDLE)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
btc=insertIcon(xBar,winDir+'\\imgs\\help.png','Helps',tHelp)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
btd=insertIcon(xBar,winDir+'\\imgs\\about.png','About DRPython',tAbout)
#==属性表============================================
pt8=tk.Entry(xBar,width=10)
pt8.pack(side=tk.RIGHT)
pt8.bind("<Return>",setControlls)
bb=tk.Label(xBar,text='  fgColor'); bb.pack(side=tk.RIGHT)
pt7=tk.Entry(xBar,width=10)
pt7.pack(side=tk.RIGHT)
pt7.bind("<Return>",setControlls)
bb=tk.Label(xBar,text='  bgColor'); bb.pack(side=tk.RIGHT)
pt6=tk.Entry(xBar,width=6)
pt6.pack(side=tk.RIGHT)
pt6.bind("<Return>",setControlls)
bb=tk.Label(xBar,text='  Height'); bb.pack(side=tk.RIGHT)
pt5=tk.Entry(xBar,width=6)
pt5.pack(side=tk.RIGHT)
pt5.bind("<Return>",setControlls)
bb=tk.Label(xBar,text='  Width'); bb.pack(side=tk.RIGHT)
pt4=tk.Entry(xBar,width=6)
pt4.pack(side=tk.RIGHT)
pt4.bind("<Return>",setControlls)
bb=tk.Label(xBar,text='  Y0'); bb.pack(side=tk.RIGHT)
pt3=tk.Entry(xBar,width=6)
pt3.pack(side=tk.RIGHT)
pt3.bind("<Return>",setControlls)
bb=tk.Label(xBar,text='  X0'); bb.pack(side=tk.RIGHT)
pt2=tk.Entry(xBar,width=10)
pt2.pack(side=tk.RIGHT)
pt2.bind("<Return>",setControlls)
bb=tk.Label(xBar,text='   Title'); bb.pack(side=tk.RIGHT)
setProtiesWin(0)

#==状态条============================================
tbar2=tk.Frame(win,highlightbackground = "#666666", highlightthickness=1);
tbar2.pack(side=tk.BOTTOM,fill=tk.X)
statusbar1 = tk.Label(tbar2,text="____Insert Status____", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar1.pack(side=tk.LEFT, fill=tk.X)
statusbar = tk.Label(tbar2,text="    Ready  …", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.LEFT, fill=tk.X)

#==左侧控件窗============================================
tbar0=tk.Frame(win,bg='#cccccc',highlightbackground ="#666666", highlightthickness=1);
tbar0.pack(side=tk.RIGHT,fill=tk.Y)
tvItem = ttk.Treeview(tbar0)
tvItem.column('#0', anchor=tk.CENTER, width=120)
tvItem.heading('#0', text='Widget List', anchor=tk.CENTER)
tvItem.insert(parent='', index=0, iid=0, text='Button')
tvItem.insert(parent='', index=1, iid=1, text='GButton')
tvItem.insert(parent='', index=2, iid=2, text='Switch')
tvItem.insert(parent='', index=3, iid=3, text='IconButton')
tvItem.insert(parent='', index=4, iid=4, text='HBGroup')
tvItem.insert(parent='', index=5, iid=5, text='VBGroup')
tvItem.insert(parent='', index=6, iid=6, text='Label')
tvItem.insert(parent='', index=7, iid=7, text='Text')
tvItem.insert(parent='', index=8, iid=8, text='List')
tvItem.insert(parent='', index=9, iid=9, text='Entry')

tvItem.insert(parent='', index=10, iid=10, text='RadioBut')
tvItem.insert(parent='', index=11, iid=11, text='CheckBut')
tvItem.insert(parent='', index=12, iid=12, text='ListBox')
tvItem.insert(parent='', index=13, iid=13, text='Combobox')
tvItem.insert(parent='', index=14, iid=14, text='OptionMenu')
tvItem.insert(parent='', index=15, iid=15, text='SpinBox')
tvItem.insert(parent='', index=16, iid=16, text='Knob')
tvItem.insert(parent='', index=17, iid=17, text='HScale')
tvItem.insert(parent='', index=18, iid=18, text='VScale')
tvItem.insert(parent='', index=19, iid=19, text='HSlider')

tvItem.insert(parent='', index=20, iid=20, text='VSlider')
tvItem.insert(parent='', index=21, iid=21, text='Progress')
tvItem.insert(parent='', index=22, iid=22, text='Ruler')
tvItem.insert(parent='', index=23, iid=23, text='HRuler')
tvItem.insert(parent='', index=24, iid=24, text='Gauge')
tvItem.insert(parent='', index=25, iid=25, text='Digital')
tvItem.insert(parent='', index=26, iid=26, text='Lamp')
tvItem.insert(parent='', index=27, iid=27, text='Info')
tvItem.insert(parent='', index=28, iid=28, text='Tab')
tvItem.insert(parent='', index=29, iid=29, text='Plot')

tvItem.insert(parent='', index=30, iid=30, text='PlotFast')
tvItem.insert(parent='', index=31, iid=31, text='Stem')
tvItem.insert(parent='', index=32, iid=32, text='SemilogX')
tvItem.insert(parent='', index=33, iid=33, text='SemilogY')
tvItem.insert(parent='', index=34, iid=34, text='LogLog')
tvItem.insert(parent='', index=35, iid=35, text='PlotBar')
tvItem.insert(parent='', index=36, iid=36, text='PlotPie')
tvItem.insert(parent='', index=37, iid=37, text='PlotPolar')
tvItem.insert(parent='', index=38, iid=38, text='Plot3D')
tvItem.insert(parent='', index=39, iid=39, text='PlotSurf')
tvItem.insert(parent='', index=40, iid=40, text='PlotContour')

tvItem.insert(parent='', index=41, iid=41, text='Timer')
tvItem.insert(parent='', index=42, iid=42, text='Recorder')
tvItem.insert(parent='', index=43, iid=43, text='Play')
tvItem.insert(parent='', index=44, iid=44, text='PlayX')
tvItem.insert(parent='', index=45, iid=45, text='ArduinoAD')
tvItem.insert(parent='', index=46, iid=46, text='TCPS')
tvItem.insert(parent='', index=47, iid=47, text='UDPS')
tvItem.insert(parent='', index=48, iid=48, text='UDPBS')
tvItem.insert(parent='', index=49, iid=49, text='==========')

tvScroll1 = ttk.Scrollbar(tbar0, orient='vertical',command=tvItem.yview)
tvScroll1.pack(side=tk.RIGHT, fill=tk.Y)
tvItem.configure(yscrollcommand=tvScroll1.set)
tvItem.pack(side=tk.RIGHT,fill=tk.Y)
tvItem.bind('<<TreeviewSelect>>', gettvID)
tvItem.bind('<ButtonRelease-1>',tvmouseUP)
tvItem.bind('<ButtonRelease-3>',tvmouseRightUP)
tvItem.selection_set(0)

#logo
mFirst=0
mLogo=dr.DRIcon(win,(wWin-472)/2,(hWin-200)/2,472,110,'imgs/drpython.png',400)

#==Main Start============================================
win.mainloop()
#==Main Stop============================================
