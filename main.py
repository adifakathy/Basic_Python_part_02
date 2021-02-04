s="Hello World"
print(s)
print(type(s))
print(s.replace("world","universe"))
print(s.upper())
print(s.lower())


a=2
a=a+11#a+=11
b=a/3
print(a)
c=a//3
d=a**3
print(a,b,c,d,sep=" , ")


s=input("enter your name:")
print(s)
i=int(input("1st value:"))
j=int(input("2nd value:"))
m=i+j
print("the value of m is:",m)


x=10
y=40
print(not(x==10 or y==30))

#type of printing
name ="kathi"
marks=90.4
print(name,marks)
print("name is:",name,"\nhe got marks:",marks)
print("name is:%s \nhe got marks:%f"%(name,marks))
print("name is{} \nhe got marks{}".format(name,marks))#dot forment way


#LIST
list=[10,20.5,"hello",32,-30]
print(list)
print(type(list))
print(len(list))
list.append(45)#it will add at the end of the list
print(list)
lst=[10,13,14.5,50,60]
print(max(lst))
print(min(lst))
lst.sort()
print(lst)
lst.insert(3,100)
print(lst)
lst.sort(reverse=True)
lst.remove(100)
print(lst)
lst.clear()

