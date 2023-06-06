#!/usr/bin/python3
end = ", "
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8:
            end = ""
        print("{}{}".format(i, j), end=end)
print("")
