from MyMath import MyPoint

p1 = MyPoint(3, 4)
p2 = MyPoint(5, 12)

midPoint_p1_p2 = p1.get_halfway_point_to(p2)
midPoint_p2_p1 = p2.get_halfway_point_to(p1)

print("midPoint_p1_p2", midPoint_p1_p2)
print("midPoint_p2_p1", midPoint_p2_p1)
print("midPoint_p1_p2 equal to midPoint_p2_p1 : ", str(midPoint_p1_p2) == str(midPoint_p2_p1))
print(type(midPoint_p1_p2))