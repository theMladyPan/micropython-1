# test bignum comparisons

i = 1 << 65
cases = (0, 1, -1, i, -i, i + 1, -(i + 1))

for lhs in cases:
    for rhs in cases:
        print(f"{lhs} == {rhs} = {lhs == rhs}")
        print(f"{lhs} != {rhs} = {lhs != rhs}")
        print(f"{lhs} < {rhs} = {lhs < rhs}")
        print(f"{lhs} > {rhs} = {lhs > rhs}")
        print(f"{lhs} <= {rhs} = {lhs <= rhs}")
        print(f"{lhs} >= {rhs} = {lhs >= rhs}")
