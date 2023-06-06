for n in range(20):
    print(f'testing dict with {n} items')
    for i in range(n):
        d = {str(j): j for j in range(n)}
        print(len(d))

        # delete an item
        del d[str(i)]
        print(len(d))

        # check items
        for j in range(n):
            if str(j) in d:
                if j == i:
                    print(j, 'in d, but it should not be')
            elif j != i:
                print(j, 'not in d, but it should be')
