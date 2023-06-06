# basic test
s = {1}
print(s.remove(1))
print(list(s))
try:
    print(s.remove(1), "!!!")
except KeyError as er:
    print('KeyError', er.args[0])
else:
    print("failed to raise KeyError")

# test sets of varying size
for n in range(20):
    print(f'testing set with {n} items')
    for i in range(n):
        s = {str(j) for j in range(n)}
        print(len(s))

        # delete an item
        s.remove(str(i))
        print(len(s))

        # check items
        for j in range(n):
            if str(j) in s:
                if j == i:
                    print(j, 'in s, but it should not be')
            elif j != i:
                print(j, 'not in s, but it should be')
