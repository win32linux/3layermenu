#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Bill"

import json

# 读取菜单列表
with open ("menu_file.db", "r", encoding="utf-8") as read_menu:
    MENU_LIST = read_menu.read()

# ["EVAL", "JSON"] 功能转换开关
CHANGE_FORMAT = "JSON"

# 转换成字典的方式二种
if CHANGE_FORMAT == "EVAL":
    MENU_LIST = eval(MENU_LIST)
else:
    # json时需要注意：文件中不能包含单引号，严格按照列表字典的书写方式
    # 不能序列化的示例  {"key1": ["v1","v2",]} {'key1': ["v1","v2"]}
    MENU_LIST = json.loads(MENU_LIST.replace("'", "\"").replace(" ","").replace("\n",""))


# 临时菜单存放菜单(简单的栈实现,后进先出)
TEMP_MENU = []
EXIT_FLAG = True
TEMP_MENU.append(MENU_LIST)

while EXIT_FLAG:
    temp_menu_list_id = []
    temp_menu_list_name = []
    if type(TEMP_MENU[-1]) == dict:
        # 加上sorted排序，会让你的key不会随意的改变顺序，因为字典是无序的
        for layer1 in enumerate(sorted(TEMP_MENU[-1])):
            l_id, l_name = layer1[0], layer1[1]
            temp_menu_list_id.append(l_id)
            temp_menu_list_name.append(l_name)
            print(l_id, l_name)
        temp_menu = dict(zip(temp_menu_list_id, temp_menu_list_name))
        real_name = input("input you want to layer[ID or NAME](B:back Q:exit):\n>>>").strip()
        if real_name == "b" or real_name == "B":
            if len(TEMP_MENU) > 1:
                del TEMP_MENU[-1]
                continue
            else:
                input("Now, It's top layer(any key continue)")
                continue
        elif real_name == "q" or real_name == "Q":
            EXIT_FLAG = False
            continue
        elif real_name.isdigit():
            real_name = int(real_name)
            if real_name in temp_menu:
                real_name = temp_menu[real_name]
                TEMP_MENU.append(TEMP_MENU[-1][real_name])
            else:
                input("The worng ID was entered(any key continue)")
                continue
        elif real_name in temp_menu_list_name:
            TEMP_MENU.append(TEMP_MENU[-1][real_name])
        else:
            input("The worng info was entered(any key continue)")
            continue
    else:
        # 加上sorted排序，会让你的key不会随意的改变顺序，因为字典是无序的
        for layer1 in enumerate(sorted(TEMP_MENU[-1])):
            l_id, l_name = layer1[0], layer1[1]
            temp_menu_list_id.append(l_id)
            temp_menu_list_name.append(l_name)
            print(l_id, l_name)
        temp_menu = dict(zip(temp_menu_list_id, temp_menu_list_name))
        real_name = input("Show all menu (B:back Q:exit):\n>>>").strip()
        if real_name == "b" or real_name == "B":
            if len(TEMP_MENU) > 1:
                del TEMP_MENU[-1]
                continue
            else:
                input("Now, It's top layer(any key continue)")
                continue
        elif real_name == "q" or real_name == "Q":
            EXIT_FLAG = False
            continue
        else:
            input("The worng info was entered(any key continue)")
            continue
else:
    print("88")