""#line:45
import os #line:47
import sys #line:48
import os .path #line:49
idlelib_dir =os .path .dirname (os .path .dirname (os .path .abspath (__file__ )))#line:51
if idlelib_dir not in sys .path :sys .path .insert (0 ,idlelib_dir )#line:52
from idlelib import editor #line:53
from idlelib .pyshell import main as IDLE #line:54
import drvi .drviAppendPath as mPath #line:56
mPath .appendPythonPath ()#line:57
import threading #line:60
from decimal import Decimal #line:61
import re #line:62
import os #line:63
import tkinter as tk #line:64
import tkinter .ttk as ttk #line:65
import numpy as np #line:66
import math #line:67
import base64 #line:68
from tkinter import colorchooser #line:69
import tkinter .messagebox as msgbox #line:70
from tkinter import filedialog #line:71
import numpy as np #line:72
import subprocess #line:73
import drvi .drviControlls as dr #line:74
import drvi .drviDSP as dsp #line:75
import drvi .drviCodeGenerator as code #line:76
from drvi import drColorWin as colorWin #line:77
import drvi .DRhtml as web1 #line:79
import drvi .drffmpeg as mPlayer #line:80
import serial .tools .list_ports #line:81
def insertIcon (O00O0OO0O0O00O000 ,OOOOOO000O0OOOO00 ,OO0OO00OOO0O0O0OO ,OO0000OOOOO0OO0OO ):#line:84
 OO00O0OOO0O0OOOO0 =tk .PhotoImage (file =OOOOOO000O0OOOO00 )#line:85
 OO0O00OO00OO00000 =tk .Label (O00O0OO0O0O00O000 ,image =OO00O0OOO0O0OOOO0 )#line:86
 OO0O00OO00OO00000 .pack (side =tk .LEFT )#line:87
 OO0O00OO00OO00000 .bind ('<Button-1>',OO0000OOOOO0OO0OO )#line:88
 OO0O00OO00OO00000 .bind ('<Motion>',OO0000OOOOO0OO0OO )#line:89
 OOO0O00OO000O000O =dr .ToolTip (OO0O00OO00OO00000 ,OO0OO00OOO0O0O0OO )#line:90
 return OO0O00OO00OO00000 ,OO00O0OOO0O0OOOO0 #line:91
def signalList ():#line:93
    runBatFile (dsp .getPythonPath (),'DRVIExample_Class.py')#line:94
def arduinoCard ():#line:96
    runBatFile (dsp .getPythonPath (),'DRSerial.py')#line:97
def listCOM ():#line:99
    OO00OO0O0000O00O0 =list (serial .tools .list_ports .comports ())#line:100
    OOO0O0OOOOOOO0OO0 =''#line:101
    for OO00OO0O0O00O0OOO in range (0 ,len (OO00OO0O0000O00O0 )):#line:102
        OOO0O0OOOOOOO0OO0 =OOO0O0OOOOOOO0OO0 +OO00OO0O0000O00O0 [OO00OO0O0O00O0OOO ][0 ]+'  :  '+OO00OO0O0000O00O0 [OO00OO0O0O00O0OOO ][1 ]+'\n'#line:103
    OO00O00000OOO0O00 =msgbox .askyesno ('COM口列表',OOO0O0OOOOOOO0OO0 )#line:104
def mp3ToWav ():#line:107
    global winDir #line:108
    OOO00O0OO00O0O00O =filedialog .askopenfilename (title ="选择文件",filetypes =(("mp3 files","*.mp3"),("all files","*.*")))#line:109
    if not OOO00O0OO00O0O00O :return 1 #line:110
    OO0OO0O000000O00O =OOO00O0OO00O0O00O .replace ('.mp3','.wav');#line:111
    OOOOOO0OOOOOO0O0O =winDir +'\\ffmpeg511'#line:112
    O0OO0O0O0000O0000 =mPlayer .DRffmpeg (OOOOOO0OOOOOO0O0O )#line:113
    O0OO0O0O0000O0000 .getWavFile (OOO00O0OO00O0O00O ,OO0OO0O000000O00O )#line:114
def mp4ToWav ():#line:116
    global winDir #line:117
    O000O00OO00000OO0 =filedialog .askopenfilename (title ="选择文件",filetypes =(("mp4 files","*.mp4"),("all files","*.*")))#line:118
    if not O000O00OO00000OO0 :return 1 #line:119
    O0000OOO0O00O0O0O =O000O00OO00000OO0 .replace ('.mp4','.wav');#line:120
    OOOO000OOO0O00OOO =winDir +'\\ffmpeg511'#line:121
    OOOOO0O0OOOOO0OOO =mPlayer .DRffmpeg (OOOO000OOO0O00OOO )#line:122
    OOOOO0O0OOOOO0OOO .getWavFile (O000O00OO00000OO0 ,O0000OOO0O00O0O0O )#line:123
def mp4Play ():#line:125
    global winDir #line:126
    O0000000OOO0OOO00 =filedialog .askopenfilename (title ="选择文件",filetypes =(("mp4 files","*.mp4"),("all files","*.*")))#line:127
    if not O0000000OOO0OOO00 :return 1 #line:128
    O000000O00000O000 =winDir +'\\ffmpeg511'#line:129
    O0000O0O00O00O000 =mPlayer .DRffmpeg (O000000O00000O000 )#line:130
    O0000O0O00O00O000 .playVideoX (O0000000OOO0OOO00 ,480 ,320 ,0 )#line:131
def mp3Play ():#line:133
    global winDir #line:134
    O0000OO000O0O0O0O =filedialog .askopenfilename (title ="选择文件",filetypes =(("mp3 files","*.mp3"),("all files","*.*")))#line:135
    if not O0000OO000O0O0O0O :return 1 #line:136
    OOOO000OO00OOO0O0 =winDir +'\\ffmpeg511'#line:137
    O0O0O00O000O00O0O =mPlayer .DRffmpeg (OOOO000OO00OOO0O0 )#line:138
    O0O0O00O000O00O0O .playVideoX (O0000OO000O0O0O0O ,480 ,320 ,0 )#line:139
def gettvID (OOO00OOOO0O0O0000 ):#line:142
    global mFirst ,ooo00oooo000000000oo ;#line:143
    mFirst =mFirst +1 ;#line:144
    OO0O0O0OOOO0OOOO0 =ooo00oooo000000000oo .item (OOO00OOOO0O0O0000 .widget .selection (),'text')#line:145
    if OO0O0O0OOOO0OOOO0 =='Button':setInsertControlls (1 )#line:146
    if OO0O0O0OOOO0OOOO0 =='HBGroup':setInsertControlls (101 )#line:147
    if OO0O0O0OOOO0OOOO0 =='VBGroup':setInsertControlls (102 )#line:148
    if OO0O0O0OOOO0OOOO0 =='Label':setInsertControlls (2 )#line:149
    if OO0O0O0OOOO0OOOO0 =='Entry':setInsertControlls (3 )#line:150
    if OO0O0O0OOOO0OOOO0 =='HScale':setInsertControlls (4 )#line:151
    if OO0O0O0OOOO0OOOO0 =='VScale':setInsertControlls (5 )#line:152
    if OO0O0O0OOOO0OOOO0 =='RadioBut':setInsertControlls (6 )#line:153
    if OO0O0O0OOOO0OOOO0 =='CheckBut':setInsertControlls (7 )#line:154
    if OO0O0O0OOOO0OOOO0 =='ListBox':setInsertControlls (8 )#line:155
    if OO0O0O0OOOO0OOOO0 =='Combobox':setInsertControlls (9 )#line:156
    if OO0O0O0OOOO0OOOO0 =='OptionMenu':setInsertControlls (14 )#line:157
    if OO0O0O0OOOO0OOOO0 =='Text':setInsertControlls (10 )#line:158
    if OO0O0O0OOOO0OOOO0 =='SpinBox':setInsertControlls (11 )#line:159
    if OO0O0O0OOOO0OOOO0 =='Progress':setInsertControlls (13 )#line:160
    if OO0O0O0OOOO0OOOO0 =='Switch':setInsertControlls (35 )#line:161
    if OO0O0O0OOOO0OOOO0 =='Knob':setInsertControlls (30 )#line:162
    if OO0O0O0OOOO0OOOO0 =='HSlider':setInsertControlls (32 )#line:163
    if OO0O0O0OOOO0OOOO0 =='VSlider':setInsertControlls (33 )#line:164
    if OO0O0O0OOOO0OOOO0 =='GButton':setInsertControlls (41 )#line:165
    if OO0O0O0OOOO0OOOO0 =='Plot':setInsertControlls (51 )#line:167
    if OO0O0O0OOOO0OOOO0 =='Stem':setInsertControlls (59 )#line:168
    if OO0O0O0OOOO0OOOO0 =='SemilogX':setInsertControlls (60 )#line:169
    if OO0O0O0OOOO0OOOO0 =='SemilogY':setInsertControlls (61 )#line:170
    if OO0O0O0OOOO0OOOO0 =='LogLog':setInsertControlls (62 )#line:171
    if OO0O0O0OOOO0OOOO0 =='PlotBar':setInsertControlls (52 )#line:172
    if OO0O0O0OOOO0OOOO0 =='PlotPie':setInsertControlls (53 )#line:173
    if OO0O0O0OOOO0OOOO0 =='PlotPolar':setInsertControlls (56 )#line:174
    if OO0O0O0OOOO0OOOO0 =='Plot3D':setInsertControlls (54 )#line:175
    if OO0O0O0OOOO0OOOO0 =='PlotSurf':setInsertControlls (55 )#line:176
    if OO0O0O0OOOO0OOOO0 =='PlotContour':setInsertControlls (57 )#line:177
    if OO0O0O0OOOO0OOOO0 =='PlotFast':setInsertControlls (58 )#line:178
    if OO0O0O0OOOO0OOOO0 =='Ruler':setInsertControlls (31 )#line:180
    if OO0O0O0OOOO0OOOO0 =='HRuler':setInsertControlls (40 )#line:181
    if OO0O0O0OOOO0OOOO0 =='Gauge':setInsertControlls (34 )#line:182
    if OO0O0O0OOOO0OOOO0 =='Digital':setInsertControlls (36 )#line:183
    if OO0O0O0OOOO0OOOO0 =='Lamp':setInsertControlls (39 )#line:184
    if OO0O0O0OOOO0OOOO0 =='Tab':setInsertControlls (37 )#line:185
    if OO0O0O0OOOO0OOOO0 =='Info':setInsertControlls (38 )#line:186
    if OO0O0O0OOOO0OOOO0 =='IconButton':setInsertControlls (12 )#line:187
    if OO0O0O0OOOO0OOOO0 =='List':setInsertControlls (42 )#line:189
    if OO0O0O0OOOO0OOOO0 =='Timer':setInsertControlls (70 )#line:190
    if OO0O0O0OOOO0OOOO0 =='Recorder':setInsertControlls (71 )#line:191
    if OO0O0O0OOOO0OOOO0 =='Play':setInsertControlls (72 )#line:192
    if OO0O0O0OOOO0OOOO0 =='ArduinoAD':setInsertControlls (73 )#line:193
    if OO0O0O0OOOO0OOOO0 =='TCPS':setInsertControlls (74 )#line:194
    if OO0O0O0OOOO0OOOO0 =='UDPS':setInsertControlls (75 )#line:195
    if OO0O0O0OOOO0OOOO0 =='UDPBS':setInsertControlls (76 )#line:196
    if OO0O0O0OOOO0OOOO0 =='PlayX':setInsertControlls (77 )#line:197
    return 1 #line:198
def tvmouseRightUP (O00OOO000OOO00O0O ):#line:202
 global ooooooooo000000000oo ,winDir #line:203
 O0OO00OO0OOO00OOO =''#line:204
 O0OO000OOOOOOOOO0 =O00OOO000OOO00O0O .x ;#line:205
 if O0OO000OOOOOOOOO0 <0 :return #line:206
 if ooooooooo000000000oo ==1 :O0OO00OO0OOO00OOO ='Button'#line:207
 if ooooooooo000000000oo ==101 :O0OO00OO0OOO00OOO ='HBGr'#line:208
 if ooooooooo000000000oo ==102 :O0OO00OO0OOO00OOO ='VBGr'#line:209
 if ooooooooo000000000oo ==2 :O0OO00OO0OOO00OOO ='Label'#line:210
 if ooooooooo000000000oo ==3 :O0OO00OO0OOO00OOO ='Entry'#line:211
 if ooooooooo000000000oo ==4 :O0OO00OO0OOO00OOO ='HScale'#line:212
 if ooooooooo000000000oo ==5 :O0OO00OO0OOO00OOO ='VScale'#line:213
 if ooooooooo000000000oo ==6 :O0OO00OO0OOO00OOO ='RadioBut'#line:214
 if ooooooooo000000000oo ==7 :O0OO00OO0OOO00OOO ='CheckBut'#line:215
 if ooooooooo000000000oo ==8 :O0OO00OO0OOO00OOO ='ListBox'#line:216
 if ooooooooo000000000oo ==9 :O0OO00OO0OOO00OOO ='ComboBox'#line:217
 if ooooooooo000000000oo ==10 :O0OO00OO0OOO00OOO ='Text'#line:218
 if ooooooooo000000000oo ==11 :O0OO00OO0OOO00OOO ='SpinBox'#line:219
 if ooooooooo000000000oo ==12 :O0OO00OO0OOO00OOO ='IconButton'#line:220
 if ooooooooo000000000oo ==13 :O0OO00OO0OOO00OOO ='Progress'#line:221
 if ooooooooo000000000oo ==14 :O0OO00OO0OOO00OOO ='OMenu'#line:222
 if ooooooooo000000000oo ==30 :O0OO00OO0OOO00OOO ='Knob'#line:223
 if ooooooooo000000000oo ==31 :O0OO00OO0OOO00OOO ='Ruler'#line:224
 if ooooooooo000000000oo ==32 :O0OO00OO0OOO00OOO ='HSlide'#line:225
 if ooooooooo000000000oo ==33 :O0OO00OO0OOO00OOO ='VSlide'#line:226
 if ooooooooo000000000oo ==34 :O0OO00OO0OOO00OOO ='Gauge'#line:227
 if ooooooooo000000000oo ==35 :O0OO00OO0OOO00OOO ='Switch'#line:228
 if ooooooooo000000000oo ==36 :O0OO00OO0OOO00OOO ='Digital'#line:229
 if ooooooooo000000000oo ==37 :O0OO00OO0OOO00OOO ='Tab'#line:230
 if ooooooooo000000000oo ==38 :O0OO00OO0OOO00OOO ='Info'#line:231
 if ooooooooo000000000oo ==39 :O0OO00OO0OOO00OOO ='Lamp'#line:232
 if ooooooooo000000000oo ==40 :O0OO00OO0OOO00OOO ='HRuler'#line:233
 if ooooooooo000000000oo ==41 :O0OO00OO0OOO00OOO ='GButton'#line:234
 if ooooooooo000000000oo ==42 :O0OO00OO0OOO00OOO ='List'#line:235
 if ooooooooo000000000oo ==51 :O0OO00OO0OOO00OOO ='Plot'#line:236
 if ooooooooo000000000oo ==52 :O0OO00OO0OOO00OOO ='PlotBar'#line:237
 if ooooooooo000000000oo ==53 :O0OO00OO0OOO00OOO ='PlotPie'#line:238
 if ooooooooo000000000oo ==54 :O0OO00OO0OOO00OOO ='Plot3D'#line:239
 if ooooooooo000000000oo ==55 :O0OO00OO0OOO00OOO ='PlotSurf'#line:240
 if ooooooooo000000000oo ==56 :O0OO00OO0OOO00OOO ='PlotPolar'#line:241
 if ooooooooo000000000oo ==57 :O0OO00OO0OOO00OOO ='PlotContour'#line:242
 if ooooooooo000000000oo ==58 :O0OO00OO0OOO00OOO ='PlotFast'#line:243
 if ooooooooo000000000oo ==59 :O0OO00OO0OOO00OOO ='Stem'#line:244
 if ooooooooo000000000oo ==60 :O0OO00OO0OOO00OOO ='SemilogX'#line:245
 if ooooooooo000000000oo ==61 :O0OO00OO0OOO00OOO ='SemilogY'#line:246
 if ooooooooo000000000oo ==62 :O0OO00OO0OOO00OOO ='LogLog'#line:247
 if ooooooooo000000000oo ==70 :O0OO00OO0OOO00OOO ='Timer'#line:248
 if ooooooooo000000000oo ==71 :O0OO00OO0OOO00OOO ='Recorder'#line:249
 if ooooooooo000000000oo ==72 :O0OO00OO0OOO00OOO ='Play'#line:250
 if ooooooooo000000000oo ==73 :O0OO00OO0OOO00OOO ='Arduino'#line:251
 if ooooooooo000000000oo ==74 :O0OO00OO0OOO00OOO ='TCPS'#line:252
 if ooooooooo000000000oo ==75 :O0OO00OO0OOO00OOO ='UDPS'#line:253
 if ooooooooo000000000oo ==76 :O0OO00OO0OOO00OOO ='UDPBS'#line:254
 if ooooooooo000000000oo ==77 :O0OO00OO0OOO00OOO ='PlayX'#line:255
 O0OOO0O000O0OO000 =winDir +'\\html'#line:256
 OOOO0OO0OO000OOO0 =O0OO00OO0OOO00OOO +'.html'#line:257
 OOO00000O000OO0O0 =O0OOO0O000O0OO000 +'\\'+OOOO0OO0OO000OOO0 #line:258
 O00O00OOO000O00OO =os .path .exists (OOO00000O000OO0O0 )#line:259
 if O00O00OOO000O00OO ==False :OOOO0OO0OO000OOO0 ='working.html'#line:260
 web1 .htmlBrowser (980 ,700 ,O0OOO0O000O0OO000 ,OOOO0OO0OO000OOO0 )#line:262
 return #line:263
def tvmouseUP (OOOO00O0OO0O00OOO ):#line:265
 global currentN ,controlN ,ooooooooo000000000oo #line:266
 global ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:267
 OO00O0000OO000000 =OOOO00O0OO0O00OOO .x ;OOO0000OO0OOOO00O =OOOO00O0OO0O00OOO .y #line:268
 if OO00O0000OO000000 >0 :return #line:269
 OO00O0000OO000000 =controlWGroup [0 ]+OO00O0000OO000000 -120 #line:270
 OOO0000OO0OOOO00O =OOO0000OO0OOOO00O +30 #line:271
 controlN =controlN +1 #line:273
 O00OOOOO0O0OOOO0O =0 ;O0O0O000OO000OOOO =0 ;O00OO0OOO00OO0O0O ='';OOO00O0000O00OOOO =''#line:274
 if ooooooooo000000000oo ==1 :#line:275
  OOO0O0OO00O00O000 ='Button'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#00aacc';OOO00O0000O00OOOO ='#eeee00'#line:276
 if ooooooooo000000000oo ==101 :#line:277
  OOO0O0OO00O00O000 ='HBGr'+str (controlN );O00OOOOO0O0OOOO0O =400 ;O0O0O000OO000OOOO =36 ;O00OO0OOO00OO0O0O ='#000000';OOO00O0000O00OOOO ='#ffffff'#line:278
 if ooooooooo000000000oo ==102 :#line:279
  OOO0O0OO00O00O000 ='VBGr'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =128 ;O00OO0OOO00OO0O0O ='#008800';OOO00O0000O00OOOO ='#ffffff'#line:280
 if ooooooooo000000000oo ==2 :#line:281
  OOO0O0OO00O00O000 ='Label'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =30 ;O00OO0OOO00OO0O0O ='#bbeeff';OOO00O0000O00OOOO ='#000000'#line:282
 if ooooooooo000000000oo ==3 :#line:283
  OOO0O0OO00O00O000 ='Entry'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =30 ;O00OO0OOO00OO0O0O ='#ffffff';OOO00O0000O00OOOO ='#000000'#line:284
 if ooooooooo000000000oo ==4 :#line:285
  OOO0O0OO00O00O000 ='HScale'+str (controlN );O00OOOOO0O0OOOO0O =200 ;O0O0O000OO000OOOO =50 ;O00OO0OOO00OO0O0O ='#002266';OOO00O0000O00OOOO ='#000000'#line:286
 if ooooooooo000000000oo ==5 :#line:287
  OOO0O0OO00O00O000 ='VScale'+str (controlN );O00OOOOO0O0OOOO0O =50 ;O0O0O000OO000OOOO =200 ;O00OO0OOO00OO0O0O ='#002266';OOO00O0000O00OOOO ='#000000'#line:288
 if ooooooooo000000000oo ==6 :#line:289
  OOO0O0OO00O00O000 ='RadioBut'+str (controlN );O00OOOOO0O0OOOO0O =120 ;O0O0O000OO000OOOO =100 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#ffffff'#line:290
 if ooooooooo000000000oo ==7 :#line:291
  OOO0O0OO00O00O000 ='CheckBut'+str (controlN );O00OOOOO0O0OOOO0O =120 ;O0O0O000OO000OOOO =30 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#007799'#line:292
 if ooooooooo000000000oo ==8 :#line:293
  OOO0O0OO00O00O000 ='ListBox'+str (controlN );O00OOOOO0O0OOOO0O =140 ;O0O0O000OO000OOOO =100 ;O00OO0OOO00OO0O0O ='#ddffdd';OOO00O0000O00OOOO ='#000000'#line:294
 if ooooooooo000000000oo ==9 :#line:295
  OOO0O0OO00O00O000 ='ComboBox'+str (controlN );O00OOOOO0O0OOOO0O =120 ;O0O0O000OO000OOOO =30 ;O00OO0OOO00OO0O0O ='#0099aa';OOO00O0000O00OOOO ='#ffffff'#line:296
 if ooooooooo000000000oo ==10 :#line:297
  OOO0O0OO00O00O000 ='Text'+str (controlN );O00OOOOO0O0OOOO0O =120 ;O0O0O000OO000OOOO =100 ;O00OO0OOO00OO0O0O ='#ffffff';OOO00O0000O00OOOO ='#000000'#line:298
 if ooooooooo000000000oo ==11 :#line:299
  OOO0O0OO00O00O000 ='SinBox'+str (controlN );O00OOOOO0O0OOOO0O =120 ;O0O0O000OO000OOOO =32 ;O00OO0OOO00OO0O0O ='#ccffcc';OOO00O0000O00OOOO ='#000000'#line:300
 if ooooooooo000000000oo ==12 :#line:301
  OOO0O0OO00O00O000 ='Icon'+str (controlN );O00OOOOO0O0OOOO0O =60 ;O0O0O000OO000OOOO =60 ;O00OO0OOO00OO0O0O ='#ffffff';OOO00O0000O00OOOO ='#000000'#line:302
 if ooooooooo000000000oo ==13 :#line:303
  OOO0O0OO00O00O000 ='Progress'+str (controlN );O00OOOOO0O0OOOO0O =200 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#00dd00';OOO00O0000O00OOOO ='#000000'#line:304
 if ooooooooo000000000oo ==14 :#line:305
  OOO0O0OO00O00O000 ='OMenu'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#00aacc';OOO00O0000O00OOOO ='#eeee00'#line:306
 if ooooooooo000000000oo ==30 :#line:308
  OOO0O0OO00O00O000 ='Knob'+str (controlN );O00OOOOO0O0OOOO0O =120 ;O0O0O000OO000OOOO =120 ;O00OO0OOO00OO0O0O ='#004466';OOO00O0000O00OOOO ='#222222'#line:309
 if ooooooooo000000000oo ==31 :#line:310
  OOO0O0OO00O00O000 ='Ruler'+str (controlN );O00OOOOO0O0OOOO0O =110 ;O0O0O000OO000OOOO =200 ;O00OO0OOO00OO0O0O ='#ffffff';OOO00O0000O00OOOO ='#aaaaaa'#line:311
 if ooooooooo000000000oo ==32 :#line:312
  OOO0O0OO00O00O000 ='HSlider'+str (controlN );O00OOOOO0O0OOOO0O =260 ;O0O0O000OO000OOOO =30 ;O00OO0OOO00OO0O0O ='#444444';OOO00O0000O00OOOO ='#880000'#line:313
 if ooooooooo000000000oo ==33 :#line:314
  OOO0O0OO00O00O000 ='VSlider'+str (controlN );O00OOOOO0O0OOOO0O =30 ;O0O0O000OO000OOOO =260 ;O00OO0OOO00OO0O0O ='#444444';OOO00O0000O00OOOO ='#880000'#line:315
 if ooooooooo000000000oo ==34 :#line:316
  OOO0O0OO00O00O000 ='Gauge'+str (controlN );O00OOOOO0O0OOOO0O =160 ;O0O0O000OO000OOOO =160 ;O00OO0OOO00OO0O0O ='#ffffff';OOO00O0000O00OOOO ='#444444'#line:317
 if ooooooooo000000000oo ==35 :#line:318
  OOO0O0OO00O00O000 ='Switch'+str (controlN );O00OOOOO0O0OOOO0O =80 ;O0O0O000OO000OOOO =36 ;O00OO0OOO00OO0O0O ='#004466';OOO00O0000O00OOOO ='#aaddee'#line:319
 if ooooooooo000000000oo ==36 :#line:320
  OOO0O0OO00O00O000 ='Digital'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =36 ;O00OO0OOO00OO0O0O ='#000000';OOO00O0000O00OOOO ='#00ffaa'#line:321
 if ooooooooo000000000oo ==37 :#line:322
  OOO0O0OO00O00O000 ='Tab'+str (controlN );O00OOOOO0O0OOOO0O =600 ;O0O0O000OO000OOOO =400 ;O00OO0OOO00OO0O0O ='#dddddd';OOO00O0000O00OOOO ='#888888'#line:323
 if ooooooooo000000000oo ==38 :#line:324
  OOO0O0OO00O00O000 ='Info'+str (controlN );O00OOOOO0O0OOOO0O =40 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#00bbbb';OOO00O0000O00OOOO ='#000000'#line:325
 if ooooooooo000000000oo ==39 :#line:326
  OOO0O0OO00O00O000 ='Lamp'+str (controlN );O00OOOOO0O0OOOO0O =60 ;O0O0O000OO000OOOO =60 ;O00OO0OOO00OO0O0O ='#00aa00';OOO00O0000O00OOOO ='#cccc00'#line:327
 if ooooooooo000000000oo ==40 :#line:328
  OOO0O0OO00O00O000 ='HRuler'+str (controlN );O00OOOOO0O0OOOO0O =200 ;O0O0O000OO000OOOO =80 ;O00OO0OOO00OO0O0O ='#eeeeee';OOO00O0000O00OOOO ='#aaaaaa'#line:329
 if ooooooooo000000000oo ==41 :#line:330
  OOO0O0OO00O00O000 ='GButton'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#00ccaa';OOO00O0000O00OOOO ='#eeee00'#line:331
 if ooooooooo000000000oo ==42 :#line:332
  OOO0O0OO00O00O000 ='List'+str (controlN );O00OOOOO0O0OOOO0O =300 ;O0O0O000OO000OOOO =90 ;O00OO0OOO00OO0O0O ='#eeeeff';OOO00O0000O00OOOO ='#000000'#line:333
 if ooooooooo000000000oo ==51 :#line:335
  OOO0O0OO00O00O000 ='Plot'+str (controlN );O00OOOOO0O0OOOO0O =700 ;O0O0O000OO000OOOO =210 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:336
 if ooooooooo000000000oo ==52 :#line:337
  OOO0O0OO00O00O000 ='PlotBar'+str (controlN );O00OOOOO0O0OOOO0O =700 ;O0O0O000OO000OOOO =210 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:338
 if ooooooooo000000000oo ==53 :#line:339
  OOO0O0OO00O00O000 ='PlotPie'+str (controlN );O00OOOOO0O0OOOO0O =300 ;O0O0O000OO000OOOO =300 ;O00OO0OOO00OO0O0O ='#ffffff';OOO00O0000O00OOOO ='#000000'#line:340
 if ooooooooo000000000oo ==54 :#line:341
  OOO0O0OO00O00O000 ='Plot3D'+str (controlN );O00OOOOO0O0OOOO0O =420 ;O0O0O000OO000OOOO =380 ;O00OO0OOO00OO0O0O ='#ffffff';OOO00O0000O00OOOO ='#000000'#line:342
 if ooooooooo000000000oo ==55 :#line:343
  OOO0O0OO00O00O000 ='PlotSurf'+str (controlN );O00OOOOO0O0OOOO0O =500 ;O0O0O000OO000OOOO =380 ;O00OO0OOO00OO0O0O ='#ffffff';OOO00O0000O00OOOO ='#000000'#line:344
 if ooooooooo000000000oo ==56 :#line:345
  OOO0O0OO00O00O000 ='PlotPolar'+str (controlN );O00OOOOO0O0OOOO0O =300 ;O0O0O000OO000OOOO =300 ;O00OO0OOO00OO0O0O ='#005599';OOO00O0000O00OOOO ='#ffffff'#line:346
 if ooooooooo000000000oo ==57 :#line:347
  OOO0O0OO00O00O000 ='PlotContour'+str (controlN );O00OOOOO0O0OOOO0O =640 ;O0O0O000OO000OOOO =480 ;O00OO0OOO00OO0O0O ='#ffffff';OOO00O0000O00OOOO ='#000000'#line:348
 if ooooooooo000000000oo ==58 :#line:349
  OOO0O0OO00O00O000 ='FastPlot'+str (controlN );O00OOOOO0O0OOOO0O =700 ;O0O0O000OO000OOOO =200 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:350
 if ooooooooo000000000oo ==59 :#line:351
  OOO0O0OO00O00O000 ='Stem'+str (controlN );O00OOOOO0O0OOOO0O =700 ;O0O0O000OO000OOOO =210 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:352
 if ooooooooo000000000oo ==60 :#line:353
  OOO0O0OO00O00O000 ='SemilogX'+str (controlN );O00OOOOO0O0OOOO0O =700 ;O0O0O000OO000OOOO =210 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:354
 if ooooooooo000000000oo ==61 :#line:355
  OOO0O0OO00O00O000 ='SemilogY'+str (controlN );O00OOOOO0O0OOOO0O =700 ;O0O0O000OO000OOOO =210 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:356
 if ooooooooo000000000oo ==62 :#line:357
  OOO0O0OO00O00O000 ='LogLog'+str (controlN );O00OOOOO0O0OOOO0O =700 ;O0O0O000OO000OOOO =210 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:358
 if ooooooooo000000000oo ==70 :#line:360
  OOO0O0OO00O00O000 ='Timer'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#00aacc';OOO00O0000O00OOOO ='#eeee00'#line:361
 if ooooooooo000000000oo ==71 :#line:362
  OOO0O0OO00O00O000 ='Recorder'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#00aacc';OOO00O0000O00OOOO ='#eeee00'#line:363
 if ooooooooo000000000oo ==72 :#line:364
  OOO0O0OO00O00O000 ='Player'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#00aacc';OOO00O0000O00OOOO ='#eeee00'#line:365
 if ooooooooo000000000oo ==73 :#line:366
  OOO0O0OO00O00O000 ='Arduino'+str (controlN );O00OOOOO0O0OOOO0O =900 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:367
 if ooooooooo000000000oo ==74 :#line:368
  OOO0O0OO00O00O000 ='TCPS'+str (controlN );O00OOOOO0O0OOOO0O =500 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:369
 if ooooooooo000000000oo ==75 :#line:370
  OOO0O0OO00O00O000 ='UDPS'+str (controlN );O00OOOOO0O0OOOO0O =500 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:371
 if ooooooooo000000000oo ==76 :#line:372
  OOO0O0OO00O00O000 ='UDPBS'+str (controlN );O00OOOOO0O0OOOO0O =500 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#003355';OOO00O0000O00OOOO ='#000000'#line:373
 if ooooooooo000000000oo ==77 :#line:374
  OOO0O0OO00O00O000 ='PlayerX'+str (controlN );O00OOOOO0O0OOOO0O =100 ;O0O0O000OO000OOOO =40 ;O00OO0OOO00OO0O0O ='#00aacc';OOO00O0000O00OOOO ='#eeee00'#line:375
 pushControlPar (controlN ,ooooooooo000000000oo ,1 ,OOO0O0OO00O00O000 ,OO00O0000OO000000 ,OOO0000OO0OOOO00O ,O00OOOOO0O0OOOO0O ,O0O0O000OO000OOOO ,O00OO0OOO00OO0O0O ,OOO00O0000O00OOOO );#line:376
 insertDRControlls (controlN );#line:377
 ooooooooo000000000oo =0 #line:378
 return 1 #line:379
def setProtiesWin (O0OO0OOO00O0O00OO ):#line:382
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:383
 global pt1 ,pt2 ,pt3 ,pt4 ,pt5 ,pt6 ,pt7 ,pt8 #line:384
 OO0OOOO00OO00O00O =controlNameGroup [O0OO0OOO00O0O00OO ];OOO00000000O0OOOO =controlX0Group [O0OO0OOO00O0O00OO ];OOO00OOO00OOOO000 =controlY0Group [O0OO0OOO00O0O00OO ];OO0OO0O00O0O0OOOO =controlWGroup [O0OO0OOO00O0O00OO ];OOO000O0O00O00OOO =controlHGroup [O0OO0OOO00O0O00OO ];O0OOOO00OOO0OOOOO =controlbgGroup [O0OO0OOO00O0O00OO ];OOOO0OO0OOOOO0OOO =controlfgGroup [O0OO0OOO00O0O00OO ]#line:385
 pt2 .delete (0 ,20 );pt2 .insert (0 ,OO0OOOO00OO00O00O )#line:386
 pt3 .delete (0 ,20 );pt3 .insert (0 ,str (OOO00000000O0OOOO ))#line:387
 pt4 .delete (0 ,20 );pt4 .insert (0 ,str (OOO00OOO00OOOO000 ))#line:388
 pt5 .delete (0 ,20 );pt5 .insert (0 ,str (OO0OO0O00O0O0OOOO ))#line:389
 pt6 .delete (0 ,20 );pt6 .insert (0 ,str (OOO000O0O00O00OOO ))#line:390
 pt7 .delete (0 ,20 );pt7 .insert (0 ,O0OOOO00OOO0OOOOO )#line:391
 pt8 .delete (0 ,20 );pt8 .insert (0 ,OOOO0OO0OOOOO0OOO )#line:392
 return 1 #line:393
def posChanged (O0O00OO0O0OO0OOOO ,OO00OOO0OO000OOOO ,OOOOO000OOOOOO0O0 ,OOO0OO000OO000000 ,O00OOO0O00OOOO00O ):#line:396
    global currentN #line:397
    OOO0O00O00OO0O0OO =O0O00OO0O0OO0OOOO ;currentN =O0O00OO0O0OO0OOOO #line:398
    controlX0Group [OOO0O00O00OO0O0OO ]=OO00OOO0OO000OOOO ;controlY0Group [OOO0O00O00OO0O0OO ]=OOOOO000OOOOOO0O0 ;#line:399
    controlWGroup [OOO0O00O00OO0O0OO ]=OOO0OO000OO000000 ;controlHGroup [OOO0O00O00OO0O0OO ]=O00OOO0O00OOOO00O #line:400
    setProtiesWin (OOO0O00O00OO0O0OO )#line:401
    return 1 #line:402
def insertControl (O0OOO0OOO00000000 ,OOO000OOO00O00OO0 ,O000O0OOO00000000 ,O000OOO00OOO0OO00 ,O0O00O0OOO0OO0OOO ,O0O000O00OO0O00O0 ,OOOOOOO0OO0OO0000 ,OO000000O0OOOOOOO ):#line:404
 global currentN #line:405
 O00OOO0O00OOOO0O0 =dr .DRSize (O0OOO0OOO00000000 ,currentN ,OOO000OOO00O00OO0 ,O000O0OOO00000000 ,O000OOO00OOO0OO00 ,O0O00O0OOO0OO0OOO ,O0O000O00OO0O00O0 ,OOOOOOO0OO0OO0000 ,OO000000O0OOOOOOO )#line:406
 O00OOO0O00OOOO0O0 .addCallBackSize (posChanged )#line:407
 return O00OOO0O00OOOO0O0 #line:408
def delAllControls ():#line:411
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:412
 global controlN ;#line:413
 for O00OO0O00O0O00OO0 in range (1 ,500 ):#line:414
  O0O0000OOOO0O000O =controlGroup [O00OO0O00O0O00OO0 ]#line:415
  if O0O0000OOOO0O000O !=0 :#line:416
   O0O0000OOOO0O000O .ax .destroy ();controlGroup [O00OO0O00O0O00OO0 ]=0 ;ooooooooo000000000ooGroup [O00OO0O00O0O00OO0 ]=0 #line:417
 controlN =0 #line:418
 return 1 #line:419
def insertFromFile (O00000O00O0O0O0O0 ):#line:422
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:423
 global controlN ;#line:424
 O00000O00O0O0O0O0 =O00000O00O0O0O0O0 .split ('\n')#line:425
 OO0O0OOO000OO00O0 =int (O00000O00O0O0O0O0 [0 ])#line:426
 if OO0O0OOO000OO00O0 <2 :#line:427
  return 1 #line:428
 for O00OO0000O00OO0OO in range (0 ,OO0O0OOO000OO00O0 ):#line:430
  ooooooooo000000000ooGroup [O00OO0000O00OO0OO ]=int (O00000O00O0O0O0O0 [2 +O00OO0000O00OO0OO *9 ])#line:431
  controlNameGroup [O00OO0000O00OO0OO ]=O00000O00O0O0O0O0 [3 +O00OO0000O00OO0OO *9 ]#line:432
  controlX0Group [O00OO0000O00OO0OO ]=int (O00000O00O0O0O0O0 [4 +O00OO0000O00OO0OO *9 ])#line:433
  controlY0Group [O00OO0000O00OO0OO ]=int (O00000O00O0O0O0O0 [5 +O00OO0000O00OO0OO *9 ])#line:434
  controlWGroup [O00OO0000O00OO0OO ]=int (O00000O00O0O0O0O0 [6 +O00OO0000O00OO0OO *9 ])#line:435
  controlHGroup [O00OO0000O00OO0OO ]=int (O00000O00O0O0O0O0 [7 +O00OO0000O00OO0OO *9 ])#line:436
  controlbgGroup [O00OO0000O00OO0OO ]=O00000O00O0O0O0O0 [8 +O00OO0000O00OO0OO *9 ]#line:437
  controlfgGroup [O00OO0000O00OO0OO ]=O00000O00O0O0O0O0 [9 +O00OO0000O00OO0OO *9 ]#line:438
  if O00OO0000O00OO0OO >0 :insertDRControlls (O00OO0000O00OO0OO );#line:440
 controlN =OO0O0OOO000OO00O0 ;#line:441
 O0O000O0O0OOO00O0 =str (controlWGroup [0 ])+'x'+str (controlHGroup [0 ])#line:443
 win .geometry (O0O000O0O0OOO00O0 )#line:444
 win .config (bg =controlbgGroup [0 ])#line:445
 setProtiesWin (0 )#line:446
 return 1 #line:447
def initAll ():#line:449
    global x0Control ,y0Control ,editStatus ,mouseStatus ,ooooooooo000000000oo ,currentN ,controlN #line:450
    global ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:451
    x0Control =0 ;y0Control =0 ;editStatus =0 ;mouseStatus =0 #line:452
    ooooooooo000000000oo =0 ;currentN =0 ;controlN =0 #line:453
    ooooooooo000000000ooGroup =[0 for O0OO00OOOOOOOO0O0 in range (0 ,511 )]#line:454
    controlGroup =[0 for O00OO000OO00OO0OO in range (0 ,511 )]#line:455
    controlNameGroup =['A'for O00O0OOOOO0O00000 in range (0 ,511 )]#line:456
    controlX0Group =[0 for O0OOO0OO0OO0O00OO in range (0 ,511 )]#line:457
    controlY0Group =[0 for O000O000O00OO00OO in range (0 ,511 )]#line:458
    controlWGroup =[0 for O00OO0O0O00OOO000 in range (0 ,511 )]#line:459
    controlHGroup =[0 for OO0O00O000OO000O0 in range (0 ,511 )]#line:460
    controlbgGroup =['0'for OO00000O000O00OOO in range (0 ,511 )]#line:461
    controlfgGroup =['0'for OO000O0O00OOOOO0O in range (0 ,511 )]#line:462
    currentN =0 ;ooooooooo000000000ooGroup [0 ]=0 #line:463
    controlGroup [0 ]=win #line:464
    controlNameGroup [0 ]='Main';#line:465
    controlX0Group [0 ]=0 ;#line:466
    controlY0Group [0 ]=0 ;#line:467
    controlWGroup [0 ]=1000 ;#line:468
    controlHGroup [0 ]=600 #line:469
    controlbgGroup [0 ]='#ddeeee'#line:470
    controlfgGroup [0 ]='#000000'#line:471
    return 1 ;#line:472
def tNew (O00OO0OOO0OOO00O0 ):#line:475
    if O00OO0OOO0OOO00O0 .num ==1 :mNew ();return ;#line:476
    oo000000000oo000oo .config (text =' 新建GUI布局文件')#line:477
def mNew ():#line:479
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:480
 [O0OOO0O00OOO0OO00 ,O0O00000OOO0OOO0O ]=code .toScript (ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup )#line:481
 if O0OOO0O00OOO0OO00 >1 :#line:482
  O0OOOOOOO0O0OOO00 =msgbox .askyesno ('确认操作','该操作将删除所有已布局的控件 ？')#line:483
  if O0OOOOOOO0O0OOO00 ==False :#line:484
   return 1 #line:485
 delAllControls ();initAll ();setProtiesWin (0 )#line:486
 return 1 #line:487
def tOpen (OO000O00O0O0OO000 ):#line:490
    if OO000O00O0O0OO000 .num ==1 :mOpen ();return ;#line:491
    oo000000000oo000oo .config (text =' 打开GUI布局TXT文件')#line:492
def mOpen ():#line:494
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:495
 [OO0OO0000O0OO000O ,OO00O000O00OO000O ]=code .toScript (ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup )#line:496
 if OO0OO0000O0OO000O >1 :#line:497
  OO00O00OOOOOO0OO0 =msgbox .askyesno ('确认操作','该操作将删除所有已布局的控件 ？')#line:498
  if OO00O00OOOOOO0OO0 ==False :#line:499
   return 1 #line:500
 delAllControls ();initAll ();setProtiesWin (0 )#line:501
 OOO0O0OO0OOOO0000 =filedialog .askopenfilename (title ="选择文件",filetypes =(("txt files","*.txt"),("all files","*.*")))#line:502
 if not OOO0O0OO0OOOO0000 :#line:503
  return 1 #line:504
 O00O0OOO0O0OOO0O0 =open (OOO0O0OO0OOOO0000 ,"r",encoding ='utf-8')#line:505
 OO00O000O00OO000O =O00O0OOO0O0OOO0O0 .read ()#line:506
 O00O0OOO0O0OOO0O0 .close ()#line:507
 insertFromFile (OO00O000O00OO000O )#line:508
 return 1 #line:509
def tSave (O0O0O0000OO0OO00O ):#line:512
    if O0O0O0000OO0OO00O .num ==1 :mSave ();return ;#line:513
    oo000000000oo000oo .config (text =' 保存当前GUI布局到TXT文件')#line:514
def mSave ():#line:516
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:517
 [OOO0O0OOO00OO00O0 ,OOOOO00OO00000O00 ]=code .toScript (ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup )#line:518
 if OOO0O0OOO00OO00O0 <2 :#line:519
  return 1 #line:520
 O000000O0OOO00OO0 =filedialog .asksaveasfile (title ="选择文件",defaultextension =".txt",initialfile ="Untitled.txt",filetypes =(("txt files","*.txt"),("all files","*.*")))#line:521
 if not O000000O0OOO00OO0 :#line:522
  return 1 #line:523
 O00O000OOO000O0O0 =open (O000000O0OOO00OO0 .name ,"w",encoding ="utf-8")#line:524
 O00O000OOO000O0O0 .write (OOOOO00OO00000O00 )#line:525
 O00O000OOO000O0O0 .close ()#line:526
 return 1 #line:527
def tPython (O0O00O0000O0O00O0 ):#line:530
    if O0O00O0000O0O00O0 .num ==1 :mToPython ();return ;#line:531
    oo000000000oo000oo .config (text =' 导出Python APP代码')#line:532
def mToPython ():#line:534
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:535
 global sWidth ,sHeight #line:536
 [O000O0000000OOOOO ,O000OOO00000OOOOO ]=code .toPythonScriptNew (sWidth ,sHeight ,currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup )#line:537
 if O000O0000000OOOOO <2 :return 1 #line:538
 O0O0O0OOOO00000OO =filedialog .asksaveasfile (title ="选择文件",defaultextension =".py",initialfile ="Untitled.py",filetypes =(("Python files","*.py"),("all files","*.*")))#line:539
 if not O0O0O0OOOO00000OO :return 1 #line:540
 O0O0OO0O00O000O0O =open (O0O0O0OOOO00000OO .name ,"w",encoding ="utf-8")#line:541
 O0O0OO0O00O000O0O .write (O000OOO00000OOOOO )#line:542
 O0O0OO0O00O000O0O .close ()#line:543
 return 1 #line:544
def tPython1 (O0O0OO0000000O0OO ):#line:546
    if O0O0OO0000000O0OO .num ==1 :mToPython1 ();return ;#line:547
    oo000000000oo000oo .config (text =' 导出比例布局Python APP代码')#line:548
def mToPython1 ():#line:550
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:551
 global sWidth ,sHeight #line:552
 [OO000O0000O0O0OO0 ,OO0OOO0O0O0O00O0O ]=code .toPythonScriptNew1 (sWidth ,sHeight ,currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup )#line:553
 if OO000O0000O0O0OO0 <2 :return 1 #line:554
 O0OO0O00OOO0O0O00 =filedialog .asksaveasfile (title ="选择文件",defaultextension =".py",initialfile ="Untitled.py",filetypes =(("Python files","*.py"),("all files","*.*")))#line:555
 if not O0OO0O00OOO0O0O00 :return 1 #line:556
 OO0OOO0O0O0O00O0O =OO0OOO0O0O0O00O0O +'#Original Screen Size=========================\n'#line:557
 OO0OOO0O0O0O00O0O =OO0OOO0O0O0O00O0O +'#ScreenWidth='+str (sWidth )+'\n'#line:558
 OO0OOO0O0O0O00O0O =OO0OOO0O0O0O00O0O +'#ScreenHeight='+str (sHeight )+'\n'#line:559
 O0O0O000OO0000O0O =open (O0OO0O00OOO0O0O00 .name ,"w",encoding ="utf-8")#line:560
 O0O0O000OO0000O0O .write (OO0OOO0O0O0O00O0O )#line:561
 O0O0O000OO0000O0O .close ()#line:562
 return 1 #line:563
def tPythonClass (OOO0OOO0O0O000OO0 ):#line:565
    if OOO0OOO0O0O000OO0 .num ==1 :mToPythonClass ();return ;#line:566
    oo000000000oo000oo .config (text =' 导出APP Class代码')#line:567
def mToPythonClass ():#line:569
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:570
 [OOO000O0OO000000O ,OO0000O00OOOOOO00 ]=code .toPythonScriptClass (currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup )#line:571
 if OOO000O0OO000000O <2 :return 1 #line:572
 O0O0O0O00OOO0000O =filedialog .asksaveasfile (title ="选择文件",defaultextension =".py",initialfile ="Untitled.py",filetypes =(("Python files","*.py"),("all files","*.*")))#line:573
 if not O0O0O0O00OOO0000O :#line:574
  return 1 #line:575
 O0O00OOOOO00O000O =open (O0O0O0O00OOO0000O .name ,"w",encoding ="utf-8")#line:576
 O0O00OOOOO00O000O .write (OO0000O00OOOOOO00 )#line:577
 O0O00OOOOO00O000O .close ()#line:578
 return 1 #line:579
def runBatFile (O00OOOOO0OO0OOO0O ,OOO0O0000O00000O0 ):#line:584
 global winDir #line:585
 O0000OOO0OOOO0O0O =O00OOOOO0OO0OOO0O +' '+OOO0O0000O00000O0 +'\n'#line:586
 OOOOOO000O00OOOOO =mPlayer .runCMD (O0000OOO0OOOO0O0O )#line:587
 OOOOOO000O00OOOOO .start ()#line:588
 return 1 #line:589
def tEditPython (O0OOOO00OOOOO0O0O ):#line:592
    if O0OOOO00OOOOO0O0O .num ==1 :mEditPython ();return ;#line:593
    oo000000000oo000oo .config (text =' Python代码调试')#line:594
def mEditPython ():#line:596
 global winDir #line:597
 O00OO0OOOOOO0OOOO =filedialog .askopenfilename (title ="选择文件",filetypes =(("Python files","*.py"),("all files","*.*")))#line:598
 if not O00OO0OOOOOO0OOOO :return 1 #line:599
 OOO0OOOOOO0OO0OO0 =winDir +'\\temp.bat'#line:600
 O00OO0OOOOOO0OOOO ='"'+O00OO0OOOOOO0OOOO +'"'#line:601
 runBatFile (dsp .getIDLEPath (),O00OO0OOOOOO0OOOO )#line:602
 return 1 #line:603
def tIDLE (O00O0O0OO000OOOO0 ):#line:606
    if O00O0O0OO000OOOO0 .num ==1 :mIDLE ();return ;#line:607
    oo000000000oo000oo .config (text =' 命令行窗口')#line:608
def mIDLE ():#line:610
    OOOOOOO0O0OOO0000 =""#line:611
    runBatFile (dsp .getIDLEPath (),OOOOOOO0O0OOO0000 )#line:612
def typicalScript (O0OOO0OO00O00O000 ):#line:615
 runBatFile (dsp .getPythonPath (),O0OOO0OO00O00O000 )#line:616
 return 1 #line:617
def viewtypicalScript (OO000O0O0O0OO0OOO ):#line:620
 O0000O0O000O0OO00 =open (OO000O0O0O0OO0OOO ,"r",encoding ='utf-8')#line:621
 O0O0OO00OOO0O00OO =O0000O0O000O0OO00 .read ()#line:622
 O0000O0O000O0OO00 .close ()#line:623
 dr .textWindow ('样例程序代码',800 ,600 ,O0O0OO00OOO0O00OO )#line:624
 return 1 #line:625
def mExit ():#line:628
 win .destroy ()#line:629
 return 1 #line:630
def tAbout (OO00OO0OO0OOO00OO ):#line:633
    if OO00OO0OO0OOO00OO .num ==1 :mAbout ();return ;#line:634
    oo000000000oo000oo .config (text =' 关于DRPython')#line:635
def mAbout ():#line:637
    global winDir #line:638
    O0O00OO0O000O0O0O =winDir +'\\html'#line:639
    O0O00O0OO0O0O0OOO =O0O00OO0O000O0O0O +"\\"+"about.html"#line:640
    web1 .htmlBrowser (980 ,700 ,O0O00OO0O000O0O0O ,"about.html")#line:642
def tHelp (OOO0O00OO0OOOO00O ):#line:645
    if OOO0O00OO0OOOO00O .num ==1 :mHelp ();return ;#line:646
    oo000000000oo000oo .config (text =' 显示帮助文档')#line:647
def mHelp ():#line:649
    global winDir #line:650
    OO00OO000O0O0OOOO =winDir +'\\html'#line:651
    OOO0O00000O000000 =OO00OO000O0O0OOOO +"\\"+"drpythonhelp.html"#line:652
    web1 .htmlBrowser (980 ,700 ,OO00OO000O0O0OOOO ,"drpythonhelp.html")#line:654
def tEditControl (OO0OOO000O00OOO00 ):#line:658
    if OO0OOO000O00OOO00 .num ==1 :editControl ();return ;#line:659
    oo000000000oo000oo .config (text =' 进入插入状态')#line:660
def editControl ():#line:662
 global editStatus ,oo000000000oo000oo1 #line:663
 editStatus =0 #line:664
 oo000000000oo000oo1 .config (text ="____插入状态____")#line:665
 return 1 #line:666
def tDelControl (OOOOOO00000OOO0OO ):#line:669
    global currentN #line:670
    if OOOOOO00000OOO0OO .num ==1 :#line:671
        currentN =0 ;#line:672
        delControl ();#line:673
        return ;#line:674
    oo000000000oo000oo .config (text =' 进入删除状态')#line:675
def delControl ():#line:677
 global editStatus ,oo000000000oo000oo1 #line:678
 editStatus =1 #line:679
 oo000000000oo000oo1 .config (text ="____删除状态____")#line:680
 return 1 #line:681
def tColor (O00OO0000OO00O0OO ):#line:684
    if O00OO0000OO00O0OO .num ==1 :selColor ();return ;#line:685
    oo000000000oo000oo .config (text =' 色彩码选择窗')#line:686
def selColor ():#line:688
 O0000O0000OOO0O0O =colorchooser .askcolor (title ="Choose color")#line:689
 if O0000O0000OOO0O0O [0 ]==None :return #line:690
 oo000000000oo000oo .config (text =' 当前选择的色彩码 : '+O0000O0000OOO0O0O [1 ])#line:691
 return 1 #line:692
def tPreview (OOOO0OO0O0O00O0O0 ):#line:695
    if OOOO0OO0O0O00O0O0 .num ==1 :mPreview ();return ;#line:696
    oo000000000oo000oo .config (text =' APP布局效果预览')#line:697
def mPreview ():#line:699
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:700
 global sWidth ,sHeight #line:701
 [OO000O000OO000OO0 ,OOOO0OOO00OO000OO ]=code .toPythonScriptNew (sWidth ,sHeight ,currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup )#line:702
 if OO000O000OO000OO0 <2 :return 1 #line:703
 global winDir #line:704
 O0O0O00OO00OO0O0O =winDir +'\\temp.py'#line:705
 OO00O0OOOOO0000OO =open (O0O0O00OO00OO0O0O ,"w",encoding ="utf-8")#line:706
 OO00O0OOOOO0000OO .write (OOOO0OOO00OO000OO )#line:707
 OO00O0OOOOO0000OO .close ()#line:708
 O0O0O00OO00OO0O0O ='"'+O0O0O00OO00OO0O0O +'"'#line:709
 runBatFile (dsp .getPythonPath (),O0O0O00OO00OO0O0O )#line:710
 return 1 #line:711
def tPreviewCode (O00O000OO000000OO ):#line:714
    if O00O000OO000000OO .num ==1 :mPreviewCode ();return ;#line:715
    oo000000000oo000oo .config (text =' Python代码预览')#line:716
def mPreviewCode ():#line:718
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:719
 global sWidth ,sHeight #line:720
 [O0OOO0OOO0O00OOOO ,OOO0OOOO0000O0O00 ]=code .toPythonScriptNew (sWidth ,sHeight ,currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup )#line:721
 if O0OOO0OOO0O00OOOO <2 :return 1 #line:722
 O0O0OOO00000O0OO0 =dr .textWindow ('代码预览',800 ,600 ,OOO0OOOO0000O0O00 )#line:723
def setInsertControlls (O0O000O0OO0O0OOOO ):#line:726
 global ooooooooo000000000oo ,oo000000000oo000oo ,mFirst ,mLogo #line:727
 if mFirst >1 :mFirst =0 ;mLogo .ax .destroy ()#line:728
 ooooooooo000000000oo =O0O000O0OO0O0OOOO #line:729
 if O0O000O0OO0O0OOOO ==1 :#line:730
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 按钮 Button')#line:731
 if O0O000O0OO0O0OOOO ==101 :#line:732
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 水平按钮组 Horizontal Button Group')#line:733
 if O0O000O0OO0O0OOOO ==102 :#line:734
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 垂直按钮组 Vertical Button Group')#line:735
 if O0O000O0OO0O0OOOO ==2 :#line:736
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 标签 Label')#line:737
 if O0O000O0OO0O0OOOO ==3 :#line:738
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 输入框 Entry')#line:739
 if O0O000O0OO0O0OOOO ==301 :#line:740
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 水平输入框组 Horizontal Entry Group')#line:741
 if O0O000O0OO0O0OOOO ==302 :#line:742
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 垂直输入框组 Vertical Entry Group')#line:743
 if O0O000O0OO0O0OOOO ==4 :#line:744
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 水平标尺 Horizontal Scale')#line:745
 if O0O000O0OO0O0OOOO ==5 :#line:746
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 垂直标尺 Vertical Scale')#line:747
 if O0O000O0OO0O0OOOO ==6 :#line:748
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : RadioButton')#line:749
 if O0O000O0OO0O0OOOO ==7 :#line:750
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : CheckButton')#line:751
 if O0O000O0OO0O0OOOO ==8 :#line:752
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 列表框 ListBox')#line:753
 if O0O000O0OO0O0OOOO ==9 :#line:754
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 下拉列表框 ComboBox')#line:755
 if O0O000O0OO0O0OOOO ==10 :#line:756
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 文本框 Text')#line:757
 if O0O000O0OO0O0OOOO ==11 :#line:758
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : SpinBox')#line:759
 if O0O000O0OO0O0OOOO ==12 :#line:760
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 图标 Icon')#line:761
 if O0O000O0OO0O0OOOO ==13 :#line:762
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 进度条 ProgressBar')#line:763
 if O0O000O0OO0O0OOOO ==14 :#line:764
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 弹出菜单 OptionMenu')#line:765
 if O0O000O0OO0O0OOOO ==30 :#line:767
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 旋钮 Knob')#line:768
 if O0O000O0OO0O0OOOO ==31 :#line:769
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 棒图 Ruler')#line:770
 if O0O000O0OO0O0OOOO ==32 :#line:771
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 水平滑条 HSlider')#line:772
 if O0O000O0OO0O0OOOO ==33 :#line:773
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 垂直滑条 VSlider')#line:774
 if O0O000O0OO0O0OOOO ==34 :#line:775
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 表盘控件 Gauge')#line:776
 if O0O000O0OO0O0OOOO ==35 :#line:777
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 开关控件 Switch')#line:778
 if O0O000O0OO0O0OOOO ==36 :#line:779
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 数显控件 Digital')#line:780
 if O0O000O0OO0O0OOOO ==39 :#line:781
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 报警灯控件 Lamp')#line:782
 if O0O000O0OO0O0OOOO ==37 :#line:783
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 页帧控件 Tab')#line:784
 if O0O000O0OO0O0OOOO ==38 :#line:785
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 外部信息 Info')#line:786
 if O0O000O0OO0O0OOOO ==40 :#line:787
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 水平表盘 HRuler')#line:788
 if O0O000O0OO0O0OOOO ==41 :#line:789
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 渐变色按钮 GButton')#line:790
 if O0O000O0OO0O0OOOO ==42 :#line:791
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 列表控件 List')#line:792
 if O0O000O0OO0O0OOOO ==51 :#line:794
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 二维曲线 Plot')#line:795
 if O0O000O0OO0O0OOOO ==52 :#line:796
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 二维曲线 PlotBar')#line:797
 if O0O000O0OO0O0OOOO ==53 :#line:798
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 二维曲线 PlotPie')#line:799
 if O0O000O0OO0O0OOOO ==54 :#line:800
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 三维曲线 Plot3D')#line:801
 if O0O000O0OO0O0OOOO ==55 :#line:802
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 三维曲线 PlotSurface')#line:803
 if O0O000O0OO0O0OOOO ==56 :#line:804
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 二维曲线 PlotPolar')#line:805
 if O0O000O0OO0O0OOOO ==57 :#line:806
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 二维曲线 PlotContour')#line:807
 if O0O000O0OO0O0OOOO ==58 :#line:808
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 二维曲线 FastPlot')#line:809
 if O0O000O0OO0O0OOOO ==59 :#line:810
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 二维曲线 Stem')#line:811
 if O0O000O0OO0O0OOOO ==60 :#line:812
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 二维曲线 SemilogX')#line:813
 if O0O000O0OO0O0OOOO ==61 :#line:814
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 二维曲线 SemilogY')#line:815
 if O0O000O0OO0O0OOOO ==62 :#line:816
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 二维曲线 LogLog')#line:817
 if O0O000O0OO0O0OOOO ==70 :#line:819
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 定时器 Timer')#line:820
 if O0O000O0OO0O0OOOO ==71 :#line:821
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 录音 Recorder')#line:822
 if O0O000O0OO0O0OOOO ==72 :#line:823
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 放音 Player')#line:824
 if O0O000O0OO0O0OOOO ==73 :#line:825
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : Arduino AD卡')#line:826
 if O0O000O0OO0O0OOOO ==74 :#line:827
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : TCP测量数据服务器')#line:828
 if O0O000O0OO0O0OOOO ==75 :#line:829
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : UDP测量数据服务器')#line:830
 if O0O000O0OO0O0OOOO ==76 :#line:831
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : UDP广播测量数据服务器')#line:832
 if O0O000O0OO0O0OOOO ==77 :#line:833
     oo000000000oo000oo .config (text =' 当前选择的控件类型 : 视频播放器PlayerX')#line:834
 return 1 #line:836
def insertDRControlls (O0O0O0O00O00OO0O0 ):#line:842
    global win ,oo000000000oo000oo #line:843
    global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:844
    currentN =O0O0O0O00O00OO0O0 #line:845
    controlGroup [O0O0O0O00O00OO0O0 ]=insertControl (win ,controlX0Group [O0O0O0O00O00OO0O0 ],controlY0Group [O0O0O0O00O00OO0O0 ],controlWGroup [O0O0O0O00O00OO0O0 ],controlHGroup [O0O0O0O00O00OO0O0 ],controlbgGroup [O0O0O0O00O00OO0O0 ],controlfgGroup [O0O0O0O00O00OO0O0 ],controlNameGroup [O0O0O0O00O00OO0O0 ])#line:846
    return #line:847
def setControlls (OO0O0O0O00O000O0O ):#line:850
 global win ,oo000000000oo000oo #line:851
 global pt1 ,pt2 ,pt3 ,pt4 ,pt5 ,pt6 ,pt7 ,pt8 ,pt9 #line:852
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:853
 oo000000000oo000oo .config (text =' 当前状态: 设定控件属性参数')#line:854
 O00OOOO000O000O00 =pt2 .get ()#line:855
 O0O0OO0O00O0OO0O0 =int (pt3 .get ());OOOO0000000O00OOO =int (pt4 .get ())#line:856
 O00O0000O00O000O0 =int (pt5 .get ());O00O0OOO00OO0000O =int (pt6 .get ())#line:857
 OOO00OOO0O000O0O0 =pt7 .get ();O0O000OO0O00O0OOO =pt8 .get ()#line:858
 OOO0OO0OOO0O0OO0O =currentN #line:859
 controlNameGroup [OOO0OO0OOO0O0OO0O ]=O00OOOO000O000O00 ;controlX0Group [OOO0OO0OOO0O0OO0O ]=O0O0OO0O00O0OO0O0 ;controlY0Group [OOO0OO0OOO0O0OO0O ]=OOOO0000000O00OOO ;controlWGroup [OOO0OO0OOO0O0OO0O ]=O00O0000O00O000O0 ;controlHGroup [OOO0OO0OOO0O0OO0O ]=O00O0OOO00OO0000O ;controlbgGroup [OOO0OO0OOO0O0OO0O ]=OOO00OOO0O000O0O0 ;controlfgGroup [OOO0OO0OOO0O0OO0O ]=O0O000OO0O00O0OOO #line:860
 if OOO0OO0OOO0O0OO0O ==0 :#line:862
  controlNameGroup [OOO0OO0OOO0O0OO0O ]='Main'#line:863
 if O00OOOO000O000O00 =='Main':#line:864
  O00OOOO0O0OO0OOO0 =str (O00O0000O00O000O0 )+'x'+str (O00O0OOO00OO0000O )#line:865
  win .geometry (O00OOOO0O0OO0OOO0 )#line:866
  win .config (bg =OOO00OOO0O000O0O0 )#line:867
  return 1 #line:868
 controlGroup [OOO0OO0OOO0O0OO0O ].ax .destroy ()#line:870
 insertDRControlls (OOO0OO0OOO0O0OO0O )#line:871
 return 1 #line:873
def pushControlPar (OOOO00O0000O0O000 ,OOOO0000OO00O0000 ,O0OOO0OO00OOOO0OO ,O0OO00O00O0000O00 ,O00OO000OO00000OO ,O0OOOO0O0OO0O0O00 ,O0OOO00000OO0O0OO ,O0O00OOOOOO0OOO00 ,OO0O0O0OO000OOO0O ,O0O0000O0O000OOO0 ):#line:879
 global currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:880
 global pt1 ,pt2 ,pt3 ,pt4 ,pt5 ,pt6 ,pt7 ,pt8 ,pt9 #line:881
 currentN =OOOO00O0000O0O000 #line:882
 ooooooooo000000000ooGroup [OOOO00O0000O0O000 ]=OOOO0000OO00O0000 ;controlGroup [OOOO00O0000O0O000 ]=O0OOO0OO00OOOO0OO ;controlNameGroup [OOOO00O0000O0O000 ]=O0OO00O00O0000O00 ;controlX0Group [OOOO00O0000O0O000 ]=O00OO000OO00000OO ;controlY0Group [OOOO00O0000O0O000 ]=O0OOOO0O0OO0O0O00 ;controlWGroup [OOOO00O0000O0O000 ]=O0OOO00000OO0O0OO ;controlHGroup [OOOO00O0000O0O000 ]=O0O00OOOOOO0OOO00 ;controlbgGroup [OOOO00O0000O0O000 ]=OO0O0O0OO000OOO0O ;controlfgGroup [OOOO00O0000O0O000 ]=O0O0000O0O000OOO0 #line:883
 setProtiesWin (OOOO00O0000O0O000 )#line:884
 return 1 #line:885
def clickInsert (O0OO0O0OO0O0OOOO0 ):#line:888
 global ooooooooo000000000oo ,oo000000000oo000oo ,mouseStatus ,editStatus #line:889
 global controlN ,currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:890
 mouseStatus =1 #line:892
 O0OOO0O0O00OOOOOO =ooooooooo000000000oo #line:893
 OOOOO000000OO0O0O =O0OO0O0OO0O0OOOO0 .x ;O0OOOO00000O00O00 =O0OO0O0OO0O0OOOO0 .y #line:894
 if OOOOO000000OO0O0O >(controlWGroup [0 ]-140 ):return ;#line:896
 O00000O0O0OOO0O0O ='  当前鼠标位置 :   '+str (OOOOO000000OO0O0O )+' , '+str (O0OOOO00000O00O00 )#line:898
 oo000000000oo000oo .config (text =O00000O0O0OOO0O0O )#line:899
 if editStatus ==1 :#line:902
     if O0OOOO00000O00O00 <20 :return ;#line:903
     if currentN ==0 :return ;#line:904
     O0OO00O0OOOOOOO0O =msgbox .askyesno ('确认操作','你确定删除该控件 ？')#line:905
     if O0OO00O0OOOOOOO0O ==True :#line:906
         OOOO00OO0O00O0OO0 =currentN ;#line:907
         controlGroup [OOOO00OO0O00O0OO0 ].ax .destroy ();#line:908
         controlGroup [OOOO00OO0O00O0OO0 ]=0 ;#line:909
         ooooooooo000000000ooGroup [OOOO00OO0O00O0OO0 ]=0 ;#line:910
         setProtiesWin (0 )#line:911
         currentN =0 ;#line:912
     return 1 #line:913
 return ;#line:914
def releaseInsert (OO00OOOO0OOOO00OO ):#line:917
 global mouseStatus #line:918
 mouseStatus =0 #line:919
 return 1 #line:920
def winResize (OOO00OOO0OO00OOO0 ):#line:923
 global win ,sWidth ,sHeight #line:924
 global controlN ,currentN ,ooooooooo000000000ooGroup ,controlGroup ,controlNameGroup ,controlX0Group ,controlY0Group ,controlWGroup ,controlHGroup ,controlbgGroup ,controlfgGroup #line:925
 O000OO0000O00OOO0 =win .winfo_width ()#line:926
 OOO000O0O000O0000 =win .winfo_height ()#line:927
 if (O000OO0000O00OOO0 ==controlWGroup [0 ])and (OOO000O0O000O0000 ==controlHGroup [0 ]):return #line:928
 currentN =0 ;controlWGroup [0 ]=O000OO0000O00OOO0 ;controlHGroup [0 ]=OOO000O0O000O0000 ;#line:929
 setProtiesWin (0 )#line:930
winDir =os .getcwd ()#line:933
sys .path .append (winDir )#line:934
win =tk .Tk ()#line:935
win .config (bg ="#ddeeee")#line:936
win .wm_title ('Python APP快速设计工具—DRPython  华中科技大学-何岭松')#line:937
sWidth =win .winfo_screenwidth ()#line:938
sHeight =win .winfo_screenheight ()#line:939
sWrate =0.7 ;sHrate =0.7 ;#line:940
wWin =sWidth *sWrate ;hWin =sHeight *sHrate #line:941
x =(sWidth -wWin )/2 ;y =(sHeight -hWin )/2 #line:942
win .geometry ("%dx%d+%d+%d"%(wWin ,hWin ,x ,y ))#line:943
for i in range (20 ):#line:946
 vf =tk .Frame (win ,bg ='#888888',height =2000 ,width =1 )#line:947
 vf .place (x =i *100 ,y =30 )#line:948
 hf =tk .Frame (win ,bg ='#888888',height =1 ,width =4000 )#line:949
 hf .place (x =0 ,y =i *100 )#line:950
win .bind ('<Configure>',winResize )#line:954
win .bind ('<ButtonPress-1>',clickInsert )#line:955
win .bind ('<ButtonRelease-1>',releaseInsert )#line:956
x0Control =0 #line:959
y0Control =0 #line:960
editStatus =0 #line:961
mouseStatus =0 #line:962
ooooooooo000000000oo =0 #line:963
currentN =0 #line:964
controlN =0 #line:965
ooooooooo000000000ooGroup =[0 for O0OOOOO0OOO00O0O0 in range (0 ,511 )]#line:966
controlGroup =[0 for O00O000OOOOO0OOOO in range (0 ,511 )]#line:967
controlNameGroup =['A'for OOO0O0O0OO000O000 in range (0 ,511 )]#line:968
controlX0Group =[0 for OO0OO0O000O00OOOO in range (0 ,511 )]#line:969
controlY0Group =[0 for OOOO00OO00OO00OO0 in range (0 ,511 )]#line:970
controlWGroup =[0 for O00O00OO00O0O000O in range (0 ,511 )]#line:971
controlHGroup =[0 for O0O000O00OOO0OOOO in range (0 ,511 )]#line:972
controlbgGroup =['0'for O0O00O0OOOO0OOO00 in range (0 ,511 )]#line:973
controlfgGroup =['0'for O0O00O000O00O00O0 in range (0 ,511 )]#line:974
currentN =0 #line:977
ooooooooo000000000ooGroup [0 ]=0 #line:978
controlGroup [0 ]=win #line:979
controlNameGroup [0 ]='Main';#line:980
controlX0Group [0 ]=0 ;#line:981
controlY0Group [0 ]=0 ;#line:982
controlWGroup [0 ]=wWin ;#line:983
controlHGroup [0 ]=hWin ;#line:984
controlbgGroup [0 ]='#ddeeee'#line:985
controlfgGroup [0 ]='#000000'#line:986
oo000000000oo000 =tk .Menu (win )#line:989
oooooooooo00000000ooo =tk .Menu (oo000000000oo000 ,tearoff =False )#line:990
oooooooooo00000000ooo .add_command (label ="新建布局文件",command =mNew )#line:991
oooooooooo00000000ooo .add_command (label ="打开 TXT 布局文件",command =mOpen )#line:992
oooooooooo00000000ooo .add_command (label ="保存 TXT 布局文件",command =mSave )#line:993
oooooooooo00000000ooo .add_separator ()#line:994
oooooooooo00000000ooo .add_command (label ="导出独立APP框架代码",command =mToPython )#line:995
oooooooooo00000000ooo .add_command (label ="导出比例布局独立APP框架代码",command =mToPython1 )#line:996
oooooooooo00000000ooo .add_command (label ="导出APP Class框架代码",command =mToPythonClass )#line:997
oooooooooo00000000ooo .add_separator ()#line:998
oooooooooo00000000ooo .add_command (label ="调试Python程序",command =mEditPython )#line:999
oooooooooo00000000ooo .add_separator ()#line:1000
oooooooooo00000000ooo .add_command (label ="命令行窗口",command =mIDLE )#line:1001
oooooooooo00000000ooo .add_separator ()#line:1002
oooooooooo00000000ooo .add_command (label ="关闭",command =mExit )#line:1003
oo000000000oo000 .add_cascade (label ="文件",menu =oooooooooo00000000ooo )#line:1004
ooo00ooooo00000000ooo =tk .Menu (oo000000000oo000 ,tearoff =False )#line:1006
ooo00ooooo00000000ooo .add_command (label ="插入控件",command =editControl )#line:1007
ooo00ooooo00000000ooo .add_separator ()#line:1008
ooo00ooooo00000000ooo .add_command (label ="删除控件",command =delControl )#line:1009
ooo00ooooo00000000ooo .add_separator ()#line:1010
ooo00ooooo00000000ooo .add_command (label ="设计预览",command =mPreview )#line:1011
ooo00ooooo00000000ooo .add_command (label ="代码预览",command =mPreviewCode )#line:1012
oo000000000oo000 .add_cascade (label ="编辑",menu =ooo00ooooo00000000ooo )#line:1013
ooo00ooooo0000oo00ooo =tk .Menu (oo000000000oo000 ,tearoff =False )#line:1015
ooo00ooooo0000oo00ooo .add_command (label ="声音信号录音",command =lambda :typicalScript ('DRVIExample_Recording.py'))#line:1016
ooo00ooooo0000oo00ooo .add_command (label ="WAV文件放音",command =lambda :typicalScript ('DRVIExample_Play.py'))#line:1017
ooo00ooooo0000oo00ooo .add_command (label ="正弦波与电子琴",command =lambda :typicalScript ('DRVIExample_Piano.py'))#line:1018
ooo00ooooo0000oo00ooo .add_command (label ="典型信号波形与频谱",command =lambda :typicalScript ('DRVIExample_Spectrum.py'))#line:1019
ooo00ooooo0000oo00ooo .add_command (label ="Arduino卡信号采集",command =lambda :typicalScript ('DRVIExample_Arduino.py'))#line:1020
ooo00ooooo0000oo00ooo .add_command (label ="信号保存读取程序",command =lambda :typicalScript ('DRVIExample_SaveLoad.py'))#line:1021
ooo00ooooo0000oo00ooo .add_command (label ="APP Class样例",command =lambda :typicalScript ('DRVIExample_AppClass.py'))#line:1022
ooo00ooooo0000oo00ooo .add_separator ()#line:1023
ooo00ooooo0000oo00ooo .add_command (label ="声音信号录音 代码",command =lambda :viewtypicalScript ('DRVIExample_Recording.py'))#line:1024
ooo00ooooo0000oo00ooo .add_command (label ="WAV文件放音 代码",command =lambda :viewtypicalScript ('DRVIExample_Play.py'))#line:1025
ooo00ooooo0000oo00ooo .add_command (label ="正弦波与电子琴 代码",command =lambda :viewtypicalScript ('DRVIExample_Piano.py'))#line:1026
ooo00ooooo0000oo00ooo .add_command (label ="典型信号波形与频谱 代码",command =lambda :viewtypicalScript ('DRVIExample_Spectrum.py'))#line:1027
ooo00ooooo0000oo00ooo .add_command (label ="Arduino卡信号采集 代码",command =lambda :viewtypicalScript ('DRVIExample_Arduino.py'))#line:1028
ooo00ooooo0000oo00ooo .add_command (label ="信号保存读取程序 代码",command =lambda :viewtypicalScript ('DRVIExample_SaveLoad.py'))#line:1029
ooo00ooooo0000oo00ooo .add_command (label ="APP Class样例 代码",command =lambda :viewtypicalScript ('DRVIExample_AppClass.py'))#line:1030
oo000000000oo000 .add_cascade (label ="APP样例",menu =ooo00ooooo0000oo00ooo )#line:1031
ooo00ooooo00o0oo00ooo00oo =tk .Menu (oo000000000oo000 ,tearoff =False )#line:1033
ooo00ooooo00o0oo00ooo00oo .add_command (label ="UDP广播模式测量数据接收端",command =lambda :typicalScript ('DRVIExample_UDPBS.py'))#line:1034
ooo00ooooo00o0oo00ooo00oo .add_command (label ="UDP广播模式测量数据发送端",command =lambda :typicalScript ('DRVIExample_UDPBC.py'))#line:1035
ooo00ooooo00o0oo00ooo00oo .add_separator ()#line:1036
ooo00ooooo00o0oo00ooo00oo .add_command (label ="UDP模式测量数据接收端",command =lambda :typicalScript ('DRVIExample_UDPS.py'))#line:1037
ooo00ooooo00o0oo00ooo00oo .add_command (label ="UDP模式测量数据发送端",command =lambda :typicalScript ('DRVIExample_UDPC.py'))#line:1038
ooo00ooooo00o0oo00ooo00oo .add_separator ()#line:1039
ooo00ooooo00o0oo00ooo00oo .add_command (label ="TCP模式测量数据接收端",command =lambda :typicalScript ('DRVIExample_TCPS.py'))#line:1040
ooo00ooooo00o0oo00ooo00oo .add_command (label ="TCP模式测量数据发送端",command =lambda :typicalScript ('DRVIExample_TCPC.py'))#line:1041
ooo00ooooo00o0oo00ooo00oo .add_separator ()#line:1042
ooo00ooooo00o0oo00ooo00oo .add_command (label ="UDP广播模式测量数据接收端 代码",command =lambda :viewtypicalScript ('DRVIExample_UDPBS.py'))#line:1043
ooo00ooooo00o0oo00ooo00oo .add_command (label ="UDP广播模式测量数据发送端 代码",command =lambda :viewtypicalScript ('DRVIExample_UDPBC.py'))#line:1044
ooo00ooooo00o0oo00ooo00oo .add_separator ()#line:1045
ooo00ooooo00o0oo00ooo00oo .add_command (label ="UDP广播模式测量数据接收端 代码",command =lambda :viewtypicalScript ('DRVIExample_UDPS.py'))#line:1046
ooo00ooooo00o0oo00ooo00oo .add_command (label ="UDP广播模式测量数据发送端 代码",command =lambda :viewtypicalScript ('DRVIExample_UDPC.py'))#line:1047
ooo00ooooo00o0oo00ooo00oo .add_separator ()#line:1048
ooo00ooooo00o0oo00ooo00oo .add_command (label ="UDP广播模式测量数据接收端 代码",command =lambda :viewtypicalScript ('DRVIExample_TCPS.py'))#line:1049
ooo00ooooo00o0oo00ooo00oo .add_command (label ="UDP广播模式测量数据发送端 代码",command =lambda :viewtypicalScript ('DRVIExample_TCPC.py'))#line:1050
oo000000000oo000 .add_cascade (label ="网络化测量样例",menu =ooo00ooooo00o0oo00ooo00oo )#line:1051
ooo00ooooo00o0oo00ooo00 =tk .Menu (oo000000000oo000 ,tearoff =False )#line:1053
ooo00ooooo00o0oo00ooo00 .add_command (label ="MP3转WAV",command =mp3ToWav )#line:1054
ooo00ooooo00o0oo00ooo00 .add_command (label ="MP4音频提取",command =mp4ToWav )#line:1055
ooo00ooooo00o0oo00ooo00 .add_separator ()#line:1056
ooo00ooooo00o0oo00ooo00 .add_command (label ="播放MP3",command =mp3Play )#line:1057
ooo00ooooo00o0oo00ooo00 .add_command (label ="播放MP4",command =mp4Play )#line:1058
ooo00ooooo00o0oo00ooo00 .add_separator ()#line:1059
ooo00ooooo00o0oo00ooo00 .add_command (label ="色彩代码",command =selColor )#line:1060
ooo00ooooo00o0oo00ooo00 .add_separator ()#line:1061
ooo00ooooo00o0oo00ooo00 .add_command (label ="COM口列表",command =listCOM )#line:1062
ooo00ooooo00o0oo00ooo00 .add_command (label ="Arduino_AD调试器",command =arduinoCard )#line:1063
ooo00ooooo00o0oo00ooo00 .add_separator ()#line:1064
ooo00ooooo00o0oo00ooo00 .add_command (label ="信号分析实验案例",command =signalList )#line:1065
oo000000000oo000 .add_cascade (label ="工具",menu =ooo00ooooo00o0oo00ooo00 )#line:1066
ooo00ooooo00o0oo00ooo =tk .Menu (oo000000000oo000 ,tearoff =False )#line:1068
ooo00ooooo00o0oo00ooo .add_command (label ="关于 DRPython",command =mAbout )#line:1069
ooo00ooooo00o0oo00ooo .add_separator ()#line:1070
ooo00ooooo00o0oo00ooo .add_command (label ="在线帮助",command =mHelp )#line:1071
oo000000000oo000 .add_cascade (label ="关于",menu =ooo00ooooo00o0oo00ooo )#line:1072
win .config (menu =oo000000000oo000 )#line:1074
xBar =tk .Frame (win ,highlightbackground ="#666666",highlightthickness =1 );#line:1077
xBar .pack (side =tk .TOP ,fill =tk .X )#line:1078
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1079
bt1 =insertIcon (xBar ,winDir +'\\imgs\\new.png','新建布局文件',tNew )#line:1080
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1081
bt2 =insertIcon (xBar ,winDir +'\\imgs\\open.png','打开布局文件',tOpen )#line:1082
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1083
bt3 =insertIcon (xBar ,winDir +'\\imgs\\save.png','保存布局文件',tSave )#line:1084
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1085
bt4 =insertIcon (xBar ,winDir +'\\imgs\\export.png','导出独立APP框架',tPython )#line:1086
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1087
bt42 =insertIcon (xBar ,winDir +'\\imgs\\export1.png','导出比例布局独立APP框架',tPython1 )#line:1088
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1089
bt41 =insertIcon (xBar ,winDir +'\\imgs\\class.png','导出APP Class框架',tPythonClass )#line:1090
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1091
bt5 =insertIcon (xBar ,winDir +'\\imgs\\debug.png','调试Python程序',tEditPython )#line:1092
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1093
bt6 =insertIcon (xBar ,winDir +'\\imgs\\insert.png','控件插入状态',tEditControl )#line:1094
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1095
bt7 =insertIcon (xBar ,winDir +'\\imgs\\del.png','控件删除状态',tDelControl )#line:1096
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1097
bt9 =insertIcon (xBar ,winDir +'\\imgs\\color.png','色彩码窗',tColor )#line:1098
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1099
bta =insertIcon (xBar ,winDir +'\\imgs\\preview.png','GUI效果预览',tPreview )#line:1100
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1101
btb =insertIcon (xBar ,winDir +'\\imgs\\code.png',' GUI代码预览',tPreviewCode )#line:1102
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1103
bt55 =insertIcon (xBar ,winDir +'\\imgs\\command.png','命令行窗口',tIDLE )#line:1104
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1105
btc =insertIcon (xBar ,winDir +'\\imgs\\help.png','帮助文档',tHelp )#line:1106
bb =tk .Label (xBar ,text ='');bb .pack (side =tk .LEFT )#line:1107
btd =insertIcon (xBar ,winDir +'\\imgs\\about.png','关于DRPython',tAbout )#line:1108
pt8 =tk .Entry (xBar ,width =10 )#line:1110
pt8 .pack (side =tk .RIGHT )#line:1111
pt8 .bind ("<Return>",setControlls )#line:1112
bb =tk .Label (xBar ,text ='  前景色');bb .pack (side =tk .RIGHT )#line:1113
pt7 =tk .Entry (xBar ,width =10 )#line:1114
pt7 .pack (side =tk .RIGHT )#line:1115
pt7 .bind ("<Return>",setControlls )#line:1116
bb =tk .Label (xBar ,text ='  背景色');bb .pack (side =tk .RIGHT )#line:1117
pt6 =tk .Entry (xBar ,width =6 )#line:1118
pt6 .pack (side =tk .RIGHT )#line:1119
pt6 .bind ("<Return>",setControlls )#line:1120
bb =tk .Label (xBar ,text ='  高度');bb .pack (side =tk .RIGHT )#line:1121
pt5 =tk .Entry (xBar ,width =6 )#line:1122
pt5 .pack (side =tk .RIGHT )#line:1123
pt5 .bind ("<Return>",setControlls )#line:1124
bb =tk .Label (xBar ,text ='  宽度');bb .pack (side =tk .RIGHT )#line:1125
pt4 =tk .Entry (xBar ,width =6 )#line:1126
pt4 .pack (side =tk .RIGHT )#line:1127
pt4 .bind ("<Return>",setControlls )#line:1128
bb =tk .Label (xBar ,text ='  Y0');bb .pack (side =tk .RIGHT )#line:1129
pt3 =tk .Entry (xBar ,width =6 )#line:1130
pt3 .pack (side =tk .RIGHT )#line:1131
pt3 .bind ("<Return>",setControlls )#line:1132
bb =tk .Label (xBar ,text ='  X0');bb .pack (side =tk .RIGHT )#line:1133
pt2 =tk .Entry (xBar ,width =10 )#line:1134
pt2 .pack (side =tk .RIGHT )#line:1135
pt2 .bind ("<Return>",setControlls )#line:1136
bb =tk .Label (xBar ,text ='   标题');bb .pack (side =tk .RIGHT )#line:1137
setProtiesWin (0 )#line:1138
tbar2 =tk .Frame (win ,highlightbackground ="#666666",highlightthickness =1 );#line:1141
tbar2 .pack (side =tk .BOTTOM ,fill =tk .X )#line:1142
oo000000000oo000oo1 =tk .Label (tbar2 ,text ="____插入状态____",bd =1 ,relief =tk .SUNKEN ,anchor =tk .W )#line:1143
oo000000000oo000oo1 .pack (side =tk .LEFT ,fill =tk .X )#line:1144
oo000000000oo000oo =tk .Label (tbar2 ,text ="    就绪  …",bd =1 ,relief =tk .SUNKEN ,anchor =tk .W )#line:1145
oo000000000oo000oo .pack (side =tk .LEFT ,fill =tk .X )#line:1146
tbar0 =tk .Frame (win ,bg ='#cccccc',highlightbackground ="#666666",highlightthickness =1 );#line:1149
tbar0 .pack (side =tk .RIGHT ,fill =tk .Y )#line:1150
ooo00oooo000000000oo =ttk .Treeview (tbar0 )#line:1151
ooo00oooo000000000oo .column ('#0',anchor =tk .CENTER ,width =120 )#line:1152
ooo00oooo000000000oo .heading ('#0',text ='控件列表',anchor =tk .CENTER )#line:1153
ooo00oooo000000000oo .insert (parent ='',index =0 ,iid =0 ,text ='Button')#line:1154
ooo00oooo000000000oo .insert (parent ='',index =1 ,iid =1 ,text ='GButton')#line:1155
ooo00oooo000000000oo .insert (parent ='',index =2 ,iid =2 ,text ='Switch')#line:1156
ooo00oooo000000000oo .insert (parent ='',index =3 ,iid =3 ,text ='IconButton')#line:1157
ooo00oooo000000000oo .insert (parent ='',index =4 ,iid =4 ,text ='HBGroup')#line:1158
ooo00oooo000000000oo .insert (parent ='',index =5 ,iid =5 ,text ='VBGroup')#line:1159
ooo00oooo000000000oo .insert (parent ='',index =6 ,iid =6 ,text ='Label')#line:1160
ooo00oooo000000000oo .insert (parent ='',index =7 ,iid =7 ,text ='Text')#line:1161
ooo00oooo000000000oo .insert (parent ='',index =8 ,iid =8 ,text ='List')#line:1162
ooo00oooo000000000oo .insert (parent ='',index =9 ,iid =9 ,text ='Entry')#line:1163
ooo00oooo000000000oo .insert (parent ='',index =10 ,iid =10 ,text ='RadioBut')#line:1165
ooo00oooo000000000oo .insert (parent ='',index =11 ,iid =11 ,text ='CheckBut')#line:1166
ooo00oooo000000000oo .insert (parent ='',index =12 ,iid =12 ,text ='ListBox')#line:1167
ooo00oooo000000000oo .insert (parent ='',index =13 ,iid =13 ,text ='Combobox')#line:1168
ooo00oooo000000000oo .insert (parent ='',index =14 ,iid =14 ,text ='OptionMenu')#line:1169
ooo00oooo000000000oo .insert (parent ='',index =15 ,iid =15 ,text ='SpinBox')#line:1170
ooo00oooo000000000oo .insert (parent ='',index =16 ,iid =16 ,text ='Knob')#line:1171
ooo00oooo000000000oo .insert (parent ='',index =17 ,iid =17 ,text ='HScale')#line:1172
ooo00oooo000000000oo .insert (parent ='',index =18 ,iid =18 ,text ='VScale')#line:1173
ooo00oooo000000000oo .insert (parent ='',index =19 ,iid =19 ,text ='HSlider')#line:1174
ooo00oooo000000000oo .insert (parent ='',index =20 ,iid =20 ,text ='VSlider')#line:1176
ooo00oooo000000000oo .insert (parent ='',index =21 ,iid =21 ,text ='Progress')#line:1177
ooo00oooo000000000oo .insert (parent ='',index =22 ,iid =22 ,text ='Ruler')#line:1178
ooo00oooo000000000oo .insert (parent ='',index =23 ,iid =23 ,text ='HRuler')#line:1179
ooo00oooo000000000oo .insert (parent ='',index =24 ,iid =24 ,text ='Gauge')#line:1180
ooo00oooo000000000oo .insert (parent ='',index =25 ,iid =25 ,text ='Digital')#line:1181
ooo00oooo000000000oo .insert (parent ='',index =26 ,iid =26 ,text ='Lamp')#line:1182
ooo00oooo000000000oo .insert (parent ='',index =27 ,iid =27 ,text ='Info')#line:1183
ooo00oooo000000000oo .insert (parent ='',index =28 ,iid =28 ,text ='Tab')#line:1184
ooo00oooo000000000oo .insert (parent ='',index =29 ,iid =29 ,text ='Plot')#line:1185
ooo00oooo000000000oo .insert (parent ='',index =30 ,iid =30 ,text ='PlotFast')#line:1187
ooo00oooo000000000oo .insert (parent ='',index =31 ,iid =31 ,text ='Stem')#line:1188
ooo00oooo000000000oo .insert (parent ='',index =32 ,iid =32 ,text ='SemilogX')#line:1189
ooo00oooo000000000oo .insert (parent ='',index =33 ,iid =33 ,text ='SemilogY')#line:1190
ooo00oooo000000000oo .insert (parent ='',index =34 ,iid =34 ,text ='LogLog')#line:1191
ooo00oooo000000000oo .insert (parent ='',index =35 ,iid =35 ,text ='PlotBar')#line:1192
ooo00oooo000000000oo .insert (parent ='',index =36 ,iid =36 ,text ='PlotPie')#line:1193
ooo00oooo000000000oo .insert (parent ='',index =37 ,iid =37 ,text ='PlotPolar')#line:1194
ooo00oooo000000000oo .insert (parent ='',index =38 ,iid =38 ,text ='Plot3D')#line:1195
ooo00oooo000000000oo .insert (parent ='',index =39 ,iid =39 ,text ='PlotSurf')#line:1196
ooo00oooo000000000oo .insert (parent ='',index =40 ,iid =40 ,text ='PlotContour')#line:1197
ooo00oooo000000000oo .insert (parent ='',index =41 ,iid =41 ,text ='Timer')#line:1199
ooo00oooo000000000oo .insert (parent ='',index =42 ,iid =42 ,text ='Recorder')#line:1200
ooo00oooo000000000oo .insert (parent ='',index =43 ,iid =43 ,text ='Play')#line:1201
ooo00oooo000000000oo .insert (parent ='',index =44 ,iid =44 ,text ='PlayX')#line:1202
ooo00oooo000000000oo .insert (parent ='',index =45 ,iid =45 ,text ='ArduinoAD')#line:1203
ooo00oooo000000000oo .insert (parent ='',index =46 ,iid =46 ,text ='TCPS')#line:1204
ooo00oooo000000000oo .insert (parent ='',index =47 ,iid =47 ,text ='UDPS')#line:1205
ooo00oooo000000000oo .insert (parent ='',index =48 ,iid =48 ,text ='UDPBS')#line:1206
ooo00oooo000000000oo .insert (parent ='',index =49 ,iid =49 ,text ='==========')#line:1207
tvScroll1 =ttk .Scrollbar (tbar0 ,orient ='vertical',command =ooo00oooo000000000oo .yview )#line:1209
tvScroll1 .pack (side =tk .RIGHT ,fill =tk .Y )#line:1210
ooo00oooo000000000oo .configure (yscrollcommand =tvScroll1 .set )#line:1211
ooo00oooo000000000oo .pack (side =tk .RIGHT ,fill =tk .Y )#line:1212
ooo00oooo000000000oo .bind ('<<TreeviewSelect>>',gettvID )#line:1213
ooo00oooo000000000oo .bind ('<ButtonRelease-1>',tvmouseUP )#line:1214
ooo00oooo000000000oo .bind ('<ButtonRelease-3>',tvmouseRightUP )#line:1215
ooo00oooo000000000oo .selection_set (0 )#line:1216
mFirst =0 #line:1219
mLogo =dr .DRIcon (win ,(wWin -472 )/2 ,(hWin -200 )/2 ,472 ,110 ,'imgs/drpython.png',400 )#line:1220
win .mainloop ()#line:1223
