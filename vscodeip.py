def isEvenorOdd(n):
    counteven=0
    if (n%2==0):
        return 1
    else:
        return 0
def isPositive():
    n=int(input())
    if (n>0):
        print("n is positive")
    elif (n==0):
        print("zero")
    else:
        print("negative")
    return
def perimeterofrectangle():
    length=int(input())
    breadth=int(input())
    if length<=0 or breadth<=0:
        print("Not a valid input")
    else:
        return (2*(length+breadth))
def computeTax():

    salary=int(input())
    if salary<=0:
        print("Invalid salary")
        return
    tax=0.0
    if salary<10000:
        tax=0
    elif salary<=20000:
        tax=0+0.1*(salary-10000)
    elif salary<=30000:
        tax=0+0.1*10000+0.2*(salary-20000)
    elif salary<=40000:
        tax=0+0.1*10000+0.2*10000+0.3*(salary-30000)
    elif salary<=50000:
        tax=0+(0.1*10000)+(0.2*10000)+(0.3*10000)+0.4*(salary-40000)
    else:
        tax=0+(0.1*10000)+(0.2*10000)+(0.3*10000)+(0.4*10000)+0.5*(salary-50000)
    return tax
def checkPrime(n):
    x=0
    if(n==1):
        x=0
    elif(n==2):
        x=1
    else:
        for i in range(2,n):
            if(n%i==0):
               x=0
               break
            else:
               x=1
    return x
def reverse(n):
    rev=0
    while(n>0):
        a=n%10
        rev=(rev*10)+a
        n=n//10
    print(rev)        
def longeststring(strs):
    longest=max(strs,key=len)
    print(longest)
def selectionsort(givenlist):
    for i in range(0,len(givenlist)):
        min=i
        for j in range(i+1,len(givenlist)):
            if(givenlist[j]<givenlist[min]):
                temp=givenlist[min]
                givenlist[min]=givenlist[j]
                givenlist[j]=temp
    return [givenlist]
def reverse(list):
    return list[::-1]
def revstr(str):
    str2=[]
    for i in range(0,len(str)):
        ele2=str[i]
        str2.append(ele2)
    str2=reverse(str2)
    x=1
    for i in range(0,len(str)):
        if(str[i]==str2[i]):
            x=1
        else:
            x=0
            break
    return x
def answer(givenlist):
    min=0
    max=0
    for i in range(0,len(givenlist)):
        if(givenlist[min]>givenlist[i]):
            min=i
        elif(givenlist[max]<givenlist[i]):
            max=i
    print(givenlist[max])
    print(givenlist[min])
def kidsWithCandies(candies, extraCandies):
        max=0
        for i in range(0,len(candies)):
                if(candies[i]>candies[max]):
                        max=i
        for i in range(0,len(candies)):
                if ((candies[i]+extraCandies)>=candies[max]):
                        return bool(1)
                else:
                        return bool(0)
def removeElement(nums, val):
    nums.remove(val)
    print(nums)
    return len(nums)
def searchInsert(nums,target):
        a=0
        i=0
        while(i<len(nums)):
                if(nums[i]==target):
                        a=1
                        b=i
                        return i
                i=i+1
        if(a==0):
                i=0
                while(i<len(nums)-1):
                        if(nums[i]<target)and(target<nums[i+1]):
                                a=1
                                b=i+1
                                return (i+1)
                        
                        elif(i==(len(nums)-1)):
                             b=i
                             break
                             return b
        else:
            return b
def longestCommonPrefix(strs):

    result=0
    y=''
    for i in range(0,len(strs)):
        val=strs[1][i]
        for j in range(0,len(strs)-1):
            if(val==strs[i][j])and(val==strs[i+1][j]):
                result=result+1
    if (result!=0):
        result=result
    else:
        result=-2
    for i in range(0,result+1):
        y=y+strs[0][i]
    y=''+y
    return y
def removeDuplicates(nums):
    a=1
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            if(nums[i]==nums[j]):
                a=a
            else:
                a=a+1
                break   
    return a
def checkj(nums):
    for i in range(0,n-1):
        if(i==2):
            del nums[i]
        print(i)
    print(nums)
    return 0
def plusone(digits):
    a=0
    b=int
    c=int
    n=len(digits)
    for i in range(len(digits))[::-1]:
        c=digits[i]
        b=(10**(n-i-1))*c
        a=a+b
        print((n-i-1))
    a=a+1
    list=[]
    while(a!=0):
        b=a%10
        list.append(b)
        a=a//10
    l2=len(list)
    ele=int
    finallist=[]
    for i in range(0,l2):
        ele=list.pop()
        finallist.append(ele)

    return finallist
def merge(nums1,nums2,m,n):
    i=0
    j=0
    fnum=[]
    while(i<m):
        fnum.append(nums1[i])
        i=i+1
    while(j<m):
        fnum.append(nums2[j])
        j=j+1
    for i in range(0,len(nums1)):
        nums1.pop()
    for i in range(0,len(fnum)):
        nums1.append(fnum[i])
    for i in range(0,len(nums1)):
        min=i
        for j in range(i+1,len(nums1)):
            if(nums1[j]<nums1[min]):
                temp=nums1[min]
                nums1[min]=nums1[j]
                nums1[j]=temp
    print(nums1)
    return 0
def stockprice(prices):
    sp=[]
    for i in range(0,len(prices)-1):
        for j in range(i+1,len(prices)):
            ele=prices[j]-prices[i]
            if (ele>0):
                sp.append(ele)
    sp.sort()
    n=len(sp)-1
    if(n>0)or(n==0):   
        return sp[n]
    else:
        return 0
def jewels(J,S):
    count=0
    for i in range(0,len(J)):
        for j in range(0,len(S)):
            if(J[i]==S[j]):
                count=count+1
    return count
def numssmaller(nums):
    list=[]
    count=0
    for i in range(0,len(nums)):
        count=0
        for j in range(0,len(nums)):
            if(nums[i]>nums[j]):
                count=count+1
        list.append(count)
    return list
def subandsum(n):
    list=[]
    list2=[]
    while(n!=0):
        ele=n%10
        n=n//10
        list.append(ele)
def encodedlist(nums):
    list=[]
    j=1
    for i in range(0,len(nums),+2):
        freq=nums[i]
        val=nums[j]
        j=j+2
        for k in range(0,freq,+1):
            list.append(val)
    return list
def findevendigitarray(nums):
    count=0
    list=[]
    a=int
    for i in range(0,len(nums)):
        n=nums[i]
        while(n!=0):
            a=n%10
            list.append(a)
            n=n//10
        if((len(list))%2==0):  
            count=count+1
            print(list)
        for i in range(0,len(list)):
            list.pop()
        
    return count
def splitstring(str):
    countr=0
    for i in range(0,len(str)):
        if(str[i]=="R"):
            if(str[i+1]=="R"):
                 print(countr) 
def areaofrectangle(l,b):
    if(l==0 or b==0):
        return 0
    else:
        return l*b
def simpleinterest(p,r,t):
    a=int(p*r*t/100)
    return a
def squaresoffirstn(n):
    count=0
    q=1
    for i in range(0,n):
        count=count+(q*q)
        q=q+1
    return count
def isPrimeorNot(x):
    a=0
    if(x<2):
        a=0
    elif(x==2):
        a=1
    else:
        for i in range(2,(x-1)):
            if(x%i==0):
                a=0
                break
            else:
                a=1
    if(a==0):
        print("No")
    else:
        print("Yes")
def queryInteger(x,q,count):
    if(x==q):
        count=count+1
    else:
        count=count
    return count
def reverseLink(l):
    for i in range(len(l),0):
        print(l[i])
        i=i-1
def nonnegbetween(m,n):
    for i in range(0,(n-m)+1):
        if(m<0):
            m=m+1
        elif(m>=0 or m<=n):
            print(m)
            m=m+1
        elif(m>n):
            break
def descendingarray(arr,n):
    x=1
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(arr[j]<=arr[i]):
                x=1
            else:
                x=0
    return x
def asscendingarray(arr,n):
    x=1
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(arr[j]>=arr[i]):
                x=1
            else:
                x=0
    return x
def reverseinteger(n):
    a=0
    if(n>=0 and n<2147483647):
        while(n>0):
            x=n%10
            a=a*10+x
            n=n//10
        print(a)
    elif(n>2147483647):
        print(0)
    else:
        n=-1*n
        while(n>0):
            x=n%10
            a=a*10+x
            n=n//10
        print(-a)     
def searchInsert2(nums,target):
    for i in range(0,len(nums)):
        if (nums[i]>=target):
            a=i
            break
    return a
n=int(input())
target=int(input())
nums=[]
for j in range(0,n):
    ele=int(input())
    nums.append(ele)
print(searchInsert2(nums,target))