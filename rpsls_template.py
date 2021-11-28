
"""
程序目标：Rock-paper-scissors-lizard-Spock
作者：李赴点
"""

import random





def name_to_number(name):
    if name=="石头":
        a=0
    elif name=="史波克":
        a=1
    elif name=="纸":
        a=2
    elif name=="蜥蜴":
        a=3
    elif name=="剪刀":
        a=4
    else:a=5
    return a


def number_to_name(number):
    if number==0:
        comp_name="石头"
    elif number==1:
        comp_name="史波克"
    elif number==2:
        comp_name="纸"
    elif number==3:
        comp_name="蜥蜴"
    elif number==4:
        comp_name="剪刀"
    return comp_name





def rpsls(player_choice):
    number=random.randint(0,4)
    print("----------------")
    print("你的选择为"+player_choice)
    print("计算机的选择为"+number_to_name(number))
    a=name_to_number(player_choice)
    if a==5:
        print("Error: No Correct Name")
    elif a==number:
        print("平局")
    elif a<=2 and a-number<=-3:
        print("您赢了")
    elif a>2 and a-number<=2:
        print("您赢了")
    else:print("机器赢了")


print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
input()




