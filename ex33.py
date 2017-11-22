
numbers = []


def while_loop(n, k):
    i = 0
    for i in range(0, n, k):

        # while i < n:

        print "At the top i is %d" % i
        numbers.append(i)

        #i = i + k
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i


while_loop(8, 2)
print "The numbers:"
for num in numbers:
    print num
