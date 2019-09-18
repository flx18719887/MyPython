# 文本文件：文本文件存储的是普通的“字符”文本，可以用记事本打开。word编辑的文档不是文本文件。
# python默认为unicode字符集，两个字节表示一个字符。
# 二进制文件：二进制文件把数据内容用“字节”进行存储，无法用记事本打开。必须使用专用的软件解码。常见的有：MP4视频文件、MP3音频文件、JPG图片、doc文档等。











import os
import os.path

ls = []
def getFile(path, ls):
    fileList = os.listdir(path)


# import os
# import os.path

#path = 'D:/UC/'
ls = []

def getAppointFile(path,ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path,tmp)
            if True==os.path.isdir(pathTmp):
                getAppointFile(pathTmp,ls)
            elif pathTmp[pathTmp.rfind('.')+1:].upper()=='PY':
                ls.append(pathTmp)
    except PermissionError:
        pass

def main():

    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path) == True:
            break

    getAppointFile(path,ls)
    #print(len(ls))
    print(ls)
    print(len(ls))

main()