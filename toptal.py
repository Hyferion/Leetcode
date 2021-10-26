import re


def solution(A, B, P):
    matches = []
    for i in range(len(B)):
        if P in B[i]:
            matches.append(A[i])

    # Sort names

    return (sorted(matches, key=str.lower)[0])


# print(solution(['pim', 'pom'], ["999999999","777888999"],"88999"))


def solution_1(S):
    # Remove whitespace and dashes
    st = "".join(S.split())
    st = "".join(st.split(sep="-"))

    solution = ""

    for index, k in enumerate(st):
        if index + 4 > len(st):
            if (index % 2) == 0 and index != 0:
                solution = solution + "-"
        else:
            if (index % 3) == 0 and index != 0:
                solution = solution + "-"
        solution = solution + str(k)
    return solution


print(solution_1("555372654"))


def solution_2(N, A, B):
    last = N
    current_node = 1

    limiter = 0
    while not current_node == last and limiter < 2:
        limiter += 1
        for i in range(len(A)):
            if A[i] == current_node:
                if B[i] == A[i] + 1:
                    current_node = B[i]
                    limiter = 0
            elif B[i] == current_node:
                if A[i] == B[i] + 1:
                    current_node = A[i]
                    limiter = 0

    if current_node == last:
        return True
    else:
        return False


#print(solution_2(4, [1, 2, 1, 3], [2, 4, 3, 4]))


def solution_l(Y, A, B, W):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    length_of_months = [31, (28,29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    index_first_of_year = days.index(W)
