name = 'Zed A. Shaw'
age = 35  # it's a lie
height = 74.0 * 2.54  # inches
# round() si she wu ru
weight = round(180 * 0.4536)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %.1f inches tall." % height
print "he's %r pounds heavy" % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky,try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
