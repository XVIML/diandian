#Add current Python working path, remove it, if you original python is ok.
import drvi.drviAppendPath as mPath
mPath.appendPythonPath()
#====================================================================
import os
import gc
import time
import numpy as np
import subprocess
import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
from tkinter import filedialog
import tkinter.messagebox as msgbox
from idlelib.colorizer import ColorDelegator, color_config
from idlelib.percolator import Percolator
from drvi import drColorWin as colorWin

#========================================
def item_click(event):
    global currentPath;
    if len(tree_view.selection())<1 :return    
    selected_item = tree_view.selection()[0]
    mArray=tree_view.item(selected_item)
    S=currentPath+"\\"+mArray["values"][0]
    mPasteFileText(S)         

def list_files(folder_path):
    global currentPath;
    currentPath=folder_path
    for item in tree_view.get_children():
        tree_view.delete(item)    
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            tree_view.insert("", "end", values=(filename,))

#=======================================================
def mAI():
    global drviPath
    mPath=drviPath+'\\html\\index.html'
    os.system(mPath)    
    
def mNew():
    mTxt.delete("1.0",'end')
    largeWin()    

def mOpen():
    mfile=filedialog.askopenfilename(title="选择文件",filetypes=(("py files", "*.py"),("all files", "*.*")))
    if not mfile: return 1
    text_file = open(mfile,"r",encoding='utf-8')
    S=text_file.read()
    text_file.close()
    mTxt.delete("1.0",'end')    
    mTxt.insert("1.0",S)
    largeWin()
    
def mSave():
    mfile=filedialog.asksaveasfile(title="选择文件",defaultextension=".py",initialfile = "Untitled.py",filetypes=(("py files", "*.py"),("all files", "*.*")))
    if not mfile: return 1
    S=mTxt.get(1.0,"end-1c")
    text_file = open(mfile.name,"w", encoding="utf-8")
    text_file.write(S)
    text_file.close()

def mExit():
    win.destroy()
   
def mAbout():
    msgbox.showinfo(title='关于...', message='DR.PPTTool\nVersion 1.00\n设计：何岭松\n华中科技大学')

def errFind(err):
    SS=mTxt.get(1.0,"end-1c")
    err=err+'\n\n\n'+SS
    setEditorText(err)
    largeWin()  
      
def mRun():
    gc.collect() 
    SS=mTxt.get(1.0,"end-1c")
    #代码语法检查
    st,err=colorWin.checkCode(SS)
    if st==-1:
        errFind(err)
        return
    #执行脚本，错误则返回
    print('Start...')
    A=colorWin.execScript(rootPath,SS,errFind);
    A.start()
    #正常则将启动的运行窗口置顶
    B=colorWin.delaySetTop(6,'DRVI-','Figure')
    B.start()
    smallWin()
    print('Finish')    
              
def setEditorText(S):
    mTxt.delete("1.0",'end');
    mTxt.insert("1.0",S)
      
def mPaste():
    S=win.clipboard_get()
    S=colorWin.getPlainText(S)
    L=len(S)
    #长度短按文件名处理
    if L<100 and S.find(".py")>=0:
        mFile=S
        if mFile.find(":")>=0:
            mFile=mFile                   #用户指定的绝对路径py文件             
        elif mFile.find("\\")>=0:
            mFile=drviPath+"\\"+S         #drvi库路径下的py文件
        else:
            mFile=rootPath+'\\temp\\'+S   #该程序启动路径\\temp\\的py文件
        mPasteFileText(mFile)
        return
    else:
        mPasteText(S);          

def mPasteFileText(mFile):    
    if not os.path.exists(mFile):
        S="文件不存在：\n"+mFile
        setEditorText(S)
        largeWin()
        return
    text_file = open(mFile,"r",encoding='utf-8')
    S=text_file.read()
    text_file.close()    
    setEditorText(S);
    #小窗口下粘贴文件，则直接运行
    if win.winfo_height()<100: mRun()    

def mPasteText(S):
    setEditorText(S)
    #小窗口下粘贴文件，则直接运行
    if win.winfo_height()<100: mRun()      
    
def mEdit():
    if win.winfo_height()<100: largeWin()
    else: smallWin()

def smallWin():
    win.geometry("220x0")
    for child in xBar.winfo_children():
        child.configure(state='disable')    

def largeWin():
    win.geometry("1100x550")
    for child in xBar.winfo_children():
        child.configure(state='normal')
        
def mFont(v):
    mTxt.configure(font=('Arial',v))

def mTop():
    #==将标题栏含如下字符的窗口置顶，位于PPT前
    E1=colorWin.delaySetTop(0,'DRVI','Figure','豆包')
    E1.start()

def mIDLE():
    subprocess.run(["python", "-m", "idlelib", "-e"])

#==缩进处理=================
def auto_indent(event):
    global mTxt
    # 获取当前行
    line_idx = mTxt.index(tk.INSERT).split('.')[0]
    line_text = mTxt.get(f"{line_idx}.0", f"{line_idx}.end")
    # 提取当前行开头空格
    leading_space = re.match(r'^(\s*)', line_text).group(1)
    indent_level = len(leading_space)
    # 如果本行以:结尾，下一行多4空格缩进
    if block_pattern.search(line_text):
        new_indent = leading_space + "    "
    else:
        new_indent = leading_space
    # 插入换行 + 缩进
    mTxt.insert(tk.INSERT, "\n" + new_indent)
    return "break"  # 阻止默认回车行为

def tab_handler(event):
    global mTxt
    mTxt.insert(tk.INSERT, "    ")
    return "break"

def backspace_handler(event):
    global mTxt
    pos = mTxt.index(tk.INSERT)
    col = int(pos.split(".")[1])
    if col >=4:
        line_start = pos.split(".")[0] + ".0"
        line_prefix = mTxt.get(line_start, pos)
        if line_prefix.endswith("    "):
            mTxt.delete(f"{pos} -4c", pos)
            return "break"

    
#==Main Window=====================
win= tk.Tk()
win.wm_title('Main')
win.geometry('1100x550')
win.config(bg="#ddeeee")
win.wm_title('Python PPT伴侣 -- 何岭松')
win.attributes("-toolwindow", 2)
win.wm_attributes("-topmost", True)
#==MenuBar========================
menubar=tk.Menu(win,bg="#222222",fg="#ffffff")
menu1=tk.Menu(menubar,tearoff=False)
menu1.add_command(label="IDLE",command=mIDLE)
menu1.add_separator()
menu1.add_command(label="新建文件",command=mNew)
menu1.add_command(label="打开文件",command=mOpen)
menu1.add_command(label="保存文件",command=mSave)
menu1.add_separator()
menu12=tk.Menu(menubar,tearoff=False)
menu12.add_command(label="10点",command=lambda:mFont(10))
menu12.add_command(label="12点",command=lambda:mFont(12))
menu12.add_command(label="14点",command=lambda:mFont(14))
menu12.add_command(label="16点",command=lambda:mFont(16))
menu12.add_command(label="18点",command=lambda:mFont(18))
menu12.add_command(label="20点",command=lambda:mFont(20))
menu12.add_command(label="22点",command=lambda:mFont(22))
menu12.add_command(label="24点",command=lambda:mFont(24))
menu12.add_command(label="26点",command=lambda:mFont(26))
menu12.add_command(label="28点",command=lambda:mFont(28))
menu12.add_command(label="30点",command=lambda:mFont(30))
menu1.add_cascade(label="±字号",menu=menu12)
menu1.add_separator()
menu1.add_command(label="↸运行窗置顶",command=mTop)
menu1.add_separator()
menu1.add_command(label="AI助手",command=mAI)
menu1.add_separator()
menu1.add_command(label="关于",command=mAbout)
menu1.add_separator()
menu1.add_command(label="关闭",command=mExit)
menubar.add_cascade(label="▤文件",menu=menu1)
menubar.add_cascade(label="⇅窗口",command=mEdit)
menubar.add_command(label="↘粘贴",command=mPaste)
menubar.add_command(label="▶运行",command=mRun)
win.config(menu=menubar)
#==Layout============================================
mLayout=tk.PanedWindow(win,orient=tk.VERTICAL,bg='#ccffff')
mLayout.pack(fill=tk.BOTH, expand=1)
#==工具条============================================
xBar=tk.Frame(mLayout,highlightbackground = "#888888",highlightthickness=1);
xBar.pack(side=tk.TOP,fill=tk.X)
cd=tk.Button(xBar,text='DRVI控件',command=lambda:list_files(drviPath+'\\cd_drvi'))
cd.pack(side=tk.LEFT)
c1=tk.Button(xBar,text='波形分析',command=lambda:list_files(drviPath+'\\c1_Time'))
c1.pack(side=tk.LEFT)
c2=tk.Button(xBar,text='频谱分析',command=lambda:list_files(drviPath+'\\c2_Fre'))
c2.pack(side=tk.LEFT)
c3=tk.Button(xBar,text='幅值分析',command=lambda:list_files(drviPath+'\\c3_PDF'))
c3.pack(side=tk.LEFT)
c4=tk.Button(xBar,text='相关分析',command=lambda:list_files(drviPath+'\\c4_corr'))
c4.pack(side=tk.LEFT)
c5=tk.Button(xBar,text='数字滤波',command=lambda:list_files(drviPath+'\\c5_filter'))
c5.pack(side=tk.LEFT)
c6=tk.Button(xBar,text='时频分析',command=lambda:list_files(drviPath+'\\c6_TF'))
c6.pack(side=tk.LEFT)
c7=tk.Button(xBar,text='小波分析',command=lambda:list_files(drviPath+'\\c7_WT'))
c7.pack(side=tk.LEFT)
c8=tk.Button(xBar,text='Hilbert-黄',command=lambda:list_files(drviPath+'\\c8_EWD'))
c8.pack(side=tk.LEFT)
c9=tk.Button(xBar,text='盲源分离',command=lambda:list_files(drviPath+'\\c9_Blend'))
c9.pack(side=tk.LEFT)
ca=tk.Button(xBar,text='时序分析',command=lambda:list_files(drviPath+'\\ca_ARMA'))
ca.pack(side=tk.LEFT)
ca=tk.Button(xBar,text='压缩感知',command=lambda:list_files(drviPath+'\\cg_compress'))
ca.pack(side=tk.LEFT)
cb=tk.Button(xBar,text='测试数据集',command=lambda:list_files(drviPath+'\\cb_DATASET'))
cb.pack(side=tk.LEFT)
cb=tk.Button(xBar,text='控制系统',command=lambda:list_files(drviPath+'\\ce_control'))
cb.pack(side=tk.LEFT)
cb=tk.Button(xBar,text='OpenCV',command=lambda:list_files(drviPath+'\\cf_opencv'))
cb.pack(side=tk.LEFT)
cc=tk.Button(xBar,text='其他例程',command=lambda:list_files(drviPath+'\\cc_other'))
cc.pack(side=tk.LEFT)
cc=tk.Button(xBar,text='Temp',command=lambda:list_files(rootPath+'\\temp'))
cc.pack(side=tk.LEFT)
#==Layout1================================
mLayout1=tk.PanedWindow(mLayout,bg='#ccccff')
mLayout1.pack(fill=tk.BOTH, expand=1)
#==Trame===============
frame1=tk.Frame(mLayout1, width=200, background='lightgreen')
frame2=tk.Frame(mLayout1,  background='hotpink')
mLayout1.add(frame1)
mLayout1.add(frame2)
#=================================
tree_view = ttk.Treeview(frame1, columns=("Files",), show="headings", selectmode="browse")
tree_view.heading("Files", text="文件列表")
tree_view.pack(padx=2, pady=2, fill="both", expand=True);
tree_view.bind("<<TreeviewSelect>>", item_click);

#=Editor Window==============================================
mTxt = scrolledtext.ScrolledText(frame2, font=("Consolas",11), wrap=tk.NONE)
mTxt.pack(side=tk.LEFT,fill="both", expand=True)
# 插入IDLE着色器
color_config(mTxt)
percolator=Percolator(mTxt)
color_delegator = ColorDelegator()
percolator.insertfilter(color_delegator)
# 自制自动缩进逻辑 =====
block_pattern = re.compile(r":\s*(#.*)?$")
mTxt.bind("<Return>", auto_indent)
mTxt.bind("<Tab>", tab_handler)
mTxt.bind("<BackSpace>", backspace_handler)

#======================================
rootPath=os.getcwd();
drviPath=mPath.getDRVIPath()
currentPath=drviPath+"\\cd_drvi"
list_files(currentPath);
setEditorText(colorWin.mSpectrumCode())
smallWin()
mFont(13)
#==Main Loop=====================
win.mainloop()

