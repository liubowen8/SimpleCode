import sys, os
lib_path = os.path.abspath(".")
sys.path.append(lib_path)
import input, draw, calulate
import CCRRT, CLRRT, PURRT
import numpy as np
car=CCRRT.Vehicle(input.ego_car_size[0],input.ego_car_size[1],input.ego_car_size[2])

# 值的传递：
s=input.cross_starting_point_time1
g=input.cross_goal_point_time1
r=input.random_sample_area_cross_time1
rt=input.rengong_tuoyuan5
gk=input.ganzhi_kuang5
gt=input.ganzhi_tuoyuan5
zk=input.zhenzhi_kuang_cross 
# 值传递完毕

print(r)
tree=CLRRT.ClrrtGo(car=car, start=s,goal=g, ganzhi_kuang=gk, ganzhi_tuoyuan=gt, rand_area=r,rengong_tuoyuan=rt)
tree.max_n_node=5000
tree.planning(animation=False)
print(len(tree.path))

while True:
    tree=CLRRT.ClrrtGo(car=car, start=s,goal=g, ganzhi_kuang=gk, ganzhi_tuoyuan=gt, rand_area=r,rengong_tuoyuan=rt)
    tree.max_n_node=5000
    tree.p_safe=0.96
    tree.planning(animation=False)
    print(len(tree.path))
    pengzheng=0
    for node in tree.path:
        if tree.peng_zhuang_jian_ce(node,zk):
            pengzheng=1
    if pengzheng:
        break
x=draw.Artist(rrt_object=tree,ganzhi_kuang=gk, zhenzhi_kuang=zk, tuoyuan=gt,if_draw_tree=0, is_clrrt=1)  # 坐标轴 area = [-25, 25, -25, 25]  # x-min x-max y-min y-max
x.play_cross()