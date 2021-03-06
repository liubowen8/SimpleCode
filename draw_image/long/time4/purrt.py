import sys, os
lib_path = os.path.abspath(".")
sys.path.append(lib_path)
print(sys.path)
import input, draw, calulate
import CCRRT, CLRRT, PURRT
import numpy as np
car=CCRRT.Vehicle(input.ego_car_size[0],input.ego_car_size[1],input.ego_car_size[2])

# 值的传递：
s=input.starting_point_time4
g=input.goal_point_time4
r=input.random_sample_area4
rt=input.rengong_tuoyuan4
gk=input.ganzhi_kuang4
gt=input.ganzhi_tuoyuan4
zk=input.zhenzhi_kuang
# 值传递完毕

print(r)
tree=PURRT.PurrtGo(car=car, start=s,goal=g, ganzhi_kuang=gk, ganzhi_tuoyuan=gt, rand_area=r,rengong_tuoyuan=rt)
tree.max_n_node=5000
tree.p_safe=0.96
tree.planning(animation=False)
print(len(tree.path))
x=draw.Artist(tree,gk, zk, tuoyuan=gt, if_draw_tree=0, is_clrrt=0,draw_area=[0, 15, 30, 100])  # 坐标轴 draw_area = [-25, 25, -25, 25]  # x-min x-max y-min y-max
x.play_long()