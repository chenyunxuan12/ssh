#TemperConvert.py
Temperstr=input("请输入带有符号的温度值")
if Temperstr[-1] in ["F","f"]:
    C=(eval(Temperstr[0:-1]-32))/1.8
    print("转换后的温度为{:.2f}C".format(C))
elif Temperstr[-1] in ["C","c"]:
    F=1.8 * eval(Temperstr[0:-1])+32
    print("转换后的温度为{:.2f}F".format(F))
else:
    print("输入格式错误")
