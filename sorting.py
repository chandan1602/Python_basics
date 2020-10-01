size = 12
arr = [2,4,7,12,45,34,21,67,5,43]
def bubblesort(arr):
    for i in range(0, size, 1):
        for j in range(0, size-2, 1):
            if(arr[i] > arr[j]):
                arr[i] = arr[i] + arr[j]
                arr[j] = arr[i] - arr[j]
                arr[i] = arr[i] - arr[j]

def print(arr):
    for i in range(0,size,1):
        print(arr[i])

if __name__=='__main__':
    bubblesort(arr)
    print(arr)
