#! /usr/bin/python3

# Copyright(c) 2020 note.jorhelp.cn

# Authored by Jorhelp on: 2020年 01月 30日 星期四 14:06:37 CST

# @desc: 字数统计

from Count.Print import *
from Count.Count import *


if __name__ == "__main__":
    while True:
        menu()
        key=input("  Your choice：")
        if key=="1":
            os.system("clear")
            count=0
            temp_file_count=0
            globalVarClear()
            for p in PATH:
                if os.path.isdir(p):
                    os.chdir(p)
                    globalVar(p)
                    count+=countSum(p)
                else:
                    count+=countFile(p)
                    temp_file_count+=1
            print("\n\n\n")
            print("    你一共码了 "+str(count)+" 字")
            print("    共有 "+str(len(FILES)+temp_file_count)+" 个文件")
            print("    共有 "+str(len(FOLDERS))+" 个文件夹")
            input("\n\n回车键继续 @_@")

        elif key=="2":
            os.system("clear")
            for p in PATH:
                if os.path.isdir(p):
                    os.chdir(p)
                    printSum(p)
                else:
                    printFile(p)
            input("\n\n回车键继续 @_@")
        elif key=="3":
            os.system("clear")
            for p in PATH:
                if os.path.isdir(p):
                    globalVarClear()
                    os.chdir(p)
                    globalVar(p)
                    print("{:^36}\n".format(p.rstrip("/").split("/")[-1]))
                    printCloumn()
                    print()
            input("\n回车键继续 @_@")
        elif key=="4":
            break
        else:
            error()
