disks=[]
seek_time=0
print("Enter no of disks to schedule: ")
n=int(input())
for i in range(0,n):
      x=int(input("Enter disk no: "))
      disks.append(x)

head=int(input("Enter Head: "))
print("Accessed disk: ")
print(disks[0])
seek_time=seek_time+abs(disks[0]-head)
for i in range(1,n):
    print("Accessed disk: ")
    print(disks[i])
    seek_time=seek_time+abs(disks[i]-disks[i-1])
print("Total seek time is ")
print(seek_time)
