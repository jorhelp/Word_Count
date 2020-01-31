import os, time
import pyfiglet
fig=pyfiglet.Figlet(font="graffiti")

def menu():
    os.system("clear")
    print("\n=========================================")
    print(fig.renderText("  Count"))
    print("   > 1. 概览")
    print("   > 2. 结构图")
    print("   > 3. 柱状图")
    print("   > 4. 退出")
    print("\n=========================================")

def error():
    os.system("clear")
    print("\n")
    print(fig.renderText("  Error !!!"))
    time.sleep(1)
