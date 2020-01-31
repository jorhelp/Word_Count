import os, pathlib
from configparser import ConfigParser

#==================================
# 配置文件读取与全局变量
#==================================
config=ConfigParser()
config.read('wcountrc')
try:
    PATH=list(map(str.strip, config['basic']['path'].split(";")))
except:
    PATH=[]
try:
    EXCLUDE_FOLDERS=list(map(str.strip, config['basic']['exclude_folder'].split(";")))
except:
    EXCLUDE_FOLDERS=[]
try:
    EXCLUDE_FILES=list(map(str.strip, config['basic']['exclude_file'].split(";")))
except:
    EXCLUDE_FILES=[]
try:
    EXCLUDE_FILES_TYPES=list(map(str.strip, config['basic']['exclude_file_type'].split(";")))
except:
    EXCLUDE_FILES_TYPES=[]

FILES=dict()
FOLDERS=[]


#==================================
# 字数统计
#==================================
def wordCount(filename):
    count=0
    with open(filename, 'r') as f:
        lines=f.readlines()
        for line in lines:
            count+=len(line.strip())
    return count


#==================================
# 遍历目录进行统计
#==================================
# 文件是否可以统计
def validFile(filename):
    if filename in EXCLUDE_FILES:
        return False
    else:
        file_temp=filename.split(".")
        if len(file_temp)>=2:
            if file_temp[-1] in EXCLUDE_FILES_TYPES:
                return False
    return True

# 文件与文件夹全局变量获取值
def globalVar(path):
    items=os.listdir()
    if len(items)>0:
        for i in items:
            if os.path.isfile(i) and validFile(i):
                FILES[i]=countFile(i)
            elif os.path.isdir(i) and i not in EXCLUDE_FOLDERS:
                FOLDERS.append(i)
                os.chdir(i)
                globalVar(i)
                os.chdir("..")

# 文件与文件夹全局变量清空
def globalVarClear():
    global FILES
    global FOLDERS
    FILES.clear()
    FOLDERS.clear()


# 统计单个文件
def countFile(filename):
    if validFile(filename):
        return wordCount(filename)
    else:
        return 0

# 统计单个文件夹
def countFolder(folder):
    count=0
    if folder not in EXCLUDE_FOLDERS:
        os.chdir(folder)
        items=os.listdir()
        for i in items:
            if os.path.isfile(i):
                count+=countFile(i)
            elif os.path.isdir(i):
                count+=countFolder(i)
        os.chdir("..")
    return count

# 统计总数
def countSum(path):
    count=0
    items=os.listdir(path)
    if len(items)>0:
        for i in items:
            if os.path.isfile(i):
                count+=countFile(i)
            elif os.path.isdir(i):
                count+=countFolder(i)
    return count


#==================================
# 打印
#==================================
# 打印一个文件的字数
def printFile(filename):
    if validFile(filename):
        print("  "+filename+" ["+str(countFile(filename))+"]")

# 打印一个文件夹的字数
def printFolder(folder, deepth):
    if folder not in EXCLUDE_FOLDERS:
        os.chdir(folder)
        items=os.listdir()
        a=[]
        b=[]
        for i in items:
            if os.path.isfile(i) and validFile(i):
                a.append(i)
            elif os.path.isdir(i) and i not in EXCLUDE_FOLDERS:
                b.append(i)
        for i in a:
            print("    "*deepth, end="")
            printFile(i)
        for i in b:
            print("    "*deepth+"  "+i+" ["+str(countFolder(i))+"]")
            printFolder(i, deepth+1)
        os.chdir("..")

# 打印总
def printSum(path):
    root_folder=path.rstrip("/").split("/")[-1]
    print("\n  "+root_folder+" ["+str(countSum(path))+"]")
    os.chdir("..")
    printFolder(root_folder, 1)
    os.chdir(root_folder)

# 格式化对齐
def strFormat(string, length):
    temp_length=0
    re_str=""
    for char in string:  
        if u'\u4e00' <= char <= u'\u9fa5':  # 判断一个字是否为汉字
            temp_length += 2
        else:
            temp_length +=1
        if temp_length>length:
            break
        re_str+=char
    while temp_length<length:
        re_str=" "+re_str
        temp_length+=1


    return re_str

# 打印柱状图
def printCloumn():
    max_count=0
    max_len=35  #最长的那个柱的长度
    temp_files=[]
    temp_length=[]
    if len(FILES)!=0:
        for i in FILES:
            max_count=max(max_count, FILES[i])
            temp_files.append(i)

        if max_count!=0:
            for i in FILES:
                temp_length.append(int((FILES[i]/max_count)*max_len))
        else:
            temp_length=[0 for i in range(len(FILES))]

        for i in range(len(temp_files)):
            temp_files[i]=strFormat(temp_files[i], 18)

        for i in range(len(temp_files)):
            print(temp_files[i]+"│", "▇"*temp_length[i], list(FILES.values())[i])


#==================================
# 测试
#==================================
def test():
    #  print(PATH)
    #  print(EXCLUDE_FILES)
    #  print(EXCLUDE_FOLDERS)
    #  print(EXCLUDE_FILES_TYPES)
    for i in FILES:
        print(i)
    print(FOLDERS)
