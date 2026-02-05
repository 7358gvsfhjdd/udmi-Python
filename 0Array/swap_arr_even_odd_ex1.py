def min_swaps_even_odd(arr):
    n = len(arr)
    even_pos = []
    odd_pos = []

    for i in range(n):
        if i % 2 == 0 and arr[i] % 2 != 0:
            even_pos.append(i)
        elif i % 2 != 0 and arr[i] % 2 == 0:
            odd_pos.append(i)

    swaps = 0
    for i in range(len(even_pos)):
        arr[even_pos[i]], arr[odd_pos[i]] = arr[odd_pos[i]], arr[even_pos[i]]
        swaps += 1

    return swaps


arr = [3, 2, 1, 4, 5, 6]
print("Minimum swaps:", min_swaps_even_odd(arr))
print("Final array:", arr)
