s=["python","django",[1,2,3,4,(5,8,3,"DON","KING"),"don","king"],7,9,10]

print("Given input Z is:",s)

#1 
print(s[2][0])

#DON (use - indexing)
print ("by using - indexing :",s[-4][-3][-2])

#KING (use - indexing)
print("by using - indexing :",s[-4][-3][-1])

#ing (use + indexing)
print("by using + indexing :",s[2][6][1::1])

#ON (use + and - indexing)
print("by using + indexing :",s[2][4][3][1::1])
print("by using - indexing :",s[-4][-3][-2][-2::1])

#8 (use + and - indexing)
print("by using + indexing :",s[2][4][1])
print("by using - indexing :",s[-4][-3][-4])

#N "first occerence" (use + and - indexing)
print("by using + indexing :",s[2][4][3][2::1])
print("by using - indexing :",s[-4][-3][-2][-1::1])

#k (use + and - indexing)
print("by using + indexing :",s[2][6][0:1:1])
print("by using - indexing :",s[-4][-1][-4:-3:1])