'''
f(0) = 0
f(1) = 1 
f(n) = 9*f(n-1) - 4*f(n-2) for all n > 1.
def is_part_of_series(lst):

Solution:
create forward list from first two integers by f(n) = 9*f(n-1) - 4*f(n-2)
then reate backward list from last two integers by f(n-2) = (9*f(n-1) - f(n)) / 4
finally compare both list, if both equal they are part of series of given expression
for reconformation compare either one to original given sorted list. 
'''

def backward(a, b, n):
    l = [a, b]
    while n-2 > 0:
        c = ( (9 * a) - b) / 4
        if c < 0:
            return l
        l = [c] + l
        b = a
        a = c
        n -= 1
    return l

def forward(a, b, n):
    l = [a, b]
    i = 0
    while i < n-2:
        c = 9*b - 4*a
        if c < 0:
            return l
        l.append(c)
        a = b
        b = c
        i += 1 
    return l

def is_part_of_series(lst):

    if lst[0] < 0:
        return False

    n = len(lst)
    series_by_first_two_inetegrs = forward(lst[0], lst[1], n)
    series_by_last_two_inetegrs = backward(lst[-2], lst[-1], n)
    # print(series_by_first_two_inetegrs)
    # print(series_by_last_two_inetegrs)
    if series_by_first_two_inetegrs == series_by_last_two_inetegrs:
        if series_by_first_two_inetegrs == lst:
            return True
    return False

if __name__ == '__main__':

    print('Enter number of integers')
    lst = [int(i) for i in input().split()]
    lst.sort()
    print(is_part_of_series(lst))