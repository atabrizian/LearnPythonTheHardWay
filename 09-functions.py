def print_two(*args):
    arg1, arg2 = args
    print "arg1 is %s, arg2 is %s" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1 is %s, arg2 is %s" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %s" % arg1

def print_none():
    print "I got nothing."

print_two("A", "T")
print_two_again("a", "t")
print_one("first")
print_none()