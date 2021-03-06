import sys, os
lib_path = os.path.abspath(".")
sys.path.append(lib_path)
sys.path.append("../../..")
print(sys.path)
import input, draw, calulate
import CCRRT, CLRRT, PURRT
import numpy as np
car=CCRRT.Vehicle(input.ego_car_size[0],input.ego_car_size[1],input.ego_car_size[2])

# 值的传递：
s=input.starting_point
g=input.goal_point
r=input.random_sample_area
rt=input.rengong_tuoyuan
gk=input.ganzhi_kuang
gt=input.ganzhi_tuoyuan
zk=input.zhenzhi_kuang
# 值传递完毕

print(r)
tree=CLRRT.ClrrtGo(car=car, start=s,goal=g, ganzhi_kuang=gk, ganzhi_tuoyuan=gt, rand_area=r,rengong_tuoyuan=rt)
tree.max_n_node=5000
tree.p_safe=0.96
tree.planning(animation=False)
while True:
    peng=0
    for node_in_final_path in tree.path:
        if tree.peng_zhuang_jian_ce(node_in_final_path, zk):
            peng=1
            break
    if peng==1:
        break
    else:
        tree=CLRRT.ClrrtGo(car=car, start=s,goal=g, ganzhi_kuang=gk, ganzhi_tuoyuan=gt, rand_area=r,rengong_tuoyuan=rt)
        tree.max_n_node=5000
        tree.p_safe=0.96
        tree.planning(animation=False)
print(len(tree.path))
x=draw.Artist(tree,gk, zk, gt, if_draw_tree=0, is_clrrt=1,draw_area=[0, 15, 30, 77])  # 坐标轴 draw_area = [-25, 25, -25, 25]  # x-min x-max y-min y-max
x.play_long()