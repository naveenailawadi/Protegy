orange = {'name': 'orange', 'juice_type': 'orange juice'}
apple = {'name': 'macintosh', 'juice_type': 'apple juice'}
grape = {'name': 'grape', 'juice_type': 'grape juice'}
rock = {'name': 'rock', 'juice_type': 'no juice'}


def juicer(fruit):
    juice = fruit['juice_type']
    return juice


oj = juicer(orange)
aj = juicer(apple)
gj = juicer(grape)
nj = juicer(rock)


# print all the juices!
print(oj)
print(aj)
print(gj)
print(nj)
