import numpy as np

n = int(input())
print(n)
data = []
for i in range(n):
    a,b = input().split(",")
    row = [int(a), float(b)]
    data.append(row)

def calculate_message_ent(x):
    hashmap = {}
    for i in range(len(x)):
        if x[i][1] not in hashmap:
            hashmap[x[i][1]] = 1
        else:
            hashmap[x[i][1]] +=1
    ent = 0.0
    for x_value in hashmap.items():
        p = float(x_value[1])/len(x)
        logp = np.log2(p)
        ent -= p * logp
    return ent

def calculate_message_taiojian(x):
    hashmap_partition = {}
    ent = 0.0
    for i in range(len(x)):
        if x[i][0] not in hashmap_partition:
            hashmap_partition[x[i][0]] = [x[i]]
        else:
            hashmap_partition[x[i][0]].append(x[i])

    for row_data in hashmap_partition.values():
        ent -= calculate_message_ent(row_data) * (len(row_data)/len(x))
    return ent

print(calculate_message_ent(data)-calculate_message_taiojian(data))