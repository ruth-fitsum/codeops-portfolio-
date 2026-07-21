# Level 2 : Intermediate

# 4,List operations

num_List= [10, 25, 40, 15, 60, 30]
for i in range(len(num_List)):
    if num_List[i] > 30:
        print(num_List[i])

# this will sort it in place 
print(num_List.sort())

# by using only a method we can have the sum
total=sum(num_List)
print(total)

# there is no built in method for average 
average=total/len(num_List)
print(average)

