days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\n"
print "Here are the days: ", days
print "Here are the months: ", months
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
"""

while True:
    for i in ['/', '-', '|', '\\', '|']:
        print "%s\r" % i,
