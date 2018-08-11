# import problemone.py as p1

# if p1.testone([1,2,3,4,5]) == 15:
#     print("pass")
# else:
#     print ('fail')



def recList(list):
    if len(list) ==1:
        return list.pop()
    else:
        return list.pop() + recList(list)

if recList([1,2,3,4,4]) == 15:
    print("Pass")
else:
    print ('Fail')