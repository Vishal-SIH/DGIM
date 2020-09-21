input1 = list(map(int,input("Please input the data stream separated by spaces ").split()))
print("Input is ", input1)
k = int(input("Enter the value of k : "))
bucket_list = []
count_bucketsize = {}

start_ind =0
end_ind = 0
pair = 0

for i in range(len(input1)):
    binary_bit = input1[i]
    if(binary_bit == 1):
        if(pair == 1):
            end_ind = i
            pair = 0
            bucket_list.append((start_ind,end_ind,2))
            if 2 in count_bucketsize:
                count_bucketsize[2]+=1
            else:
                count_bucketsize[2] = 1
            for ct in count_bucketsize.keys():
                if(count_bucketsize[ct]>2):
                    s2,e2,size2 = bucket_list.pop(-2)
                    s1,e1,size1 = bucket_list.pop(-2)
                    bucket_list.insert(-1,(s1,e2,size1*2))
                    count_bucketsize[ct]-=2
        else:
            start_ind = i
            pair = 1


print ("List of Bucket Indexes Are : ",bucket_list)
starts = []
ends = []
for s,e,size in bucket_list:
    starts.append(s)
    ends.append(e)

print ("Buckets are ",end="")

for i in range(len(input1)):
    binary_bit = input1[i]
    if(i in starts):
        print (" " ,binary_bit,end="")
    elif(i in ends):
        print (binary_bit,end= " ")
    else:
        print (binary_bit,end = " ")

print("")


length = len(input1)

bound1 = length-1-k
bound2 = length-1

count_1 = 0

for s,e,size in bucket_list[::-1]:
    if(s<bound1 and e < bound1):
        break
    elif(s<=bound1 and e >= bound1):
        count_1 +=int(size/2)
    elif(s>=bound1 and e >= bound1):
        count_1 += size
    else:
        continue



print("Last",k,"binary bits have",count_1,"Ones")