# V1 RIP
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
        # Read the entire content of the file
        # file_content = file.read()
        for line in file:
            temp_string = ''
            num_list = []
            for char in line:
                temp_string += char
                #print(temp_string)
                if char.isdigit():
                    num_list.append(char)
                    temp_string = ''
                elif temp_string.isdigit():
                    num_list.append(temp_string)
                    temp_string = ''
                elif temp_string in num_dic:
                    num_list.append(num_dic[temp_string])
                    temp_string = ''
                else:
                    # This case checks if a and of the number strings has been formed within the temp string
                    for num in nums:
                        if num in temp_string:
                            num_list.append(num_dic[num])
                            temp_string = ''
            
            num_builder = num_list[0] + num_list[-1]
            print(num_builder)
            sum += int(num_builder)

        return sum