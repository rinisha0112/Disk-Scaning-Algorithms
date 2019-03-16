disks=[]
seek_time=0
print("Enter no of disks to schedule: ")
n=int(input())
for i in range(0,n):
      x=int(input("Enter disk no: "))
      disks.append(x)

head=int(input("Enter Head: "))
current_head=head
disks.append(head)
#disks.append(0)
disks.sort()
index=disks.index(head)
print(disks)
a1=[]
a2=[]
a1=disks[0:index]
a2=disks[index+1:n+1]
print(a1)
print(a2)
while len(a1)!=0:
    seek_time=seek_time+abs(current_head-a1[len(a1)-1])
    current_head=a1[len(a1)-1]
    a1.remove(a1[len(a1)-1])
             #index=index-1
    print("Accessed disk: ")
    print(current_head)
while len(a2)!=0:
    seek_time=seek_time+abs(current_head-a2[len(a1)-1])
    current_head=a2[len(a1)-1]
    a2.remove(a2[len(a1)-1])
    print("Accessed disk: ")
    print(current_head)
print("Total seek time is ")
print(seek_time)     

