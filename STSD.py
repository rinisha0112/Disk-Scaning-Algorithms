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
disks.sort()
index=disks.index(head)
while len(disks)!=1:
    index=disks.index(current_head)
    if index==0:
        seek_time=seek_time+abs(current_head-disks[index+1])
        current_head=disks[index+1]
        disks.remove(disks[index])
        print(disks)
        #index=index+1
    elif index==len(disks)-1:
        seek_time=seek_time+abs(current_head-disks[index-1])
        current_head=disks[index-1]
        disks.remove(disks[index])
        print(disks)
        #index=index-1
    else:
        if abs(current_head-disks[index+1])<abs(current_head-disks[index-1]):
            seek_time=seek_time+abs(current_head-disks[index+1])
            current_head=disks[index+1]
            disks.remove(disks[index])
            print(disks)
            index=index+1
        else:
            seek_time=seek_time+abs(current_head-disks[index-1])
            current_head=disks[index-1]
            disks.remove(disks[index])
            print(disks)
            #index=index-1
    print("Accessed disk: ")
    print(current_head)
                                               
print("Total seek time is ")
print(seek_time)                                            
"""print("Accessed disk: ")
print(disks[0])
seek_time=seek_time+abs(disks[0]-head)
for i in range(1,n):
    print("Accessed disk: ")
    print(disks[i])
    seek_time=seek_time+abs(disks[i]-disks[i-1])
print("Total seek time is ")
print(seek_time)"""
