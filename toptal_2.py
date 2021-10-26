import re


def solution(T, R):
    dic = {}

    for i in range(len(T)):
        n = re.findall("\d", T[i])[0]
        if R[i] != "OK":
            dic[n] = False
        else:
            if n not in dic:
                dic[n] = True

    n_keys = 0
    points = 0
    for key in dic:
        n_keys = n_keys + 1
        if dic[key]:
            points = points + 1

    if points == 0:
        return 0
    else:
        result = (points * 100) / n_keys
        return int(result)


print(solution(["test1a","test2","test1b","test1c", "test3"], ["Wrong answer", "OK", "Runtime error", "OK", "Time limit exceeded"]))


def solution_a(A):
    locations = set(A)

    shortest_vacation = 100001
    for i in range(len(A)):
        x = []
        counter = 0
        for k in range(i, len(A)):
            counter = counter + 1
            if counter > shortest_vacation:
                break

            if set(x) == locations:
                if counter - 1 < shortest_vacation:
                    shortest_vacation = counter - 1
                break
            else:
                x.append(A[k])

    return shortest_vacation





def solution_b(A, s):
    results = []

    for i in range(len(A)):
        x = []
        for k in range(i,len(A)):
            x.append(A[k])
            if (sum(x) / len(x)) == s:
                results.append(x)
                x = x.copy()

    if len(results) > 1000000000:
        return 1000000000
    return results




solution_b([2,1,3], 2)