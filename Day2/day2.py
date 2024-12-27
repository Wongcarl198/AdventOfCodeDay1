file = open("C:/self/AdventOfCode2024/Day2/day2Data.txt", "r")
raw_data = file.read()
data = raw_data.split("\n")

for i in range(0, len(data)):
    data[i] = data[i].split()

int_data = []
safe_data_list = []

for data_set in data:
    int_list = [int(s) for s in data_set]

    int_data.append(int_list) 


def part_one(data_point):
    # Check if the differences are within 1 and 3
    differences = [abs(data_point[i] - data_point[i+1]) for i in range(len(data_point) - 1)]
    if not all(1 <= diff <= 3 for diff in differences):
        return False
    
    # Check if the sequence is strictly increasing or decreasing
    if all(data_point[i] <= data_point[i+1] for i in range(len(data_point) - 1)) or all(data_point[i] >= data_point[i+1] for i in range(len(data_point) - 1)):
        return True

    return False

def part_two(data_point):
    if part_one(data_point):
        return True
    
    for i in range(len(data_point)):
        modified_data = data_point[:i] + data_point[i+1:]
        if part_one(modified_data):
            return True

    return False
# for data_points in int_data:
#     safe_data = part_one(data_points)
#     safe_data_list.append(safe_data)

safe_data_list = [part_two(data_points) for data_points in int_data]

print(sum(safe_data_list))
# print(int_data)