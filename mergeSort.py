u_list = [("kaviya",4),("Kimi",3),("Zia",4),("Jatha",5),("Jena",6)]
#u_list.sort()
print(u_list)
length = len(u_list)
mid = length//2
list_1 = u_list[0:mid]
list_2 = u_list[mid:length]
print(list_1,list_2)
while len(list_2) > 1:
  length = len(list)
  mid = length//2

count = 0
value = 1
if list_1[count][1]>list_2[count][1]:
 print(list_1[count][1])
