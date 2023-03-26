import sys
import functools
# for file in sys.argv[1:]:

# print(list(filter(lambda x: not(int(x) % 2), list(open(file, 'r').read().replace('\n', ' ').split() for file in sys.argv[1:]))))
print(len(
    list(filter(
        lambda x: not(int(x) % 2),list(functools.reduce(
            lambda x, y: x + y, list(open(file, 'r').read().split() for file in sys.argv[1:])
            )
        ))
    )
))

print(len(
    list(filter(
        lambda x: not(int(x) % 2),list(functools.reduce(
            lambda x, y: x + y, list(map(lambda x: open(x, 'r').read(), sys.argv[1:]))).split()
            )
        ))
    )
)


# python3 -c "import sys;import functools;print(len(list(filter(lambda x: not(int(x)%2),list(functools.reduce(lambda x, y: x + y, list(open(file, 'r').read().split() for file in sys.argv[1:])))))))" plik1.txt plik2.txt


# python3 -c "import sys;import functools;print(len(list(filter(lambda x: not(int(x) % 2),list(functools.reduce(lambda x, y: x + y, list(map(lambda x: open(x, 'r').read(), sys.argv[1:]))).split())))))" plik1.txt plik2.txt