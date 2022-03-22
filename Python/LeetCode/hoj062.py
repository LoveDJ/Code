import re
def add_x(matched):
    return "*"+matched.group("number")+"*"
in_str = input()
print(re.sub("(?P<number>\d+)", add_x, in_str))



