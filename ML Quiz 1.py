import array as arr

def number1():
    tribonacci = arr.array("i", [1, 1, 2])
    for i in range (3,37):
        tribonacci.append(tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3])

    test_case = int(input())
    for i in range(0,test_case):
        x = int(input())
        print(tribonacci[x])

def number2():

    def findPairs(lst, K):
        res = []
        while lst:
            num = lst.pop()
            diff = K - num
            if diff in lst:
                res.append((diff, num))

        res.reverse()
        if len(res) >= 1:
            return "YA"
        else:
            return "TIDAK"

    # Driver code

    test_case = int(input())
    lst = []
    K = int(input())
    for i in range(0,test_case):
        x = int(input())
        lst.append(x)
    print(findPairs(lst, K))

def number3():
    test_case = int(input())
    list1 = []

    for i in range(0,test_case):
        value = int(input())
        list1.append(value)

    print(list1)

    list2 = list(set(list1))
    list2.sort()

    print(list2)
    print(list2[-2])

    if (list2[-2] == 0):
        for y in range(0, test_case):

            k = 0
            if (list1[y] - list2[-1]) <= 0:
                list1[y] = abs(list2[-1] - list1[y])
                list1[y] += k
                k = list1[y]
            else:
                list1[y] = 0

    elif (list2[-2]<list2[-1]):
        for x in range(0,test_case):

            j = 0
            if (list1[x] - list2[-2]) <= 0:
                list1[x] = abs(list2[-2] - list1[x])
                list1[x] += j
                j = list1[x]
            else:
                list1[x] = 0

    print(list1)

    total = 0
    for element in range(0,len(list1)):
        total = total + list1[element]

    print(total)

number3()

