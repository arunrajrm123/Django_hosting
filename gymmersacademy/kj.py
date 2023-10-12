# s="sandeep"
# j=s
# n=1
# m=2
# s=list(s)
# c=0
# for i in range(len(s)):
#     # s=s[-n:]+s[:-n]
#     s=s[-m:]+s[:-m]
#     print(s)
#     c+=1
#     if s==j:
#         break
    
   
# print(s,j,c)
# while True:
   
#     print(s)
#     c=+1
#     s=str(s)
#     if ''.join(s) == j:
#         break
# print(c)\
# def getTotalX(a, b):
#     # Find the maximum value in array a
#     max_a = max(a)
    
#     # Find the minimum value in array b
#     min_b = min(b)
    
#     count = 0
    
#     # Check all numbers between max_a and min_b that are divisible by max_a
#     for x in range(max_a, min_b + 1, max_a):
#         if all(x % ai == 0 for ai in a) and all(bi % x == 0 for bi in b):
#             count += 1
    
#     return count

# # Example usage:
# a = [2, 6]
# b = [12,36]
# result = getTotalX(a, b)
# print(result)  # Output: 3 (the numbers are 4, 8, and 16)


# s="abba"
# s1=list(s)
# s1.remove("b","b")
# print(s1)


# s="abbaxyzz"
# s1=[]
# peek=0
# for i in s:
#     if peek==i:
#         s1.pop()
#         if s1!=[]:
#          peek=s1[len(s1)-1]
#         else:
#            peek=0
#     else:
#         s1.append(i)
#         peek=s1[len(s1)-1]
# print(s1)

# s=[1,2,2,2,4,4,5,1,6]
# d={}
# m=[]
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for key,value in d.items():
#     if value<2:
#        m.append(key)
# print(m)


# s="arun"
# s1=s[0].upper()+s[1:len(s)-1]+s[len(s)-1].upper()
# print(s1)
# a=[1,2,3,4,5,6,7,8]
# for i in range(0,len(a)-1,5):
#     print(a[i],a[i+1])


