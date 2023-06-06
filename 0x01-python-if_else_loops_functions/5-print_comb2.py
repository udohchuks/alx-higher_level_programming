#!/usr/bin/python3
end = ', '
for i in range(100):
    if i == 99:
        end = ''
    print("{:02d}".format(i), end=end)
print("")
