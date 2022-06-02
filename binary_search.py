def binary_search(list,item):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        guess=list[mid]
        if guess == item:
            return f"{item} was found in the list"
        elif guess>item:
            high=mid-1
        else:
            low=mid+1
    return f"{item} was not found in the list"

ans = binary_search(list(range(100)),33)
print(ans)
