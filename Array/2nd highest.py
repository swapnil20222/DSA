def second_highest(a, n):
    a.sort()
    second_hig = 0

    for i in range(n-2, -1, -1):
        if a[i] != a[n - 1]:
            second_hig = a[i]
            break

    return second_hig

a = [12, 35, 1, 10, 348, 1]
n = len(a)
answer = second_highest(a, n)
print("The second highest element in the array is: ", answer)

