import sys
import collections

# print(sys.stdin.read().split())
# print(sys.stdin.read().split())
# for i in sys.stdin.read().split():
#     print(i)
#     print(len(i))
# print(sys.stdin.read())
# print(sys.stdin.readline())
# print(sys.stdin.readlines())

  
# print(collections.Counter(len(x) for x in sys.stdin.read().split()))


# print(
#     dict(
#         sorted(collections.Counter(
#             [len(x) for x in sys.stdin.read().split()]).items()
#         )
#     )
# )


print(collections.Counter(len(x) for x in sys.stdin.read().split()))


print(dict(sorted(collections.Counter(map(lambda x: len(x), sys.stdin.read().split())).items())))

# python3 -c "import sys; import collections; print(collections.Counter(len(x) for x in sys.stdin.read().split()))"
# python3 -c "import sys; import collections; print(dict(collections.Counter(map(lambda x: len(x), sys.stdin.read().split()))))"
#1 1 
