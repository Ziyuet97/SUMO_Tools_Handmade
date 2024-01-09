import os
import io
#paths文件目录，files保存文件路径以及名字
file_name = 'vehroutes.xml'
paths = os.path.abspath(file_name)
oldStr='duration="30.00"'
newStr='duration="20.00"'
with open(paths, "r", encoding="utf-8") as f:
    lines=f.readlines()#将文件内容保存到内存
with open(paths, "w", encoding="utf-8") as f_w:
    for line in lines:#将内存中的文件逐行读取
        if oldStr in line:
            line=line.replace(oldStr,newStr)#新内容代替旧内容
        f_w.write(line)