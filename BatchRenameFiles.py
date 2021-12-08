import tkinter as tk
from tkinter.constants import END
import tkinter.font as tkFont
import os
 
def renameFiles():
    #讀取輸入的標題並去除空字串
    titleList=(title_entry.get('1.0', END))
    titleList=titleList.split('\n')
    for j in titleList:
        if j=='':
            titleList.remove(j)
 
    #讀取路徑與目標資料夾檔案名稱
    loc=(path_entry.get())
    allFile = os.listdir(loc)
 
    #運行錯誤的狀況排除: 已有同名檔案、數量不匹配
    sameName=False
    totalNotMatch=False
 
    if len(allFile) != len(titleList):
        totalNotMatch=True
        result_label.configure(text='檔案與標題數量不匹配')
 
    for n in range(len(titleList)):
        for u in range(len(titleList)):
            if titleList[n] in allFile[u]:
                sameName=True
                result_label.configure(text='目標資料夾已有相同檔名')
                break
        break
 
 
    #保留原本的前綴與副檔名，將最後一段文字改成標題文件的文字
    os.chdir(loc)
    ct=0
    if sameName!=True and totalNotMatch!=True:
        for i in allFile:
            prefix=allFile[ct].rpartition('_')
            ext=os.path.splitext(allFile[ct])
            os.rename(allFile[ct],prefix[0]+'_'+titleList[ct]+ext[1])
            ct+=1
        result_label.configure(text='已成功修改檔案名稱')
       
 
#GUI介面
window=tk.Tk()
fontStyle = tkFont.Font(size=12)
 
window.title('檔名修改工具')
window.geometry('400x400')
window.resizable(0,0)
window.configure(background='#e7e7e7')
 
path_frame = tk.Frame(window,bg='#e7e7e7')
path_frame.pack(side=tk.TOP,padx=20, pady=9,ipadx=140)
path_label1=tk.Label(path_frame, text='輸入檔案所在路徑',font=fontStyle,bg='#e7e7e7')
path_label1.pack(anchor=tk.NW)
path_entry=tk.Entry(path_frame,width=50,font=fontStyle)
path_entry.pack(side=tk.TOP)
 
title_frame = tk.Frame(window,bg='#e7e7e7')
title_frame.pack(side=tk.TOP,padx=20,ipadx=140)
title_label=tk.Label(title_frame,text='輸入標題(以斷行分開)',font=fontStyle,bg='#e7e7e7')
title_label.pack(anchor=tk.NW)
title_entry=tk.Text(title_frame,width=50,height=15,font=fontStyle)
title_entry.pack(side=tk.TOP)
 
btn=tk.Button(window,text='開始', font=fontStyle, command=renameFiles)
btn.pack(padx=20, pady=5,ipadx=50, ipady=2)
 
result_frame=tk.Frame(window,bg='black')
result_frame.pack(side=tk.TOP,ipadx=200, ipady=5)
result_labelL=tk.Label(result_frame,text='運行結果:',font=fontStyle,bg="black", fg="white")
result_labelL.pack(side=tk.LEFT,padx=10)
result_label=tk.Label(result_frame,font=fontStyle,bg="black", fg="white")
result_label.pack(side=tk.LEFT)
 
window.mainloop()