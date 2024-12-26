file = open("C:/self/AdventOfCode2024/Day1/day1Data.txt", "r")
raw_data = file.read()

left_values = []
right_values = []
total_distances = []
similarity_score = []

data = raw_data.split()


for i in range(0,len(data), 2):
    left_values.append(int(data[i]))
    right_values.append(int(data[i+1]))

sorted_left_values = sorted(left_values)
sorted_right_values = sorted(right_values)


#part 1
def part_one():
    for i in range(0, len(sorted_left_values)):
        distance = abs(sorted_left_values[i] - sorted_right_values[i])
        total_distances.append(distance)

    print(sum(total_distances))


#part 2
def part_two():
    for i in range(0, len(sorted_left_values)):
        occurrence = sorted_right_values.count(sorted_left_values[i])
        similarity_score.append(sorted_left_values[i] * occurrence)

    print(sum(similarity_score))

    
part_one()
part_two()
file.close()