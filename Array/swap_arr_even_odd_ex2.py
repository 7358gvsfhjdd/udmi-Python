def minSwapsSummerArray(arr):
    #elper for coputing cost for parity prefrence
    def cost_for_pattern(arr, parityFirst):
        swaps = 0
        pos= 0
        for i in range (len(arr)):
            if arr[i] % 2 == parityFirst:
                swaps+= abs(i-pos)
                pos +=1
            return swaps
        #try two patterns: odd first = 1 or even first (parityFirst=0)
        odd_first = cost_for_pattern(arr,1)
        even_first = cost_for_pattern(arr,0)
        return min(odd_first,even_first)
    
    n = int(input().strip)
    arr = list(map(int,input().strip().split()))
    print(minSwapsSummerArray(arr))
    minSwapsSummerArray(arr)
