test = int(input())
for i in range(test):
    R,C = map(int,input().split(' '))
    sol = ''
    j = 0
    while j in range(2 * R + 1):
        k = 0
        tempArr = []
        while k in range(2 * C + 1):
            if j == 0:
                if k < 2:
                    sol += '.'
                if k % 2 == 0 and k > 1:
                    sol += '+'
                if k % 2 != 0 and k > 1:
                    sol += '-'
                k += 1
            if j == 1:
                if k < 2:
                    sol += '.'
                if k > 1 and k%2 == 0:
                    sol += '|'
                if k > 1 and k%2 != 0:
                    sol += '.'
                k += 1
            elif j%2 == 0 and j > 1:
                if k%2 == 0:
                    sol += '+'
                if k%2 != 0:
                    sol += '-'
                k += 1
            elif j%2 != 0 and j > 1:
                if k%2 == 0:
                    sol += '|'
                if k%2 != 0:
                    sol += '.'
                k += 1
        sol += '\n'
        j += 1
    print('Case #' + str(i + 1) + ':\n' + sol)
