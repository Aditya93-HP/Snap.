def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr  
def main():
    arr = list(map(int,input("Enter the array element using space between them:").split()))
    print("original Array :",arr)
    sorted_arr = selection_sort(arr)
    print("Sorted Array:",sorted_arr)
main()
