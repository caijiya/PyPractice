import random

randomNum = random.randrange(1001, 9999)
var3 = []  # 比对结果


def get(num):
    var1 = []
    numStr = str(num)
    for x in numStr:
        var1.append(int(x))
    return var1


var1 = get(randomNum)  # 基数数组


def loop(var1, var2):
    bool = False
    var3 = []
    for x in range(0, 4):
        if (var1[x] > var2[x]):
            var3.append("小")
            bool = True
        elif (var1[x] < var2[x]):
            var3.append("大")
            bool = True
        else:
            var3.append("相等")
    print(var3)
    if (bool):
        inputNum = input("您猜测的不对，接着猜，菜鸡")
        var2 = get(inputNum)
        loop(var1, var2)


inputNum = input("请输入您所猜测的四位数: ")
inputNum = int(inputNum)
if inputNum > 10000 or inputNum < 1001:
    inputNum = input("请输入四位整数")

else:
    var3 = []
    var2 = get(inputNum)  # 实际输入数组
    loop(var1, var2)
