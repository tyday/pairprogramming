import problemone.py as p1

if p1.testone([1,2,3,4,5]) == 15:
    print("pass")
else:
    print ('fail')



# def recList(list):
#     if len(list) ==1:
#         return list.pop()
#     else:
#         return list.pop() + recList(list)

if p1.testone([1,2,3,4,4]) == 15:
    print("Test One:Pass")
else:
    print ('Test One: Fail')

if p1.testtwo([1,2,3,4,4]) == 15:
    print("Test Two:Pass")
else:
    print ('Test Two: Fail')
if p1.testthree([1,2,3,4,4]) == 15:
    print("Test Three:Pass")
else:
    print ('Test Three: Fail')
