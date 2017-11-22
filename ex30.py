people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars"
elif cars < people:
    # if there are many 'elif' blocks ,only the first 'True' one will be exected
    print "We should not take the cars"
# elif buses < cars:
    # print "Nothing"
else:
    print "We catn't decide"

if buses > cars:
    print "That's too many buses"
elif buses < cars:
    print "Maybe we could take the buses"
else:
    print "we still can't decide"

if people > buses:
    print "Alright,let's just take the buses"
else:
    print "fine,let's sray home then"
