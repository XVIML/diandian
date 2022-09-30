""#line:45
import drvi .drviAppendPath as mPath #line:49
mPath .appendPythonPath ()#line:50
import os #line:53
import sys #line:54
import os .path #line:55
import tkinter as tk #line:56
import tkinter .ttk as ttk #line:57
import tkinter .messagebox as msgbox #line:58
from tkinter import filedialog #line:59
from tkinter import colorchooser #line:60
from scipy .fftpack import fft ,ifft #line:61
import matplotlib .pyplot as plt #line:62
from pylab import mpl #line:63
from matplotlib import cm #line:64
import numpy as np #line:65
import drvi .drviControlls as dr #line:66
from drvi import drColorWin as colorWin #line:67
def insertIcon (OOOOOO0O00000OOOO ,OO00O0000OO00OO00 ,OOO0000OOO00000O0 ,O0OO0OOOOO0OO0OOO ):#line:71
 O0O0OO0O00OOO0O0O =tk .PhotoImage (file =OO00O0000OO00OO00 )#line:72
 OOOOOOOOO00O0OO00 =tk .Label (OOOOOO0O00000OOOO ,image =O0O0OO0O00OOO0O0O )#line:73
 OOOOOOOOO00O0OO00 .pack (side =tk .LEFT )#line:74
 OOOOOOOOO00O0OO00 .bind ('<Button-1>',O0OO0OOOOO0OO0OOO )#line:75
 OOOOOOOOO00O0OO00 .bind ('<Motion>',O0OO0OOOOO0OO0OOO )#line:76
 OOOOOO0O00O0O0O00 =dr .ToolTip (OOOOOOOOO00O0OO00 ,OOO0000OOO00000O0 )#line:77
 return OOOOOOOOO00O0OO00 ,O0O0OO0O00OOO0O0O #line:78
def tNew (O00O00OO0O00OO00O ):#line:81
    if O00O00OO0O00OO00O .num ==1 :mNew ();return ;#line:82
def mNew ():#line:84
    O0O0OO0O00O0O00OO =msgbox .askyesno ('确认操作','该操作将删除所有已布局的控件 ？')#line:85
    if O0O0OO0O00O0O00OO ==False :return 1 #line:86
    mTxt .delete ("1.0",'end')#line:87
def tOpen (OO0000OO00OO00000 ):#line:89
    if OO0000OO00OO00000 .num ==1 :mOpen ();return ;#line:90
def mOpen ():#line:92
    OO0OOO000O0000OOO =msgbox .askyesno ('确认操作','该操作将删除所有已布局的控件 ？')#line:93
    if OO0OOO000O0000OOO ==False :return 1 #line:94
    mTxt .delete ("1.0",'end')#line:95
    O0000OO0O0000OOO0 =filedialog .askopenfilename (title ="选择文件",filetypes =(("py files","*.py"),("all files","*.*")))#line:96
    if not O0000OO0O0000OOO0 :return 1 #line:97
    OO00O000O0O0OOOO0 =open (O0000OO0O0000OOO0 ,"r",encoding ='utf-8')#line:98
    OOOO0OOOO0O0OOO00 =OO00O000O0O0OOOO0 .read ()#line:99
    OO00O000O0O0OOOO0 .close ()#line:100
    mTxt .insert ("1.0",OOOO0OOOO0O0OOO00 )#line:101
def tSave (OO00O0000O00OO0OO ):#line:103
    if OO00O0000O00OO0OO .num ==1 :mSave ();return ;#line:104
def mSave ():#line:106
    OO00OO0OO000O0OOO =filedialog .asksaveasfile (title ="选择文件",defaultextension =".py",initialfile ="Untitled.py",filetypes =(("py files","*.py"),("all files","*.*")))#line:107
    if not OO00OO0OO000O0OOO :return 1 #line:108
    O0OOOOO0O00O0OO00 =mTxt .get (1.0 ,"end-1c")#line:109
    O000O00OOO0000000 =open (OO00OO0OO000O0OOO .name ,"w",encoding ="utf-8")#line:110
    O000O00OOO0000000 .write (O0OOOOO0O00O0OO00 )#line:111
    O000O00OOO0000000 .close ()#line:112
def mExit ():#line:114
 win .destroy ()#line:115
def mAbout ():#line:117
 msgbox .askyesno (title ='关于...',message ='DRSignal\nVersion 1.00\n设计：何岭松\n华中科技大学')#line:118
def Logo ():#line:121
 OOO00OO00O00OO0OO ='#\n'#line:122
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:123
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:124
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:125
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:126
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      ### ##   ### ##    ## ##    ## ##   ### ##     ####   ### ##   #### ##\n'#line:127
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#       ##  ##   ##  ##  ##   ##  ##   ##   ##  ##     ##     ##  ##  # ## ##  \n'#line:128
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#       ##  ##   ##  ##  ####     ##        ##  ##     ##     ##  ##    ## \n'#line:129
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#       ##  ##   ## ##    #####   ##        ## ##      ##     ##  ##    ##  \n'#line:130
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#       ##  ##   ## ##       ###  ##        ## ##      ##     ## ##     ##  \n'#line:131
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#       ##  ##   ##  ##  ##   ##  ##   ##   ##  ##     ##     ##        ##  \n'#line:132
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      ### ##   #### ##   ## ##    ## ##   #### ##    ####   ####      ####   \n'#line:133
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:134
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:135
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:136
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:137
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:138
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      DRScript是一个Python脚本文件编辑器，主要用于不需要GUI界面的简单程序调试。\n'#line:139
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:140
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      用户在代码窗中直接写入代码，然后点击工具条中的运行键即可。\n'#line:141
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:142
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      程序中集成了四个曲线控件，可以用Plot1、Plot2、Plot3和Plot4命令在窗口中绘制曲线\n'#line:143
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:144
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      具体用法可参考样例程序。\n'#line:145
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:146
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      另外，也可以直接用Matplotlib函数，以弹出窗口形式绘制曲线。\n'#line:147
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:148
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:149
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:150
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:151
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:152
 OOO00OO00O00OO0OO =OOO00OO00O00OO0OO +'#      \n'#line:153
 return OOO00OO00O00OO0OO #line:154
def mDemo ():#line:156
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:157
    global mynote ,win1 ,win2 ;#line:158
    xCurve =3 ;#line:159
    sVar1 .set (sList1 [0 ]);xType1 =1 ;#line:160
    sVar2 .set (sList2 [0 ]);xType2 =1 ;#line:161
    sVar3 .set (sList3 [3 ]);xType3 =4 ;#line:162
    sVar4 .set (sList3 [4 ]);xType4 =5 ;#line:163
    mType ()#line:164
    O0O00OO000O0O0000 ='Fs=44100;\nN=2000;\n'#line:165
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'dt=1.0/Fs\n'#line:166
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'t=np.arange(N)*dt\n'#line:167
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'x1=np.sin(2*np.pi*400*t)\n'#line:168
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'x2=0.5*np.sin(2*np.pi*2000*t)\n'#line:169
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'Plot1.setValue2D(t,x1)\n'#line:170
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'Plot2.setValue2D(t,x1+x2)\n'#line:171
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'f=np.arange(int(N/2))*Fs/N;\n'#line:172
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'y2=np.abs(fft(x1+x2))\n'#line:173
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'a2=2*y2[:int(N/2)]/N\n'#line:174
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'Plot3.setValue2D(f,a2)\n'#line:175
    O0O00OO000O0O0000 =O0O00OO000O0O0000 +'Plot4.setValue2D(f,a2)\n'#line:176
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",O0O00OO000O0O0000 );#line:177
    mynote .select (win1 )#line:178
def mPlot ():#line:180
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:181
    global mynote ,win1 ,win2 ;#line:182
    xCurve =1 #line:183
    sVar1 .set (sList1 [0 ]);xType1 =1 ;mType ()#line:184
    OO0O0OOOOOOOO00O0 ='Fs=44100;\nN=2000;\n'#line:185
    OO0O0OOOOOOOO00O0 =OO0O0OOOOOOOO00O0 +'dt=1.0/Fs\n'#line:186
    OO0O0OOOOOOOO00O0 =OO0O0OOOOOOOO00O0 +'t=np.arange(N)*dt\n'#line:187
    OO0O0OOOOOOOO00O0 =OO0O0OOOOOOOO00O0 +'x1=np.sin(2*np.pi*400*t)\n'#line:188
    OO0O0OOOOOOOO00O0 =OO0O0OOOOOOOO00O0 +'Plot1.setValue2D(t,x1)\n'#line:189
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",OO0O0OOOOOOOO00O0 );#line:190
    mynote .select (win1 )#line:191
def mStem ():#line:193
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:194
    global mynote ,win1 ,win2 ;#line:195
    xCurve =1 #line:196
    sVar1 .set (sList1 [1 ]);xType1 =2 ;mType ()#line:197
    O0OO0O0000OOOOOO0 ='Fs=44100;\nN=2000;\n'#line:198
    O0OO0O0000OOOOOO0 =O0OO0O0000OOOOOO0 +'dt=1.0/Fs\n'#line:199
    O0OO0O0000OOOOOO0 =O0OO0O0000OOOOOO0 +'t=np.arange(N)*dt\n'#line:200
    O0OO0O0000OOOOOO0 =O0OO0O0000OOOOOO0 +'x1=np.sin(2*np.pi*100*t)\n'#line:201
    O0OO0O0000OOOOOO0 =O0OO0O0000OOOOOO0 +'Plot1.setValue2D(t,x1)\n'#line:202
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",O0OO0O0000OOOOOO0 );#line:203
    mynote .select (win1 )#line:204
def mSemilogX ():#line:206
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:207
    global mynote ,win1 ,win2 ;#line:208
    xCurve =1 #line:209
    sVar1 .set (sList1 [2 ]);xType1 =3 ;mType ()#line:210
    O0O00O0OO0000OOOO ='Fs=44100;\nN=2000;\n'#line:211
    O0O00O0OO0000OOOO =O0O00O0OO0000OOOO +'dt=1.0/Fs\n'#line:212
    O0O00O0OO0000OOOO =O0O00O0OO0000OOOO +'t=np.arange(N)*dt\n'#line:213
    O0O00O0OO0000OOOO =O0O00O0OO0000OOOO +'x1=np.sin(2*np.pi*100*t)\n'#line:214
    O0O00O0OO0000OOOO =O0O00O0OO0000OOOO +'Plot1.setValue2D(t,x1)\n'#line:215
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",O0O00O0OO0000OOOO );#line:216
    mynote .select (win1 )#line:217
def mSemilogY ():#line:219
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:220
    global mynote ,win1 ,win2 ;#line:221
    xCurve =1 #line:222
    sVar1 .set (sList1 [3 ]);xType1 =4 ;mType ()#line:223
    O00O0000OOOOOOO00 ='Fs=44100;\nN=2000;\n'#line:224
    O00O0000OOOOOOO00 =O00O0000OOOOOOO00 +'dt=1.0/Fs\n'#line:225
    O00O0000OOOOOOO00 =O00O0000OOOOOOO00 +'t=np.arange(N)*dt\n'#line:226
    O00O0000OOOOOOO00 =O00O0000OOOOOOO00 +'x1=np.sin(2*np.pi*100*t)\n'#line:227
    O00O0000OOOOOOO00 =O00O0000OOOOOOO00 +'x2=0.5*np.sin(2*np.pi*2000*t)\n'#line:228
    O00O0000OOOOOOO00 =O00O0000OOOOOOO00 +'f=np.arange(int(N/2))*Fs/N;\n'#line:229
    O00O0000OOOOOOO00 =O00O0000OOOOOOO00 +'y2=np.abs(fft(x1+x2))\n'#line:230
    O00O0000OOOOOOO00 =O00O0000OOOOOOO00 +'a2=2*y2[:int(N/2)]/N\n'#line:231
    O00O0000OOOOOOO00 =O00O0000OOOOOOO00 +'Plot1.setValue2D(f,a2)\n'#line:232
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",O00O0000OOOOOOO00 );#line:233
    mynote .select (win1 )#line:234
def mLoglog ():#line:236
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:237
    global mynote ,win1 ,win2 ;#line:238
    xCurve =1 #line:239
    sVar1 .set (sList1 [4 ]);xType1 =5 ;mType ()#line:240
    OO0OOO000O000O000 ='Fs=44100;\nN=2000;\n'#line:241
    OO0OOO000O000O000 =OO0OOO000O000O000 +'dt=1.0/Fs\n'#line:242
    OO0OOO000O000O000 =OO0OOO000O000O000 +'t=np.arange(N)*dt\n'#line:243
    OO0OOO000O000O000 =OO0OOO000O000O000 +'x1=np.sin(2*np.pi*100*t)\n'#line:244
    OO0OOO000O000O000 =OO0OOO000O000O000 +'x2=0.5*np.sin(2*np.pi*2000*t)\n'#line:245
    OO0OOO000O000O000 =OO0OOO000O000O000 +'f=np.arange(int(N/2))*Fs/N;\n'#line:246
    OO0OOO000O000O000 =OO0OOO000O000O000 +'y2=np.abs(fft(x1+x2))\n'#line:247
    OO0OOO000O000O000 =OO0OOO000O000O000 +'a2=2*y2[:int(N/2)]/N\n'#line:248
    OO0OOO000O000O000 =OO0OOO000O000O000 +'Plot1.setValue2D(f,a2)\n'#line:249
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",OO0OOO000O000O000 );#line:250
    mynote .select (win1 )#line:251
def mPlotBar ():#line:253
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:254
    global mynote ,win1 ,win2 ;#line:255
    xCurve =1 #line:256
    sVar1 .set (sList1 [5 ]);xType1 =6 ;mType ()#line:257
    OOO0000OOO0O00O0O ='x=np.arange(16)\n'#line:258
    OOO0000OOO0O00O0O =OOO0000OOO0O00O0O +'y=[1,1,1,6,10,30,25,15,20,11,13,11,6,1,1,1]\n'#line:259
    OOO0000OOO0O00O0O =OOO0000OOO0O00O0O +'Plot1.setValue2D(x,y)\n'#line:260
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",OOO0000OOO0O00O0O );#line:261
    mynote .select (win1 )#line:262
def mPlotPie ():#line:264
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:265
    global mynote ,win1 ,win2 ;#line:266
    xCurve =1 #line:267
    sVar1 .set (sList1 [6 ]);xType1 =7 ;mType ()#line:268
    O0000O00O000OOOO0 ='title=["A","B","C","D","E","F","G","H"]\n'#line:269
    O0000O00O000OOOO0 =O0000O00O000OOOO0 +'data=[12 ,17 ,35 ,29 ,12 ,41 ,30 ,20]\n'#line:270
    O0000O00O000OOOO0 =O0000O00O000OOOO0 +'Plot1.setValue2D(title,data)\n'#line:271
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",O0000O00O000OOOO0 );#line:272
    mynote .select (win1 )#line:273
def mPlotPolar ():#line:275
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:276
    global mynote ,win1 ,win2 ;#line:277
    xCurve =1 #line:278
    sVar1 .set (sList1 [7 ]);xType1 =8 ;mType ()#line:279
    OO00000O00000O0OO ='mAngle=np.arange(0,(2*np.pi),0.01)\n'#line:280
    OO00000O00000O0OO =OO00000O00000O0OO +'mRadius=4+4*np.cos(mAngle)\n'#line:281
    OO00000O00000O0OO =OO00000O00000O0OO +'Plot1.setValue2D(mAngle,mRadius)\n'#line:282
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",OO00000O00000O0OO );#line:283
    mynote .select (win1 )#line:284
def mPlot3D ():#line:286
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:287
    global mynote ,win1 ,win2 ;#line:288
    xCurve =1 #line:289
    sVar1 .set (sList1 [8 ]);xType1 =9 ;mType ()#line:290
    OOO0O00OOOO000000 ='z3d = np.arange(0, 10*np.pi, np.pi/50)\n'#line:291
    OOO0O00OOOO000000 =OOO0O00OOOO000000 +'x3d = np.sin(z3d)\n'#line:292
    OOO0O00OOOO000000 =OOO0O00OOOO000000 +'y3d = np.cos(z3d)\n'#line:293
    OOO0O00OOOO000000 =OOO0O00OOOO000000 +'Plot1.setValue3D(x3d,y3d,z3d)\n'#line:294
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",OOO0O00OOOO000000 );#line:295
    mynote .select (win1 )#line:296
def mPlotSurf ():#line:298
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:299
    global mynote ,win1 ,win2 ;#line:300
    xCurve =1 #line:301
    sVar1 .set (sList1 [9 ]);xType1 =10 ;mType ()#line:302
    O0O00O0OO0O0OO0OO ='x=np.linspace(-14,14,128);\n'#line:303
    O0O00O0OO0O0OO0OO =O0O00O0OO0O0OO0OO +'y=x;\n'#line:304
    O0O00O0OO0O0OO0OO =O0O00O0OO0O0OO0OO +'[xSurf,ySurf]=np.meshgrid(x,y)\n'#line:305
    O0O00O0OO0O0OO0OO =O0O00O0OO0O0OO0OO +'r=np.sqrt(xSurf**2+ySurf**2)\n'#line:306
    O0O00O0OO0O0OO0OO =O0O00O0OO0O0OO0OO +'zSurf=np.sin(r).T/r\n'#line:307
    O0O00O0OO0O0OO0OO =O0O00O0OO0O0OO0OO +'Plot1.setValue3D(xSurf,ySurf,zSurf)\n'#line:308
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",O0O00O0OO0O0OO0OO );#line:309
def mPlotContour ():#line:311
    global xType1 ,xType2 ,xType3 ,xType4 ,xCurve #line:312
    global mynote ,win1 ,win2 ;#line:313
    xCurve =1 #line:314
    sVar1 .set (sList1 [10 ]);xType1 =11 ;mType ()#line:315
    O000000OOOO0000OO ='x=np.linspace(-14,14,128);\n'#line:316
    O000000OOOO0000OO =O000000OOOO0000OO +'y=x;\n'#line:317
    O000000OOOO0000OO =O000000OOOO0000OO +'[xSurf,ySurf]=np.meshgrid(x,y)\n'#line:318
    O000000OOOO0000OO =O000000OOOO0000OO +'r=np.sqrt(xSurf**2+ySurf**2)\n'#line:319
    O000000OOOO0000OO =O000000OOOO0000OO +'zSurf=np.sin(r).T/r\n'#line:320
    O000000OOOO0000OO =O000000OOOO0000OO +'Plot1.setValue3D(xSurf,ySurf,zSurf)\n'#line:321
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",O000000OOOO0000OO );#line:322
    mynote .select (win1 )#line:323
def mMatDemo ():#line:325
    global mynote ,win1 ,win2 ;#line:326
    OO0OO0OOO000O0OO0 ='Fs=44100;\nN=2000;\n'#line:327
    OO0OO0OOO000O0OO0 =OO0OO0OOO000O0OO0 +'dt=1.0/Fs\n'#line:328
    OO0OO0OOO000O0OO0 =OO0OO0OOO000O0OO0 +'t=np.arange(N)*dt\n'#line:329
    OO0OO0OOO000O0OO0 =OO0OO0OOO000O0OO0 +'x1=np.sin(2*np.pi*100*t)\n'#line:330
    OO0OO0OOO000O0OO0 =OO0OO0OOO000O0OO0 +'x2=0.5*np.sin(2*np.pi*250*t)\n'#line:331
    OO0OO0OOO000O0OO0 =OO0OO0OOO000O0OO0 +'plt.plot(t,x1)\n'#line:332
    OO0OO0OOO000O0OO0 =OO0OO0OOO000O0OO0 +'plt.plot(t,x2)\n'#line:333
    OO0OO0OOO000O0OO0 =OO0OO0OOO000O0OO0 +'plt.grid()\n'#line:334
    OO0OO0OOO000O0OO0 =OO0OO0OOO000O0OO0 +'plt.show()\n'#line:335
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",OO0OO0OOO000O0OO0 );#line:336
    mynote .select (win1 )#line:337
def mMatStem ():#line:339
    global mynote ,win1 ,win2 ;#line:340
    O0O0OOO0000O0000O ='Fs=44100;\nN=2000;\n'#line:341
    O0O0OOO0000O0000O =O0O0OOO0000O0000O +'dt=1.0/Fs\n'#line:342
    O0O0OOO0000O0000O =O0O0OOO0000O0000O +'t=np.arange(N)*dt\n'#line:343
    O0O0OOO0000O0000O =O0O0OOO0000O0000O +'x1=np.sin(2*np.pi*100*t)\n'#line:344
    O0O0OOO0000O0000O =O0O0OOO0000O0000O +'plt.stem(t,x1)\n'#line:345
    O0O0OOO0000O0000O =O0O0OOO0000O0000O +'plt.grid()\n'#line:346
    O0O0OOO0000O0000O =O0O0OOO0000O0000O +'plt.show()\n'#line:347
    mTxt .delete ("1.0",'end');mTxt .insert ("1.0",O0O0OOO0000O0000O );#line:348
    mynote .select (win1 )#line:349
def getCode (O0O00O0OOOOO0OOO0 ):#line:352
    if O0O00O0OOOOO0OOO0 =='Plot':return 1 #line:353
    if O0O00O0OOOOO0OOO0 =='Stem':return 2 #line:354
    if O0O00O0OOOOO0OOO0 =='SemilogX':return 3 #line:355
    if O0O00O0OOOOO0OOO0 =='SemilogY':return 4 #line:356
    if O0O00O0OOOOO0OOO0 =='Loglog':return 5 #line:357
    if O0O00O0OOOOO0OOO0 =='PlotBar':return 6 #line:358
    if O0O00O0OOOOO0OOO0 =='PlotPie':return 7 #line:359
    if O0O00O0OOOOO0OOO0 =='PlotPolar':return 8 #line:360
    if O0O00O0OOOOO0OOO0 =='Plot3D':return 9 #line:361
    if O0O00O0OOOOO0OOO0 =='PlotSurf':return 10 #line:362
    if O0O00O0OOOOO0OOO0 =='PlotContour':return 11 #line:363
def getSel1 (OOOOO00O0OOOO0O0O ):#line:365
    global xType1 ,xType2 ,xType3 ,xType4 #line:366
    xType1 =getCode (OOOOO00O0OOOO0O0O );mType ()#line:367
def getSel2 (O0O000OO000000OO0 ):#line:369
    global xType1 ,xType2 ,xType3 ,xType4 #line:370
    xType2 =getCode (O0O000OO000000OO0 );mType ()#line:371
def getSel3 (OOOOO00O0OOOO00O0 ):#line:373
    global xType1 ,xType2 ,xType3 ,xType4 #line:374
    xType3 =getCode (OOOOO00O0OOOO00O0 );mType ()#line:375
def getSel4 (OO0000OO0000OOOO0 ):#line:377
    global xType1 ,xType2 ,xType3 ,xType4 #line:378
    xType4 =getCode (OO0000OO0000OOOO0 );mType ()#line:379
def tP1 (OO0O0OOOOOOO0OOOO ):#line:382
    global xCurve #line:383
    if OO0O0OOOOOOO0OOOO .num !=1 :return ;#line:384
    xCurve =1 ;mType ();#line:385
def tP2 (OOO00O0OOOOO00000 ):#line:387
    global xCurve #line:388
    if OOO00O0OOOOO00000 .num !=1 :return ;#line:389
    xCurve =2 ;mType ();#line:390
def tP4 (OOOOOOOO0OOO0OOO0 ):#line:392
    global xCurve #line:393
    if OOOOOOOO0OOO0OOO0 .num !=1 :return ;#line:394
    xCurve =3 ;mType ();#line:395
def doScript ():#line:397
    global mynote ,win1 ,win2 ;#line:398
    O00OOOOOO00OOOOO0 =mTxt .get (1.0 ,"end-1c")#line:399
    print ('Start...')#line:400
    exec (O00OOOOOO00OOOOO0 )#line:401
    print ('Finished..')#line:402
    mynote .select (win2 )#line:403
def doScript1 ():#line:405
    global mynote ,win1 ,win2 ;#line:406
    O0O0OO0OOO00O0O0O =mTxt .get (1.0 ,"end-1c")#line:407
    print ('Start...')#line:408
    exec (O0O0OO0OOO00O0O0O )#line:409
    print ('Finished..')#line:410
def tRun (O0000OO0O00000O00 ):#line:412
    if O0000OO0O00000O00 .num ==1 :doScript ()#line:413
def tRun1 (O0O00000O00OO0OO0 ):#line:415
    if O0O00000O00OO0OO0 .num ==1 :doScript1 ()#line:416
def mType ():#line:418
    global Plot1 ,Plot2 ,Plot3 ,Plot4 ,xCurve ,wRate ,hRrate ;#line:419
    if isinstance (Plot1 ,int )==False :Plot1 .chart ._tkcanvas .destroy ();Plot1 =1 #line:420
    if isinstance (Plot2 ,int )==False :Plot2 .chart ._tkcanvas .destroy ();Plot2 =2 #line:421
    if isinstance (Plot3 ,int )==False :Plot3 .chart ._tkcanvas .destroy ();Plot3 =3 #line:422
    if isinstance (Plot4 ,int )==False :Plot4 .chart ._tkcanvas .destroy ();Plot4 =4 #line:423
    O0OO0OO0OOOO00OOO =xCurve ;#line:424
    if O0OO0OO0OOOO00OOO ==1 :#line:425
        if xType1 ==1 :Plot1 =dr .DRPlot (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:426
        if xType1 ==2 :Plot1 =dr .DRStem (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:427
        if xType1 ==3 :Plot1 =dr .DRSemilogX (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:428
        if xType1 ==4 :Plot1 =dr .DRSemilogY (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:429
        if xType1 ==5 :Plot1 =dr .DRLoglog (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:430
        if xType1 ==6 :Plot1 =dr .DRPlotBar (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:431
        if xType1 ==7 :Plot1 =dr .DRPlotPie (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 )#line:432
        if xType1 ==8 :Plot1 =dr .DRPlotPolar (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 )#line:433
        if xType1 ==9 :Plot1 =dr .DRPlot3D (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 ,0 )#line:434
        if xType1 ==10 :Plot1 =dr .DRPlotSurface (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 ,0 )#line:435
        if xType1 ==11 :Plot1 =dr .DRPlotContour (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,620 *hRate ,'',0 ,0 ,0 ,64 )#line:436
    if O0OO0OO0OOOO00OOO ==2 :#line:438
        if xType1 ==1 :Plot1 =dr .DRPlot (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:439
        if xType2 ==1 :Plot2 =dr .DRPlot (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:440
        if xType1 ==2 :Plot1 =dr .DRStem (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:441
        if xType2 ==2 :Plot2 =dr .DRStem (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:442
        if xType1 ==3 :Plot1 =dr .DRSemilogX (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:443
        if xType2 ==3 :Plot2 =dr .DRSemilogX (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:444
        if xType1 ==4 :Plot1 =dr .DRSemilogY (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:445
        if xType2 ==4 :Plot2 =dr .DRSemilogY (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:446
        if xType1 ==5 :Plot1 =dr .DRLoglog (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:447
        if xType2 ==5 :Plot2 =dr .DRLoglog (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:448
        if xType1 ==6 :Plot1 =dr .DRPlotBar (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:449
        if xType2 ==6 :Plot2 =dr .DRPlotBar (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:450
        if xType1 ==7 :Plot1 =dr .DRPlotPie (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 )#line:451
        if xType2 ==7 :Plot2 =dr .DRPlotPie (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 )#line:452
        if xType1 ==8 :Plot1 =dr .DRPlotPolar (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 )#line:453
        if xType2 ==8 :Plot2 =dr .DRPlotPolar (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 )#line:454
        if xType1 ==9 :Plot1 =dr .DRPlot3D (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:455
        if xType2 ==9 :Plot2 =dr .DRPlot3D (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:456
        if xType1 ==10 :Plot1 =dr .DRPlotSurface (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:457
        if xType2 ==10 :Plot2 =dr .DRPlotSurface (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:458
        if xType1 ==11 :Plot1 =dr .DRPlotContour (win2 ,20 *wRate ,20 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,64 )#line:459
        if xType2 ==11 :Plot2 =dr .DRPlotContour (win2 ,20 *wRate ,330 *hRate ,1260 *wRate ,310 *hRate ,'',0 ,0 ,0 ,64 )#line:460
    if O0OO0OO0OOOO00OOO ==3 :#line:462
        if xType1 ==1 :Plot1 =dr .DRPlot (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:463
        if xType2 ==1 :Plot2 =dr .DRPlot (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:464
        if xType3 ==1 :Plot3 =dr .DRPlot (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:465
        if xType4 ==1 :Plot4 =dr .DRPlot (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:466
        if xType1 ==2 :Plot1 =dr .DRStem (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:467
        if xType2 ==2 :Plot2 =dr .DRStem (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:468
        if xType3 ==2 :Plot3 =dr .DRStem (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:469
        if xType4 ==2 :Plot4 =dr .DRStem (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:470
        if xType1 ==3 :Plot1 =dr .DRSemilogX (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:471
        if xType2 ==3 :Plot2 =dr .DRSemilogX (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:472
        if xType3 ==3 :Plot3 =dr .DRSemilogX (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:473
        if xType4 ==3 :Plot4 =dr .DRSemilogX (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:474
        if xType1 ==4 :Plot1 =dr .DRSemilogY (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:475
        if xType2 ==4 :Plot2 =dr .DRSemilogY (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:476
        if xType3 ==4 :Plot3 =dr .DRSemilogY (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:477
        if xType4 ==4 :Plot4 =dr .DRSemilogY (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:478
        if xType1 ==5 :Plot1 =dr .DRLoglog (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:479
        if xType2 ==5 :Plot2 =dr .DRLoglog (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:480
        if xType3 ==5 :Plot3 =dr .DRLoglog (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:481
        if xType4 ==5 :Plot4 =dr .DRLoglog (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:482
        if xType1 ==6 :Plot1 =dr .DRPlotBar (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:483
        if xType2 ==6 :Plot2 =dr .DRPlotBar (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:484
        if xType3 ==6 :Plot3 =dr .DRPlotBar (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:485
        if xType4 ==6 :Plot4 =dr .DRPlotBar (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,0 ,0 ,0 )#line:486
        if xType1 ==7 :Plot1 =dr .DRPlotPie (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 )#line:487
        if xType2 ==7 :Plot2 =dr .DRPlotPie (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 )#line:488
        if xType3 ==7 :Plot3 =dr .DRPlotPie (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 )#line:489
        if xType4 ==7 :Plot4 =dr .DRPlotPie (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 )#line:490
        if xType1 ==8 :Plot1 =dr .DRPlotPolar (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 )#line:491
        if xType2 ==8 :Plot2 =dr .DRPlotPolar (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 )#line:492
        if xType3 ==8 :Plot3 =dr .DRPlotPolar (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 )#line:493
        if xType4 ==8 :Plot4 =dr .DRPlotPolar (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 )#line:494
        if xType1 ==9 :Plot1 =dr .DRPlot3D (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:495
        if xType2 ==9 :Plot2 =dr .DRPlot3D (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:496
        if xType3 ==9 :Plot3 =dr .DRPlot3D (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:497
        if xType4 ==9 :Plot4 =dr .DRPlot3D (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:498
        if xType1 ==10 :Plot1 =dr .DRPlotSurface (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:499
        if xType2 ==10 :Plot2 =dr .DRPlotSurface (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:500
        if xType3 ==10 :Plot3 =dr .DRPlotSurface (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:501
        if xType4 ==10 :Plot4 =dr .DRPlotSurface (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 )#line:502
        if xType1 ==11 :Plot1 =dr .DRPlotContour (win2 ,20 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,64 )#line:503
        if xType2 ==11 :Plot2 =dr .DRPlotContour (win2 ,20 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,64 )#line:504
        if xType3 ==11 :Plot3 =dr .DRPlotContour (win2 ,650 *wRate ,20 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,64 )#line:505
        if xType4 ==11 :Plot4 =dr .DRPlotContour (win2 ,650 *wRate ,330 *hRate ,630 *wRate ,310 *hRate ,'',0 ,0 ,0 ,64 )#line:506
winDir =os .getcwd ()#line:509
sys .path .append (winDir )#line:510
win =tk .Tk ()#line:511
win .config (bg ="#ddeeee")#line:512
sWidth =win .winfo_screenwidth ()#line:513
sHeight =win .winfo_screenheight ()#line:514
wRate =0.7 ;hRate =0.7 ;#line:515
ww =sWidth *wRate ;wh =sHeight *hRate #line:516
x =(sWidth -ww )/2 ;y =(sHeight -wh )/2 #line:517
win .geometry ("%dx%d+%d+%d"%(ww ,wh ,x ,y ))#line:518
win .wm_title ('DRScript: Python脚本文件调试工具  --  华中科技大学 何岭松')#line:519
sWOld =1920 #line:521
sHOld =1080 #line:522
sWidth =win .winfo_screenwidth ()#line:523
sHeight =win .winfo_screenheight ()#line:524
wRate =sWidth /sWOld #line:525
hRate =sHeight /sHOld #line:526
menubar =tk .Menu (win )#line:529
menu1 =tk .Menu (menubar ,tearoff =False )#line:530
menu1 .add_command (label ="新建文件",command =mNew )#line:531
menu1 .add_command (label ="打开文件",command =mOpen )#line:532
menu1 .add_command (label ="保存文件",command =mSave )#line:533
menu1 .add_separator ()#line:534
menu1 .add_command (label ="关闭",command =mExit )#line:535
menubar .add_cascade (label ="文件",menu =menu1 )#line:536
menu2 =tk .Menu (menubar ,tearoff =False )#line:538
menu2 .add_command (label ="DRPlot Demo",command =mDemo )#line:539
menu2 .add_command (label ="DR_Plot",command =mPlot )#line:540
menu2 .add_command (label ="DR_Stem",command =mStem )#line:541
menu2 .add_command (label ="DR_SemilogX",command =mSemilogX )#line:542
menu2 .add_command (label ="DR_SemilogY",command =mSemilogY )#line:543
menu2 .add_command (label ="DR_Loglog",command =mLoglog )#line:544
menu2 .add_command (label ="DR_PlotBar",command =mPlotBar )#line:545
menu2 .add_command (label ="DR_PlotPie",command =mPlotPie )#line:546
menu2 .add_command (label ="DR_PlotPolar",command =mPlotPolar )#line:547
menu2 .add_command (label ="DR_Plot3D",command =mPlot3D )#line:548
menu2 .add_command (label ="DR_PlotSurf",command =mPlotSurf )#line:549
menu2 .add_command (label ="DR_PlotContour",command =mPlotContour )#line:550
menu2 .add_command (label ="MatPlot Demo",command =mMatDemo )#line:551
menu2 .add_command (label ="Stem",command =mMatStem )#line:552
menu2 .add_command (label ="....")#line:553
menubar .add_cascade (label ="样例代码",menu =menu2 )#line:554
menu4 =tk .Menu (menubar ,tearoff =False )#line:556
menu4 .add_command (label ="关于",command =mAbout )#line:557
menubar .add_cascade (label ="关于",menu =menu4 )#line:558
win .config (menu =menubar )#line:560
xBar =tk .Frame (win ,highlightbackground ="#666666",highlightthickness =1 );#line:563
xBar .pack (side =tk .TOP ,fill =tk .X )#line:564
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:565
xt1 =insertIcon (xBar ,winDir +'\\imgs\\new.png','新建布局文件',tNew )#line:566
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:567
xt2 =insertIcon (xBar ,winDir +'\\imgs\\open.png','打开布局文件',tOpen )#line:568
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:569
xt3 =insertIcon (xBar ,winDir +'\\imgs\\save.png','保存布局文件',tSave )#line:570
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:571
xt6 =insertIcon (xBar ,winDir +'\\imgs\\P1.png','单幅曲线',tP1 )#line:572
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:573
xt7 =insertIcon (xBar ,winDir +'\\imgs\\P2.png','双幅曲线',tP2 )#line:574
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:575
xt8 =insertIcon (xBar ,winDir +'\\imgs\\P4.png','四幅曲线',tP4 )#line:576
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:577
xt4 =insertIcon (xBar ,winDir +'\\imgs\\run1.png','运行DRPY脚本',tRun )#line:578
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:579
xt5 =insertIcon (xBar ,winDir +'\\imgs\\run.png','运行PY脚本',tRun1 )#line:580
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:581
sbar =tk .Label (win ,text ="Ready",bd =1 ,relief =tk .SUNKEN ,anchor =tk .W )#line:583
sbar .pack (side =tk .BOTTOM ,fill =tk .X )#line:584
style =ttk .Style ()#line:587
style .theme_use ('default')#line:588
style .configure ('TNotebook.Tab',foreground ='#000000',background ='#ccccff')#line:589
style .configure ('TNotebook',background ='#dddddd')#line:590
style .map ("TNotebook.Tab",background =[("selected",'#ccccff')])#line:591
mynote =ttk .Notebook (win )#line:592
mynote .pack (side =tk .TOP ,fill =tk .BOTH ,expand =True )#line:593
win1 =tk .Frame (win ,highlightthickness =1 ,highlightbackground ='#ccccdd',bg ='#eeeeee')#line:594
mynote .add (win1 ,text ='代码')#line:595
win2 =tk .Frame (win ,highlightthickness =1 ,highlightbackground ='#ccccdd',bg ='#eeeeee')#line:596
mynote .add (win2 ,text ='界面')#line:597
win3 =tk .Frame (win ,highlightthickness =1 ,highlightbackground ='#ccccdd',bg ='#eeeeee')#line:598
mynote .add (win3 ,text ='曲线类型设置')#line:599
tEdit1 =tk .Frame (win1 ,bg ='#eeeeee',highlightbackground ="#aaaaaa",highlightthickness =1 );#line:602
tEdit1 .pack (side =tk .LEFT ,fill =tk .BOTH ,expand =True )#line:603
sBar =tk .Scrollbar (tEdit1 ,orient =tk .VERTICAL )#line:604
mTxt =tk .Text (tEdit1 ,yscrollcommand =sBar .set ,font =(12 ),state ="normal",relief =tk .GROOVE ,height =40 ,width =160 )#line:605
sBar .pack (side =tk .RIGHT ,fill =tk .Y )#line:606
sBar .config (command =mTxt .yview )#line:607
mTxt .pack (side =tk .LEFT )#line:608
colorWin .colorText (mTxt )#line:609
tEdit2 =tk .Frame (win3 ,bg ='#eeeeee',highlightbackground ="#eeeeee",highlightthickness =1 );#line:612
tEdit2 .pack (side =tk .LEFT ,fill =tk .BOTH ,expand =True )#line:613
sMenu ='Plot,Stem,SemilogX,SemilogY,Loglog,PlotBar,PlotPie,PlotPolar,Plot3D,PlotSurf,PlotContour'#line:614
sList1 =sMenu .split (',')#line:615
sVar1 =tk .StringVar ()#line:616
sVar1 .set (sList1 [0 ])#line:617
bb =tk .Label (tEdit2 ,text ='曲线1类型:');#line:618
bb .configure (font =('Arial',11 ))#line:619
bb .place (x =5 ,y =20 ,width =120 ,height =30 )#line:620
axList1 =tk .OptionMenu (tEdit2 ,sVar1 ,*sList1 ,command =getSel1 )#line:621
axList1 .configure (font =('Arial',11 ))#line:622
axList1 .place (x =110 ,y =20 ,width =140 ,height =30 )#line:623
sList2 =sMenu .split (',')#line:625
sVar2 =tk .StringVar ()#line:626
sVar2 .set (sList2 [0 ])#line:627
bb =tk .Label (tEdit2 ,text ='曲线2类型:');#line:628
bb .configure (font =('Arial',11 ))#line:629
bb .place (x =5 ,y =20 +40 ,width =120 ,height =30 )#line:630
axList2 =tk .OptionMenu (tEdit2 ,sVar2 ,*sList2 ,command =getSel2 )#line:631
axList2 .configure (font =('Arial',11 ))#line:632
axList2 .place (x =110 ,y =20 +40 ,width =140 ,height =30 )#line:633
sList3 =sMenu .split (',')#line:635
sVar3 =tk .StringVar ()#line:636
sVar3 .set (sList3 [0 ])#line:637
bb =tk .Label (tEdit2 ,text ='曲线3类型:');#line:638
bb .configure (font =('Arial',11 ))#line:639
bb .place (x =5 ,y =20 +2 *40 ,width =120 ,height =30 )#line:640
axList3 =tk .OptionMenu (tEdit2 ,sVar3 ,*sList3 ,command =getSel3 )#line:641
axList3 .configure (font =('Arial',11 ))#line:642
axList3 .place (x =110 ,y =20 +2 *40 ,width =140 ,height =30 )#line:643
sList4 =sMenu .split (',')#line:645
sVar4 =tk .StringVar ()#line:646
sVar4 .set (sList4 [0 ])#line:647
bb =tk .Label (tEdit2 ,text ='曲线4类型:');#line:648
bb .configure (font =('Arial',11 ))#line:649
bb .place (x =5 ,y =20 +3 *40 ,width =120 ,height =30 )#line:650
axList4 =tk .OptionMenu (tEdit2 ,sVar4 ,*sList4 ,command =getSel4 )#line:651
axList4 .configure (font =('Arial',11 ))#line:652
axList4 .place (x =110 ,y =20 +3 *40 ,width =140 ,height =30 )#line:653
xCurve =1 ;#line:656
xType1 =1 ;xType2 =1 ;xType3 =1 ;xType4 =1 #line:657
Plot1 =0 ;Plot2 =0 ;Plot3 =0 ;Plot4 =0 #line:658
mType ()#line:659
S =Logo ()#line:660
mTxt .insert ("1.0",S )#line:661
win .mainloop ()#line:664
