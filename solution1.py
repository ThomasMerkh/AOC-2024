import numpy as np

# part one
data = np.loadtxt('input1.txt')
data = np.sort(data, axis=0)
print(int(np.sum(np.abs(data[:,1] - data[:,0]))))

# part two
left = right = last = 0
while right < data.shape[0] and left < data.shape[0]:
    if data[left, 0] != last:
        count = 0
    if data[right, 1] < data[left, 0]:
        if data[left, 0] == last:
            data[left, 0] *= count
            left += 1
        right += 1
    elif data[right, 1] > data[left, 0]:
        data[left, 0] *= count
        left += 1
    else:
        count += 1
        right += 1
        last = data[left, 0]

print(int(np.sum(data[:,0])))
