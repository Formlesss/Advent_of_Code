example_1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
example_2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
example_3 = 'nppdvjthqldpwncqszvftbrmjlhg'
example_4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
example_5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

def find_marker(data):
    for i in range(0,len(data)):
        if len(set(data[i:i+4])) == 4:
            return i + 4

def find_message(data):
    for i in range(0,len(data)):
        if len(set(data[i:i+14])) == 14:
            return i + 14

with open('input.txt') as f:
    data = f.readlines()

print(find_marker(example_1))
print(find_marker(example_2))
print(find_marker(example_3))
print(find_marker(example_4))
print(find_marker(example_5))
print(find_marker(data[0]))

print(find_message(example_1))
print(find_message(example_2))
print(find_message(example_3))
print(find_message(example_4))
print(find_message(example_5))
print(find_message(data[0]))