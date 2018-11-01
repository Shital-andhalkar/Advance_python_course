items=[1,2,3,4,5,6,7]
temp = [oct(i) if i % 2 else bin(i)for i in items]
print(temp)

print(items[items.index(4)+1:])

temp1={i:hex(i)for i in range(10)}
print(temp1)
print()

temp2={hex(i) for i in range(10)}
print(temp2)