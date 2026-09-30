import os
import sys
import os.path
from tkinter import scrolledtext

idlelib_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if idlelib_dir not in sys.path: sys.path.insert(0, idlelib_dir)
from idlelib import editor
from idlelib.pyshell import main as IDLE

import drvi.drviAppendPath as mPath
#添加Python工作路径，仅非安装的便携Python需要此语句
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
from drvi import drColorWin as colorWin

sLogo="""
# DRPython
# Copyright (C) 2022
# Author: Lingsong HE
# Organization: Huazhong University of Science and Technology
# Contact: helingsong@hust.edu.cn                                      
"""

#==Draw Logo===
def drawBLine(p):
    for i in range(20):
        p.create_line(i*50,0,i*50,4000,width=1,fill='#888888',dash=(3,2))
        p.create_line(0,i*50,4000,i*50,width=1,fill='#888888',dash=(3,2))   
    
def drawLogo(p):
    p.create_text(60,20,font=("Arial", 12), fill='#0000ee',anchor='nw',text=sLogo)
    p.create_text(60,140,font=("Arial",100),fill='#0000aa',anchor='nw',text='DR.Python')
    
    
#===================================================================
def setTreeItem(tvItem,k,S):
    tvItem.insert(parent='', index=k, iid=k, text=S)
    return k+1;

def importWin(event):
    global win,mImport;
    mSTR=code.setStringWinX(win,'import信息窗口',600,300,mImport).getInput()
    if mSTR!="": mImport=mSTR

def blockXML(event):
    global currentN,controlTypeGroup,controlNameGroup,controlXML
    S=controlNameGroup[currentN];
    S1=controlXML[currentN];
    if S1!=None:
        mSTR=code.setStringWinX(win,S+' Python Script信息',600,300,S1).getInput()
        if mSTR!="": controlXML[currentN]=mSTR;

#===导出的Python暂存文件========================================================
def saveTemp(SS):
    global rootPath;
    mSave=rootPath+"\\tempFile.py"    
    text_file = open(mSave,"w", encoding="utf-8")
    text_file.write(SS)
    text_file.close()
    return mSave;

#===取插入探针对应的Python代码==============================================
#被连接 addCallBack2D(muserArrayTwo1)
def getProbeText(t):
    global probLineS1,probLineS2,probLineS11,probLineS12,probeLineN    
    mProbTxt=""; 
    if probeLineN<1: return mProbTxt
    for i in range(probeLineN):
        if probLineS1[i].find('user')<0:
            if t==0:
                S1='m'+probLineS1[i]+'.'+probLineS11[i]+'('+'m'+probLineS2[i];
                S2='.'+probLineS12[i]
            if t==1:
                S1='        self.m'+probLineS1[i]+'.'+probLineS11[i]+'('+'self.m'+probLineS2[i];
                S2='.'+probLineS12[i]
            if probLineS2[i].find('user')>=0: S2=""   #用户定义函数
            S=S1+S2+')\n'
            mProbTxt=mProbTxt+S
    return mProbTxt

#==连接 def muserArrayTwo1(tDataArray,xDataArray):
#           mPlot2.setValue2D(tDataArray,xDataArray)
def getControlXML(S):
 for i in range(0,500):
     if S==controlNameGroup[i]:
         return controlXML[i]
 return ""

def getUserFunctionProbeText(t,S):
    global probLineS1,probLineS2,probLineS11,probLineS12,probeLineN,probLineType;           
    for i in range(probeLineN):
        if probLineS1[i].find('user')>=0:
            S11=getControlXML(probLineS1[i])
            S01='#=='+probLineS1[i]
            if t==0:                       
                S02=S11+"\n"                
                S02=S02+'m'+probLineS2[i]+'.'+probLineS12[i]
                S02=S02.replace('\n','\n ') #对齐         
            if t==1:
                S02=S11+"\n"
                S02=S02+'self.m'+probLineS2[i]+'.'+probLineS12[i]
                S02=S02.replace('\n','\n        ') #对齐
            if probLineType[i]==1: S02=S02+'(v)'
            if probLineType[i]==2: S02=S02+'(txt)'
            if probLineType[i]==3: S02=S02+'(dx,xDataArray)'
            if probLineType[i]==4: S02=S02+'(tDataArray,xDataArray)'
            if probLineType[i]==5: S02=S02+'(xDataArray,yDataArray,zDataArray)'
            if probLineType[i]==6: S02=S02+'(xImage)'
            S=S.replace(S01,S02);
    return S

#==弹出连线菜单回调函数===========================================================
def probeMenu(s):
    global currentN,probeST,probeS1,probeS2,probeS11,probeS12,controlNameGroup;
    global win,probLine1,probLineS1,probLineS2,probLineS11,probLineS12,probeLineN,probLineType,myCanvas
    global controlN,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup        
    #取消当前连线
    if s=='取消':
        currentN=0;
        probeST=0;
        return;
    #选择起点
    if probeST==0:
        probeS1=controlNameGroup[currentN]
        probeS11=s
        probeST=1;
        currentN=0;
        return;
    #选择终点，并完成连线
    if probeST==1:
        probeS2=controlNameGroup[currentN]
        probeS12=s    
        t1=code.lineType1(probeS11)
        t2=code.lineType1(probeS12)
        if t1!=t2:
            msgbox.showwarning(title='线性匹配错误：', message=probeS11+"-->"+probeS12)
            currentN=0;
            probeST=0;
            return;        
        probLineS1[probeLineN]=probeS1
        probLineS2[probeLineN]=probeS2
        probLineS11[probeLineN]=probeS11
        probLineS12[probeLineN]=probeS12
        probLineType[probeLineN]=t1;        
        probeLineN=probeLineN+1
        probLine1=code.redrawAllProbeX(myCanvas,probeLineN,probLine1,probLineS1,probLineS2,probLineType,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup)
        probeST=0;
        currentN=0;
        return;   
    return 1

#===弹出菜单
def linePopMenu(win,x,y,p1,p2,p3,p4,p5,p6,p7,p8):
    x0=win.winfo_x()
    y0= win.winfo_y()    
    popupmenu = tk.Menu(win,tearoff=False)
    if p1!=None: popupmenu.add_command(label=code.setLineType(p1),command=lambda:probeMenu(p1))
    if p2!=None: popupmenu.add_command(label=code.setLineType(p2),command=lambda:probeMenu(p2))
    if p3!=None: popupmenu.add_command(label=code.setLineType(p3),command=lambda:probeMenu(p3))
    if p4!=None: popupmenu.add_command(label=code.setLineType(p4),command=lambda:probeMenu(p4))
    if p5!=None: popupmenu.add_command(label=code.setLineType(p5),command=lambda:probeMenu(p5))
    if p6!=None: popupmenu.add_command(label=code.setLineType(p6),command=lambda:probeMenu(p6))
    if p7!=None: popupmenu.add_command(label=code.setLineType(p7),command=lambda:probeMenu(p7))
    if p8!=None: popupmenu.add_command(label=code.setLineType(p8),command=lambda:probeMenu(p8))
    popupmenu.add_command(label='取消',command=lambda:probeMenu('取消')) 
    popupmenu.post(int(x0+x),int(y0+y))
 
#==================================================
def insertIcon(win,data,txt,fun):
    img = tk.PhotoImage(file=data)
    L=tk.Label(win,image=img)
    L.pack(side=tk.LEFT)
    L.bind('<Button-1>',fun)
    L.bind('<Motion>',fun)
    L_ttp = dr.ToolTip(L,txt)
    return L,img

#====================================
def listCOM():
    listCOM=list(serial.tools.list_ports.comports())
    S=''
    for i in range(0,len(listCOM)):
        S=S+listCOM[i][0]+'  :  '+listCOM[i][1]+'\n'
    k=msgbox.askyesno('COM口列表',S)
 
def gettvID(event):
    global tvItem,mFirst;   
    editControl();    
    ss=tvItem.item(event.widget.selection(),'text')
    # hls 取消'_Tk'----
    ss=ss.replace('_Tk','');    
    kk=code.nameToType(ss)
    setInsertControlls(kk) 
    return 1

#帮助文件===============================
def tvmouseRightUP(event):
    global winDir,drviPath
    x=event.x;
    if x<0: return
    s=code.typeToName(controlType);
    if len(s)<2: return
    mPath=drviPath+'\\html\\'+s+'.pdf'
    if mPath.find('DRArduino')>=0:
        mPath=mPath.replace('DRArduino.pdf','arduino.html');
    if mPath.find('DRADALM2K')>=0:
        mPath=mPath.replace('DRADALM2K.pdf','ADALM2K.html');   
    os.system(mPath)
    #print('aaaa',mPath)     
  
def tvmouseUP(event):
 global currentN,controlN,controlType,mFirst
 global controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 if mFirst==0:
     mFirst=1;
     myCanvas.delete('all')
     drawBLine(myCanvas) 
 x=event.x; y=event.y
 if x>0: return
 x=controlWGroup[0]+x-120
 y=y+30 
 controlN=controlN+1
 w=0; h=0; bg=''; fg=''; s=""; s1=""; s2=""
 s,s1,s2,w,h=code.getInitControlPar(controlType,controlN)
 pushControlPar(controlN,controlType,1,s,s1,s2,x,y,w,h,'#ffffdd','#000000'); 
 insertDRControlls(controlN);
 controlType=0
 return 1

#用控件组数据刷新属性窗参数============================
def setProtiesWin(i):
 global win,probLine1,probLineS1,probLineS2,probeLineN,myCanvas,probLineType
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup,controlParGroup
 global pt1,pt2,pt3,pt4,pt5,pt6
 S=controlNameGroup[i]; x=controlX0Group[i]; y=controlY0Group[i]; w=controlWGroup[i]; h=controlHGroup[i]; b=controlbgGroup[i]; f=controlfgGroup[i]
 pt2.delete(0,20); pt2.insert(0,S)
 pt3.delete(0,20); pt3.insert(0,str(x))
 pt4.delete(0,20); pt4.insert(0,str(y))
 pt5.delete(0,20); pt5.insert(0,str(w))
 pt6.delete(0,20); pt6.insert(0,str(h))
 #用控件组数据刷新探针曲线=====
 if probeLineN<1: return 
 probLine1=code.redrawAllProbeX(myCanvas,probeLineN,probLine1,probLineS1,probLineS2,probLineType,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup)
 return 1

#===插入尺寸可调整控件=====================================
def posChanged(ID,x,y,w,h):
    global currentN
    N=ID; currentN=ID;
    if editStatus>0: return;
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
 global controlN,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 for i in range(1,500):
  C=controlGroup[i]
  if C!=0:
   C.ax.destroy(); controlGroup[i]=0; controlTypeGroup[i]=0
 controlN=0   
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
    controlParGroup=['' for x in range(0,511)]
    controlXML=[None for x in range(0,511)]
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
    statusbar.config(text=' 新建GUI布局文件')

def mNew():
 global win,probLine1,probeLineN,myCanvas;
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 k=msgbox.askyesno('确认操作', '该操作将删除所有已布局的控件 ？')
 if k==False:  return 1
 probeLineN=code.delAllProbe(myCanvas,probeLineN,probLine1)
 delAllControls(); initAll(); setProtiesWin(0)
 return 1

def tXML(event):
    if event.num==1: mXMLFile();

def mXMLFile():
    global rootPath,controlN,mXML,win,mXML;   
    mFile=rootPath+"\\tempFile.xml"
    if controlN<1: return;
    mSave(mFile);
    text_file = open(mFile,"r",encoding='utf-8')
    mXML=text_file.read()
    text_file.close()
    
    mSTR=code.setStringWinX(win,'import信息窗口',950,400,mXML).getInput()
    if mSTR!="":
        mXML=mSTR
        text_file = open(mFile,"w", encoding="utf-8")
        text_file.write(mXML)
        text_file.close()
        mOpen(mFile);
        
#读文件
def tOpen(event):
    global controlN;
    if event.num==1:
        if controlN>1:
            k=msgbox.askyesno('确认操作', '该操作将删除所有已布局的控件 ？')
            if k==False: return 1
        mfile=filedialog.askopenfilename(title="选择文件",filetypes=(("xml files", "*.xml"),("all files", "*.*")))
        if not mfile: return 1
        mOpen(mfile);
    
def mOpenFile():
    global controlN;
    if controlN>1:
        k=msgbox.askyesno('确认操作', '该操作将删除所有已布局的控件 ？')
        if k==False: return 1
    mfile=filedialog.askopenfilename(title="选择文件",filetypes=(("xml files", "*.xml"),("all files", "*.*")))
    if not mfile: return 1
    mOpen(mfile);

def mOpen(mfile):
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 global probeLineN,probLine1;
 probeLineN=code.delAllProbe(myCanvas,probeLineN,probLine1)
 delAllControls(); initAll(); setProtiesWin(0) 
 NB=xmlParser.openXML(mfile);
 for k in range(NB):
    M,S,D=xmlParser.readBlock(k)
    if M>0:
        insertXMLBlock(M,S,D);
        insertXMLLine(M,S,D);
        getImport(M,S,D);
 setProtiesWin(0)
 return 1

def insertXMLLine(M,S,D):
    global controlN,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
    global probeLineN,probLine1,probLineType;
    if S[0]!='ProbeLine': return;
    S1=S[1].split(',')
    probLineS1[probeLineN]=S1[0]
    probLineS11[probeLineN]=S1[1]
    probLineS2[probeLineN]=S1[2]
    probLineS12[probeLineN]=S1[3]
    probLineType[probeLineN]=int(S1[4])
    probeLineN=probeLineN+1
    probLine1=code.redrawAllProbeX(myCanvas,probeLineN,probLine1,probLineS1,probLineS2,probLineType,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup)

def insertXMLBlock(M,S,D):
    global controlN,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
    global probeLineN,probLine1;
    if S[0].find('ProbeLine')>=0: return;
    if S[0].find('Import')>=0: return;
    if S[0].find('Global')>=0: return;
    if S[0].find('Main')>=0: return;
    controlN=controlN+1;
    controlNameGroup[controlN]=S[0]
    S1=S[1].split(',')
    t=int(S1[0]); x=int(S1[1]); y=int(S1[2]); w=int(S1[3]); h=int(S1[4])
    controlTypeGroup[controlN]=t    
    controlX0Group[controlN]=x
    controlY0Group[controlN]=y
    controlWGroup[controlN]=w
    controlHGroup[controlN]=h
    controlbgGroup[controlN]="#ffffaa"
    controlfgGroup[controlN]="#000000"
    controlParGroup[controlN]=S[2]
    controlXML[controlN]=D    
    insertDRControlls(controlN);
def getImport(M,S,D):
    global mImport
    if S[0]!='Import': return;
    mImport=D;

#=============================================
#保存文件
def tSave(event):
    global controlN;    
    if event.num==1:
        if controlN<1: return; 
        statusbar.config(text=' 保存当前GUI布局到XML文件')
        mfile=filedialog.asksaveasfile(title="选择文件",defaultextension=".xml",initialfile = "Untitled.xml",filetypes=(("xml files", "*.xml"),("all files", "*.*")))
        if not mfile: return 1 
        mSave(mfile.name);

def mSaveFile():
    if controlN<1: return;
    statusbar.config(text=' 保存当前GUI布局到XML文件')
    mfile=filedialog.asksaveasfile(title="选择文件",defaultextension=".xml",initialfile = "Untitled.xml",filetypes=(("xml files", "*.xml"),("all files", "*.*")))
    if not mfile: return 1 
    mSave(mfile.name);
    
def mSave(mFile):
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup,controlParGroup
 global probeLineN,probLine1,probLineS1,probLineS2,probLineS11,probLineS12,probLineType
 xmlParser.newXML();
 for i in range(0,500):
     C=controlGroup[i]
     if C!=0:
         S=str(controlTypeGroup[i])+','
         S=S+str(controlX0Group[i])+','
         S=S+str(controlY0Group[i])+','
         S=S+str(controlWGroup[i])+','
         S=S+str(controlHGroup[i])
         xmlParser.writeBlock(name=controlNameGroup[i],p1=S,p2=controlParGroup[i],data=controlXML[i]);
 if probeLineN>0:
     for i in range(0,probeLineN):
         xmlParser.writeBlock(name='ProbeLine',p1=probLineS1[i]+","+probLineS11[i]+","+probLineS2[i]+","+probLineS12[i]+","+str(probLineType[i]))
 xmlParser.writeBlock(name="Import",data=mImport);
 xmlParser.saveXML(mFile);
 return 1

#转化为PY脚本
def tPython(event):
    if event.num==1: mToPython();return;
    statusbar.config(text=' 导出DRVItk APP代码')

def mToPython():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup,controlParGroup
 global sWidth,sHeight,mImport
 if controlN<1: return; 
 [N,S,XX]=code.toPythonScriptNew(sWidth,sHeight,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlParGroup)
 if N<2: return 1
 S=getUserFunctionProbeText(0,S);
 mProbTxt=getProbeText(0); 
 S=S.replace('#ZZZZZZZZ',mProbTxt);
 S=S.replace('#I-I-I-I-',mImport);
 mfile=saveTemp(S);
 runBatFile(dsp.getIDLEPath(),mfile)
 return 1

#转化为PY脚本
def tPython1(event):
    if event.num==1: mToPython1();return;
    statusbar.config(text=' 导出可调节DRVItk APP代码')
    
def mToPython1():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup,controlParGroup
 global sWidth,sHeight 
 if controlN<1: return; 
 [N,S,XX]=code.toPythonScriptNew(sWidth,sHeight,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlParGroup)
 if N<2: return 1
 S=getUserFunctionProbeText(0,S);
 mProbTxt=getProbeText(0);  
 S=S.replace('#ZZZZZZZZ',mProbTxt);
 SS=code.getResizeCode()
 S=S.replace('#-#-#-#-',SS);
 SS=code.getAddResizeCode() 
 S=S.replace('#=#=#=',SS); 
 S=S.replace('#--#--#--',XX);
 S=S.replace('#I-I-I-I-',mImport);
 mfile=saveTemp(S);
 runBatFile(dsp.getIDLEPath(),mfile)
 return 1

def tPythonClass(event):
    if event.num==1: mToPythonClass();return;
    statusbar.config(text=' 导出可调节DRVItk APP Class代码')

def mToPythonClass():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup,controlParGroup
 if controlN<1: return; 
 [N,S]=code.toPythonScriptClass(currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup,controlParGroup)
 if N<2: return 1
 mProbTxt=getProbeText(1);
 S=getUserFunctionProbeText(1,S);
 S=S.replace('#ZZZZZZ',mProbTxt);
 S=S.replace('#I-I-I-I-',mImport);
 mfile=saveTemp(S);
 runBatFile(dsp.getIDLEPath(),mfile)   
 return 1

def tPyqt(event):
    if event.num==1: mToPyqt();return;
    statusbar.config(text=' 导出可调节DRqt APP Class代码')

def mToPyqt():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup,controlParGroup
 if controlN<1: return; 
 [N,S]=code.toPyqt(currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup,controlParGroup)
 if N<2: return 1
 mProbTxt=getProbeText(1);
 S=getUserFunctionProbeText(1,S);
 S=S.replace('#ZZZZZZ',mProbTxt);
 S=S.replace('#I-I-I-I-',mImport);
 mfile=saveTemp(S);
 runBatFile(dsp.getIDLEPath(),mfile)   
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
    statusbar.config(text=' Python代码调试')
    
def mEditPython():
 global winDir
 mfile=filedialog.askopenfilename(title="选择文件",filetypes=(("Python files", "*.py"),("all files", "*.*")))
 if not mfile: return 1
 name=winDir+'\\temp.bat'
 mfile='"'+mfile+'"'
 runBatFile(dsp.getIDLEPath(),mfile)
 return 1

#启动IDLE编辑器
def mIDLE():
    mfile=""
    runBatFile(dsp.getIDLEPath(),mfile)

#典型代码
def typicalScript(mfile):
 runBatFile(dsp.getPythonPath(),mfile)
 return 1

def typicalXMLScript(mfile):
    global drviPath
    path=drviPath+'\\z_xml\\'+mfile    
    mOpen(path)

#样例程序
def setExample(k):
    global demoFile
    path=os.getcwd()+'\\z_example'
    mfile=path+'\\'+demoFile[k]
    mfile='"'+mfile+'"'
    runBatFile(dsp.getPythonPath(),mfile)
    return 1

#退出程序
def mExit():
 win.destroy()
 return 1

#关于DRPython
def tAbout(event):
    if event.num==1: mAbout();return;
    statusbar.config(text=' 关于DRPython')
    
def mAbout():
    global winDir,drviPath
    mPath=drviPath+'\\html\\about.pdf'
    os.system(mPath)
    
#在线帮助
def tHelp(event):
    if event.num==1: mHelp();return;
    statusbar.config(text=' 显示帮助文档')
    
def mHelp():
    global winDir,drviPath
    mPath=drviPath+'\\html\\index.html'
    os.system(mPath)
  
    
#进入编辑状态，在该状态可以插入新控件
def tEditControl(event):
    if event.num==1: editControl();return;
    statusbar.config(text=' 进入插入状态')

def editControl():
 global editStatus,statusbar1,currentN;
 editStatus=0; currentN=0;
 statusbar1.config(text="____插入状态____")   
 return 1

#进入删除控件状态
def tDelControl(event):
    global currentN
    if event.num==1:
        currentN=0;
        delControl();
        return;
    statusbar.config(text=' 进入删除状态')

def delControl():
 global editStatus,statusbar1,currentN;
 editStatus=1; currentN=0;
 statusbar1.config(text="____删除状态____")   
 return 1

#插入信号探针
def tInsertProbe1(event):
    global editStatus,statusbar1,currentN;
    if event.num==1:
        editStatus=2; currentN=0;
        statusbar1.config(text="____连线状态____")
        return 1

def insertProbe1():
    global editStatus,statusbar1,currentN;
    editStatus=2; currentN=0;
    statusbar1.config(text="____连线状态____")
    return 1    

#色彩选择
def tColor(event):
    if event.num==1: selColor();return;
    statusbar.config(text=' 色彩码选择窗')
    
def selColor():
 c=colorchooser.askcolor(title ="Choose color")
 if c[0]==None: return 
 statusbar.config(text=' 当前选择的色彩码 : '+c[1])
 print(' 当前选择的色彩码 : '+c[1])
 win.clipboard_clear()
 win.clipboard_append(c[1])
 return 1

#设计预览
def tPreview(event):
    if event.num==1: mPreview(); 
    
def mPreview():
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup,controlParGroup
 global sWidth,sHeight
 if controlN<1: return; 
 [N,S,XX]=code.toPythonScriptNew(sWidth,sHeight,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlParGroup)
 if N<2: return 1
 S=getUserFunctionProbeText(0,S);
 mProbTxt=getProbeText(0); 
 S=S.replace('#ZZZZZZZZ',mProbTxt);
 S=S.replace('#I-I-I-I-',mImport);
 global winDir
 mfile=winDir+'\\temp.py'
 text_file = open(mfile,"w", encoding="utf-8")
 text_file.write(S)
 text_file.close()
 mfile='"'+mfile+'"'
 runBatFile(dsp.getPythonPath(),mfile)
 return 1

#==工具条插入控件回调函数===========================================
def setInsertControlls(k):
 global controlType,statusbar;
 controlType=k
 if k==1:
     statusbar.config(text=' 当前选择的控件类型 : 按钮 Button')
 if k==101:
     statusbar.config(text=' 当前选择的控件类型 : 水平按钮组 Horizontal Button Group')
 if k==102:
     statusbar.config(text=' 当前选择的控件类型 : 垂直按钮组 Vertical Button Group')          
 if k==2:
     statusbar.config(text=' 当前选择的控件类型 : 标签 Label')
 if k==3:
     statusbar.config(text=' 当前选择的控件类型 : 输入框 Entry')
 if k==301:
     statusbar.config(text=' 当前选择的控件类型 : 水平输入框组 Horizontal Entry Group')
 if k==302:
     statusbar.config(text=' 当前选择的控件类型 : 垂直输入框组 Vertical Entry Group')         
 if k==4:
     statusbar.config(text=' 当前选择的控件类型 : 水平标尺 Horizontal Scale')   
 if k==5:
     statusbar.config(text=' 当前选择的控件类型 : 垂直标尺 Vertical Scale')   
 if k==6:
     statusbar.config(text=' 当前选择的控件类型 : RadioButton')   
 if k==81:
     statusbar.config(text=' 当前选择的控件类型 : 水平RadioButton')   
 if k==7:
     statusbar.config(text=' 当前选择的控件类型 : CheckButton')
 if k==82:
     statusbar.config(text=' 当前选择的控件类型 : 水平CheckButton')
 if k==8:
     statusbar.config(text=' 当前选择的控件类型 : 列表框 ListBox')   
 if k==9:
     statusbar.config(text=' 当前选择的控件类型 : 下拉列表框 ComboBox')   
 if k==10:
     statusbar.config(text=' 当前选择的控件类型 : 文本框 Text')
 if k==11:
     statusbar.config(text=' 当前选择的控件类型 : SpinBox')
 if k==12:
     statusbar.config(text=' 当前选择的控件类型 : 图标 Icon')
 if k==13:
     statusbar.config(text=' 当前选择的控件类型 : 水平进度条 ProgressBar')
 if k==80:
     statusbar.config(text=' 当前选择的控件类型 : 垂直进度条 VProgressBar')
 if k==14:
     statusbar.config(text=' 当前选择的控件类型 : 弹出菜单 OptionMenu')

 if k==30:
     statusbar.config(text=' 当前选择的控件类型 : 旋钮 Knob')
 if k==83:
     statusbar.config(text=' 当前选择的控件类型 : 渐变色旋钮 GKnob')
 if k==31:
     statusbar.config(text=' 当前选择的控件类型 : 棒图 Ruler')
 if k==32:
     statusbar.config(text=' 当前选择的控件类型 : 水平滑条 HSlider')
 if k==33:
     statusbar.config(text=' 当前选择的控件类型 : 垂直滑条 VSlider')
 if k==34:
     statusbar.config(text=' 当前选择的控件类型 : 表盘控件 Gauge')         
 if k==35:
     statusbar.config(text=' 当前选择的控件类型 : 开关控件 Switch')
 if k==36:
     statusbar.config(text=' 当前选择的控件类型 : 数显控件 Digital')
 if k==39:
     statusbar.config(text=' 当前选择的控件类型 : 报警灯控件 Lamp')       
 if k==37:
     statusbar.config(text=' 当前选择的控件类型 : 页帧控件 Tab')
 if k==84:
     statusbar.config(text=' 当前选择的控件类型 : 页帧控件 NoteBook')
 if k==40:
     statusbar.config(text=' 当前选择的控件类型 : 水平表盘 HRuler')
 if k==41:
     statusbar.config(text=' 当前选择的控件类型 : 渐变色按钮 GButton')
 if k==42:
     statusbar.config(text=' 当前选择的控件类型 : 列表控件 List')          
          
 if k==51:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 Plot')
 if k==52:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 PlotBar')
 if k==53:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 PlotPie')
 if k==54:
     statusbar.config(text=' 当前选择的控件类型 : 三维曲线 Plot3D')     
 if k==55:
     statusbar.config(text=' 当前选择的控件类型 : 三维曲线 PlotSurface')
 if k==56:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 PlotPolar')
 if k==57:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 PlotContour')
 if k==58:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 FastPlot')
 if k==59:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 Stem')
 if k==60:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 SemilogX')
 if k==61:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 SemilogY')
 if k==62:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 LogLog')
 #hls 0.
 if k==90:
     statusbar.config(text=' 当前选择的控件类型 : 图象显示控件 Image')   
 if k==91:
     statusbar.config(text=' 当前选择的控件类型 : 文件选择窗控件 FileBut')
 if k==92:
     statusbar.config(text=' 当前选择的控件类型 : 谱阵显示控件 waterFall')
 if k==93:
     statusbar.config(text=' 当前选择的控件类型 : 语谱图显示控件 Colormesh')
 if k==94:
     statusbar.config(text=' 当前选择的控件类型 : STFT谱阵计算控件 Spectgram')
 if k==95:
     statusbar.config(text=' 当前选择的控件类型 : 概率密度和分布控件 PdfCdf')
 if k==96:
     statusbar.config(text=' 当前选择的控件类型 : 相关函数分析控件 Correlate')     
 if k==97:
     statusbar.config(text=' 当前选择的控件类型 : 仿真测试实验台 Tester')
 if k==98:
     statusbar.config(text=' 当前选择的控件类型 : 信号带通滤波器 Filter')
 if k==99:
     statusbar.config(text=' 当前选择的控件类型 : Matplotlib绘图容器控件 Figure')
 if k==401:
     statusbar.config(text=' 当前选择的控件类型 : 多通道示波器控件 Monitor')
 if k==402:
     statusbar.config(text=' 当前选择的控件类型 : 散点图控件 Scatter')
 if k==405:
     statusbar.config(text=' 当前选择的控件类型 : 图像组显示控件 SubImages')
 if k==406:
     statusbar.config(text=' 当前选择的控件类型 : OPenCV驱动的摄像头控件 CameraCV')
 if k==407:
     statusbar.config(text=' 当前选择的控件类型 : OPenCV驱动的视频文件播放控件 VideoCV')
 if k==408:
     statusbar.config(text=' 当前选择的控件类型 : Python脚本控件 Script')
 if k==409:
     statusbar.config(text=' 当前选择的控件类型 : 实时语谱图显示控件 Colormesh')
 if k==410:
     statusbar.config(text=' 当前选择的控件类型 : 实时谱阵显示控件 WaterFallR')
 if k==411:
     statusbar.config(text=' 当前选择的控件类型 : Arduino信号采集卡 Arduino')
 if k==412:
     statusbar.config(text=' 当前选择的控件类型 : ADALM2K信号采集卡 ADALM2K')   
 #============
 if k==70:
     statusbar.config(text=' 当前选择的控件类型 : 定时器 Timer')
 if k==71:
     statusbar.config(text=' 当前选择的控件类型 : 录音 Recorder')
 if k==72:
     statusbar.config(text=' 当前选择的控件类型 : WAV播放器Player')
 if k==77:
     statusbar.config(text=' 当前选择的控件类型 : MP4播放器Player')
 if k==78:
     statusbar.config(text=' 当前选择的控件类型 : 二维曲线 SubPlot')
 if k==79:
     statusbar.config(text=' 当前选择的控件类型 : 数字信号发生器')

 if k==300:
     statusbar.config(text=' 当前选择的控件类型 : 频谱分析计算模块')
 if k==301:
     statusbar.config(text=' 当前选择的控件类型 : 波形分析计算模块')

 if k==200:
     statusbar.config(text=' 当前选择的控件类型 : 用户自定义单值型信号探针函数')
 if k==201:
     statusbar.config(text=' 当前选择的控件类型 : 用户自定义字符串型信号探针函数')
 if k==202:
     statusbar.config(text=' 当前选择的控件类型 : 用户自定义2D曲线型信号探针函数')
 if k==203:
     statusbar.config(text=' 当前选择的控件类型 : 用户自定义采样格式2D曲线型信号探针函数')
 if k==204:
     statusbar.config(text=' 当前选择的控件类型 : 用户自定义图象型信号探针函数')
 if k==205:
     statusbar.config(text=' 当前选择的控件类型 : 用户自定义3D曲线型信号探针函数')     
 return 1


#=Toolbar1 CallBack=====================================================

#==通过右侧属性表更改控件函数=================
def insertDRControlls(N):
    global win,statusbar
    global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
    currentN=N; 
    controlGroup[N]=insertControl(win,controlX0Group[N],controlY0Group[N],controlWGroup[N],controlHGroup[N],controlbgGroup[N],controlfgGroup[N],controlNameGroup[N])    
    return

#右侧属性表回调函数
def setControlls(event):
 global win,statusbar
 global pt1,pt2,pt3,pt4,pt5,pt6
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 statusbar.config(text=' 当前状态: 设定控件属性参数')
 mName=pt2.get()
 mX0=int(pt3.get()); mY0=int(pt4.get())
 mW=int(pt5.get());  mH=int(pt6.get())
 N=currentN
 controlNameGroup[N]=mName; controlX0Group[N]=mX0; controlY0Group[N]=mY0; controlWGroup[N]=mW; controlHGroup[N]=mH; 
 controlGroup[N].ax.destroy()
 insertDRControlls(N) 
 return 1


#=Bind Event CallBack=====================================================

#==保存当前插入的控件参数到控件数组=============
def pushControlPar(N,T,C,S,S1,S2,x,y,w,h,b,f):
 global currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup,controlParGroup,controlXML;
 global pt1,pt2,pt3,pt4,pt5,pt6
 currentN=N;
 controlTypeGroup[N]=T; controlGroup[N]=C;
 controlNameGroup[N]=S; controlParGroup[N]=S1;
 controlX0Group[N]=x;   controlY0Group[N]=y;
 controlWGroup[N]=w;    controlHGroup[N]=h;
 controlbgGroup[N]=b;   controlfgGroup[N]=f
 controlXML[N]=S2;   
 setProtiesWin(N) 
 return 1

#==主窗口回调函数，控件插入================
def rightUP(event):
    global controlType,currentN    
    controlType=controlTypeGroup[currentN]
    tvmouseRightUP(event)

def clickInsert(event):
 global controlType,statusbar,mouseStatus,editStatus
 global controlN,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 global probeST,probeS1,probeS2,probeS11,probeS12; 
 mouseStatus=1
 v=controlType
 x=event.x; y=event.y
 if x>(controlWGroup[0]-140): return;  #控件窗口

 s='  当前鼠标位置 :   '+str(x)+' , '+str(y)
 statusbar.config(text=s)

 #删除状态===================
 if editStatus==1:
     if currentN==0: return;  #无控件
     k=msgbox.askyesno('确认操作', '你确定删除该控件 ？')
     if k==True:
         i=currentN;
         controlGroup[i].ax.destroy();
         controlGroup[i]=0;
         controlTypeGroup[i]=0;
         setProtiesWin(0)
         currentN=0;         
     return 1

 #连线状态===================
 if editStatus==2:
     if currentN==0: return;  #无控件
     i=currentN;
     x=controlX0Group[i]+int(controlWGroup[i]/2)
     y=controlY0Group[i]+controlHGroup[i]
     if probeST==0:         
         p1,p2,p3,p4,p5,p6,p7,p8=code.setMenu0(controlNameGroup[i])
         if p1==None:   return;
     if probeST==1:
         p1,p2,p3,p4,p5,p6,p7,p8=code.setMenu1(controlNameGroup[i])         
     linePopMenu(win,x,y,p1,p2,p3,p4,p5,p6,p7,p8)  
     return 1    
 return 1;

#主窗口鼠标释放回调函数
def releaseInsert(event):
 global mouseStatus 
 mouseStatus=0
 return 1

#主窗口鼠标拖动改变尺寸大小回调函数
def winResize(event):
 global win,sWidth,sHeight,wWin,hWin; 
 global controlN,currentN,controlTypeGroup,controlGroup,controlNameGroup,controlX0Group,controlY0Group,controlWGroup,controlHGroup,controlbgGroup,controlfgGroup
 w=win.winfo_width()
 h=win.winfo_height()
 if (w==controlWGroup[0]) and (h==controlHGroup[0]) : return
 currentN=0; controlWGroup[0]=w; controlHGroup[0]=h;
 setProtiesWin(0)
 wWin=w; hWin=h; 
 
#==GUI Laylout=============================================
winDir=os.getcwd()
rootPath=os.getcwd();
drviPath=mPath.getDRVIPath()
sys.path.append(winDir) #添加当前路径到系统目录中
win= tk.Tk()
win.config(bg= "#ddeeee")
win.wm_title('Python APP快速设计工具—DRPython  华中科技大学-何岭松')
sWidth=win.winfo_screenwidth()
sHeight=win.winfo_screenheight()
sWrate=0.7; sHrate=0.7;
wWin=sWidth*sWrate; hWin=sHeight*sHrate
x=(sWidth-wWin)/2; y=(sHeight-hWin)/2
win.geometry("%dx%d+%d+%d" %(wWin,hWin,x,y))
#==CallBack Binding======================================== 
#主窗口点击鼠标插入控件
win.bind('<Configure>',winResize)
win.bind('<ButtonPress-1>',clickInsert)
win.bind('<ButtonRelease-1>',releaseInsert)
win.bind('<ButtonRelease-3>',rightUP)
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
controlParGroup=['' for x in range(0,511)]
controlXML=[None for x in range(0,511)]
probeLineN=0
probLine1=[0 for x in range(0,511)]
probLineS1=['' for x in range(0,511)]
probLineS2=['' for x in range(0,511)]
probLineS11=['' for x in range(0,511)]
probLineS12=['' for x in range(0,511)]
probLineType=[0 for x in range(0,511)]
probeST=0;
probeS1=''
probeS2=''
probeS11=''
probeS12=''
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
menu1.add_command(label="新建布局文件",command=mNew)
menu1.add_command(label="打开 XML 布局文件",command=mOpenFile)
menu1.add_command(label="保存 XML 布局文件",command=mSaveFile)
menu1.add_separator()
menu1.add_command(label="导出标准DRVItk APP框架代码",command=mToPython)
menu1.add_command(label="导出可调节DRVItk APP框架代码",command=mToPython1)
menu1.add_command(label="导出可调节DRVItk APP Class框架代码",command=mToPythonClass)
menu1.add_command(label="导出可调节DRVIpyqt APP Class框架代码",command=mToPyqt)
menu1.add_separator()
menu1.add_command(label="IDLE Python编辑器",command=mEditPython)
menu1.add_separator()
menu1.add_command(label="Python命令行窗口",command=mIDLE)
menu1.add_separator()
menu1.add_command(label="关闭",command=mExit)
menubar.add_cascade(label="文件",menu=menu1)
menu2=tk.Menu(menubar,tearoff=False)
menu2.add_command(label="插入控件模式",command=editControl)
menu2.add_separator()
menu2.add_command(label="删除控件模式",command=delControl)
menu2.add_separator()
menu2.add_command(label="插入信号探针",command=insertProbe1)
menubar.add_cascade(label="编辑",menu=menu2)
menu5=tk.Menu(menubar,tearoff=False)
menu5.add_command(label="色彩代码",command=selColor)
menu5.add_separator()
menu5.add_command(label="COM口列表",command=listCOM)
menubar.add_cascade(label="工具",menu=menu5)
menu3=tk.Menu(menubar,tearoff=False)
menu3.add_command(label="典型信号发生器",command=lambda:typicalXMLScript('典型信号发生器.xml'))
menu3.add_command(label="小电子琴例程",command=lambda:typicalXMLScript('小电子琴例程.xml'))
menu3.add_command(label="音频文件波形和频谱分析",command=lambda:typicalXMLScript('音频文件波形和频谱分析.xml'))
#menu3.add_separator()
#menu3.add_command(label="Python信号分析案例集",command=lambda:typicalScript('DRScriptX.py'))
menubar.add_cascade(label="例程",menu=menu3)
menu4=tk.Menu(menubar,tearoff=False)
menu4.add_command(label="关于",command=mAbout)
menu4.add_separator()
menu4.add_command(label="在线帮助资源",command=mHelp)
menubar.add_cascade(label="关于",menu=menu4)
win.config(menu=menubar)
#==工具条============================================
xBar=tk.Frame(win,highlightbackground = "#666666",highlightthickness=1);
xBar.pack(side=tk.TOP,fill=tk.X)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt1=insertIcon(xBar,drviPath+'\\imgs\\new.png','新建布局文件',tNew)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt2=insertIcon(xBar,drviPath+'\\imgs\\open.png','打开XML布局文件',tOpen)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt3=insertIcon(xBar,drviPath+'\\imgs\\save.png','保存XML布局文件',tSave)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt31=insertIcon(xBar,drviPath+'\\imgs\\xml.png','编辑布局文件',tXML)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt4=insertIcon(xBar,drviPath+'\\imgs\\export.png','导出标准DRVItk APP框架代码',tPython)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt40=insertIcon(xBar,drviPath+'\\imgs\\export1.png','导出可调节DRVItk APP框架代码',tPython1)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt41=insertIcon(xBar,drviPath+'\\imgs\\class.png','导出可调节DRVItk APP Class框架代码',tPythonClass)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt42=insertIcon(xBar,drviPath+'\\imgs\\qt.png','导出可调节DRVIpyqt APP Class框架代码',tPyqt)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bta=insertIcon(xBar,drviPath+'\\imgs\\preview.png','GUI效果预览',tPreview)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt6=insertIcon(xBar,drviPath+'\\imgs\\insert.png','控件插入状态',tEditControl)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt7=insertIcon(xBar,drviPath+'\\imgs\\del.png','控件删除状态',tDelControl)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt77=insertIcon(xBar,drviPath+'\\imgs\\probe.png','插入信号探针',tInsertProbe1)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
bt9=insertIcon(xBar,drviPath+'\\imgs\\color.png','色彩码窗',tColor)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
btc=insertIcon(xBar,drviPath+'\\imgs\\help.png','在线帮助资源',tHelp)
bb=tk.Label(xBar,text=''); bb.pack(side=tk.LEFT)
btd=insertIcon(xBar,drviPath+'\\imgs\\about.png','关于',tAbout)
#==属性表============================================
pt7=tk.Button(xBar,width=6,text="XML")
pt7.pack(side=tk.RIGHT)
pt7.bind("<ButtonRelease-1>",blockXML)
pt6=tk.Entry(xBar,width=6)
pt6.pack(side=tk.RIGHT)
pt6.bind("<Return>",setControlls)
bb=tk.Label(xBar,text='  高度'); bb.pack(side=tk.RIGHT)
pt5=tk.Entry(xBar,width=6)
pt5.pack(side=tk.RIGHT)
pt5.bind("<Return>",setControlls)
bb=tk.Label(xBar,text='  宽度'); bb.pack(side=tk.RIGHT)
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
bb=tk.Label(xBar,text='   标题'); bb.pack(side=tk.RIGHT)
setProtiesWin(0)

#==状态条============================================
tbar2=tk.Frame(win,highlightbackground = "#666666", highlightthickness=1);
tbar2.pack(side=tk.BOTTOM,fill=tk.X)
statusbar1 = tk.Label(tbar2,text="____插入状态____", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar1.pack(side=tk.LEFT, fill=tk.X)
statusbar = tk.Label(tbar2,text="    就绪  …", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.LEFT, fill=tk.X)

#==左侧控件窗============================================
ttt=ttk.Style()
ttt.theme_use('clam')
ttt.configure('Treeview.Heading', background="grey",foreground='white')
tbar0=tk.Frame(win,bg='#cccccc',highlightbackground ="#666666", highlightthickness=1);
tbar0.pack(side=tk.RIGHT,fill=tk.Y)
tbar01= tk.Frame(tbar0,width=120,height=28)
tbar01.pack(side=tk.BOTTOM)
mimport=tk.Button(tbar01,bg='#666666',fg='#ffffff',font='bold',text="import")
mimport.place(x=0,y=0,width=110,height=26)
mimport.bind("<Button-1>",importWin)
tvItem = ttk.Treeview(tbar0)
tvItem.column('#0',  anchor=tk.SW, width=120)
tvItem.heading('#0', text='DRVI控件', anchor=tk.SW) 
k=setTreeItem(tvItem,0,'=常用控件==');
k=setTreeItem(tvItem,k,'Button');    k=setTreeItem(tvItem,k,'Entry');
k=setTreeItem(tvItem,k,'Label');     k=setTreeItem(tvItem,k,'Plot');
k=setTreeItem(tvItem,k,'Generator'); k=setTreeItem(tvItem,k,'Recorder');
k=setTreeItem(tvItem,k,'Play');      k=setTreeItem(tvItem,k,'Spectrum');
k=setTreeItem(tvItem,k,'=GUI控件==');
k=setTreeItem(tvItem,k,'Button');        k=setTreeItem(tvItem,k,'Switch');
k=setTreeItem(tvItem,k,'FileBut');
k=setTreeItem(tvItem,k,'GButton');       k=setTreeItem(tvItem,k,'IconButton');
k=setTreeItem(tvItem,k,'HBGroup');       k=setTreeItem(tvItem,k,'VBGroup');
k=setTreeItem(tvItem,k,'Entry');         k=setTreeItem(tvItem,k,'Label');
k=setTreeItem(tvItem,k,'Text');          
k=setTreeItem(tvItem,k,'RadioBut');      k=setTreeItem(tvItem,k,'HRadioBut');
k=setTreeItem(tvItem,k,'CheckBut');      k=setTreeItem(tvItem,k,'HCheckBut');
k=setTreeItem(tvItem,k,'ListBox');       k=setTreeItem(tvItem,k,'Combobox');
k=setTreeItem(tvItem,k,'OptionMenu');    k=setTreeItem(tvItem,k,'SpinBox');
k=setTreeItem(tvItem,k,'Knob');          k=setTreeItem(tvItem,k,'GKnob');
k=setTreeItem(tvItem,k,'HScale');        k=setTreeItem(tvItem,k,'VScale');
k=setTreeItem(tvItem,k,'HSlider');       k=setTreeItem(tvItem,k,'VSlider');
k=setTreeItem(tvItem,k,'Progress');      k=setTreeItem(tvItem,k,'VProgress');
k=setTreeItem(tvItem,k,'Ruler');         k=setTreeItem(tvItem,k,'HRuler');
k=setTreeItem(tvItem,k,'Gauge');         k=setTreeItem(tvItem,k,'Lamp');
k=setTreeItem(tvItem,k,'Digital');       k=setTreeItem(tvItem,k,'List');
k=setTreeItem(tvItem,k,'NoteBook');      k=setTreeItem(tvItem,k,'Tab_Tk');
k=setTreeItem(tvItem,k,'=绘图控件==');
#hls意义不大 k=setTreeItem(tvItem,k,'PlotFast');
k=setTreeItem(tvItem,k,'Figure');
k=setTreeItem(tvItem,k,'Plot');         k=setTreeItem(tvItem,k,'Stem');
k=setTreeItem(tvItem,k,'SemilogX');     k=setTreeItem(tvItem,k,'SemilogY');
k=setTreeItem(tvItem,k,'LogLog');       k=setTreeItem(tvItem,k,'PlotBar');
k=setTreeItem(tvItem,k,'Scatter');      k=setTreeItem(tvItem,k,'PlotPie');
k=setTreeItem(tvItem,k,'PlotPolar');    k=setTreeItem(tvItem,k,'Plot3D');
k=setTreeItem(tvItem,k,'PlotSurf');     k=setTreeItem(tvItem,k,'PlotContour');
k=setTreeItem(tvItem,k,'SubPlot');      k=setTreeItem(tvItem,k,'Monitor');
k=setTreeItem(tvItem,k,'Colormesh');
k=setTreeItem(tvItem,k,'waterFall');
k=setTreeItem(tvItem,k,'CormeshR_qt');
k=setTreeItem(tvItem,k,'WatFallR_qt');
k=setTreeItem(tvItem,k,'Image');        k=setTreeItem(tvItem,k,'SubImages');
k=setTreeItem(tvItem,k,'=信号源====');
k=setTreeItem(tvItem,k,'Generator');   k=setTreeItem(tvItem,k,'Tester');
k=setTreeItem(tvItem,k,'Recorder');    k=setTreeItem(tvItem,k,'Play');
k=setTreeItem(tvItem,k,'PlayX');       k=setTreeItem(tvItem,k,'Timer');
k=setTreeItem(tvItem,k,'CameraCV');    k=setTreeItem(tvItem,k,'VideoCV');
k=setTreeItem(tvItem,k,'Arduino');     k=setTreeItem(tvItem,k,'ADALM2K');
k=setTreeItem(tvItem,k,'=信号分析==');
k=setTreeItem(tvItem,k,'WavePar');     k=setTreeItem(tvItem,k,'Spectrum');
k=setTreeItem(tvItem,k,'Spectgram');   k=setTreeItem(tvItem,k,'PdfCdf');
k=setTreeItem(tvItem,k,'Correlate');   k=setTreeItem(tvItem,k,'Filter');
k=setTreeItem(tvItem,k,'=脚本控件==');
k=setTreeItem(tvItem,k,'Script');
k=setTreeItem(tvItem,k,'=自定义函数==');
k=setTreeItem(tvItem,k,'userSingle');  k=setTreeItem(tvItem,k,'userString');
k=setTreeItem(tvItem,k,'userArrayTwo');k=setTreeItem(tvItem,k,'userArrayTwoX');
k=setTreeItem(tvItem,k,'userArrayTri');k=setTreeItem(tvItem,k,'userImage');
k=setTreeItem(tvItem,k,'==========');
tvScroll1 = ttk.Scrollbar(tbar0, orient='vertical',command=tvItem.yview)
tvScroll1.pack(side=tk.RIGHT, fill=tk.Y)
tvItem.configure(yscrollcommand=tvScroll1.set)
tvItem.pack(side=tk.RIGHT,fill=tk.Y)
tvItem.bind('<<TreeviewSelect>>', gettvID)
tvItem.bind('<ButtonRelease-1>',tvmouseUP)
tvItem.bind('<ButtonRelease-3>',tvmouseRightUP)
tvItem.selection_set(0)
#可绘线条的底图
myCanvas=tk.Canvas(win,bg=win.cget('bg'),highlightthickness=0)
myCanvas.pack(fill='both',expand=1)
drawBLine(myCanvas)
drawLogo(myCanvas)
mFirst=0
#myCanvas.delete(a)    
#========================
xmlParser=code.DRVIParser();
mImport=code.getimport1();
mXML="";
mSTR=""
#==Main Start============================================
win.mainloop()
#==Main Stop============================================
