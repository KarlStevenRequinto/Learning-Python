heights = [154, 143, 187, 156, 165, 152, 170]
initial_height = 0
count = 0
for height in heights:
    count += 1
    initial_height += height

    print(initial_height, count)
average_height = initial_height / count
print(average_height)
