# Array operation
# Type: list, map() call. This method requires allocation of
# the same amount of memory as original array (to hold result
# array). On the other hand, input array stays intact.
import bench


def test(num):
    for _ in iter(range(num // 10000)):
        arr = bytearray(b"\0" * 1000)
        arr2 = bytearray(map(lambda x: x + 1, arr))


bench.run(test)
