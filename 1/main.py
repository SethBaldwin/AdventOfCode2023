num_dic = {"one": "1",
           "two": "2",
           "three": "3",
           "four": "4",
           "five": "5",
           "six": "6",
           "seven": "7",
           "eight": "8",
           "nine": "9"}

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def trebuchet():
    sum = 0
    with open('input', 'r') as file:
        # Read file line by line
        for line in file:
            num_list = []

            # Starting from the beginning of a line, we will look at each char and then add each subsequent char until
            # the resulting string contains one of the text numbers, or it reaches the end of the line.
            # It will short circuit, continue, if the current char is ever a digit
            # If it finds a digit or a string number, it will add the digit to the number list
            for i in range(len(line)):
                temp_string = ''
                cur_char = line[i]
                if cur_char.isdigit():
                    num_list.append(cur_char)
                    continue

                # Since two string numbers can overlap, e.g "twone" I cant match "two" and proceed to "n"
                # because "one" would be missed. Therefor I look at each char in a line as a starting char
                for char in line[i:]:
                    temp_string += char
                    if temp_string in nums:
                        num_list.append(num_dic[temp_string])
                        break

            # Take the first and last found num char and combine them into one num, convert to int, add to sum
            num_builder = num_list[0] + num_list[-1]
            sum += int(num_builder)
        return sum

print(trebuchet())






# def last_num(line):
#     num_list = []
#     for i in range(len(line)):
#         temp_string = ''
#         cur_char = line[i]
#         print(cur_char)
#         if cur_char.isdigit():
#             num_list.append(cur_char)
#             continue

#         for char in line[i:]:
#             temp_string += char
#             if temp_string in nums:
#                 num_list.append(num_dic[temp_string])
#                 break

#     return num_list