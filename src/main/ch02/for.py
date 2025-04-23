#범위 생성 함수 range()
r = range(10)
print(r)
rList = list(r)
print(rList)
r2 = range(5, 10)
print(r2)
print(list(r2))
r3 = range(0, 10, 4)
print(r3)
print(list(r3))

for num in range(10):
    print(num)

for num in [1,2,3,4]:
    print(num)

studentDict = {
    "name": "김준일",
    "age": 32,
    "address": "부산 동래구"
}

studentItems = studentDict.items()
print(studentItems)
for key, value in studentItems:
    print(key, value)


"""
2 x 1 = 2\t2 x 2 = 4\t ...
3 x 1 = 3\t3 x 2 = 6\t ...
...
"""

for dan in range(2, 10):
    for n in range(1, 10):
        print(f"{dan} x {n} = {dan * n}", end="\t")
    print()
