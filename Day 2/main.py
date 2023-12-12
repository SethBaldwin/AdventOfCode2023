# 12 red cubes, 13 green cubes, and 14 blue cubes
cube_count = {"red": 12,
              "green": 13,
              "blue": 14}

def cubeConundrum():
    with open('input', 'r') as file:
        # Read file line by line
        for line in file:
            print(line)



# cubeConundrum()

## Part 1 Store data
# Lets think about how to organize our data
# we'll have a list of games, sure.
# each game has 3 possible values
# num red cubes
# num green cubes
# num blue cubes
# We can create an object to track those.
# Maybe a tuple? my_tuple = (1, 2, 3, 'a', 'b', 'c')
# Its that or a class, we'll see

## Part 2 Parse data
# We are guaranteed 3 special characters per line (i dont feel good about how dependent i am on these special characters, smile)
# : ; ;
# We can easily use these to separate each round
# How do we get the number and color value from each group

def getSetResults(set):
    # a set should come in the form: 1 blue, 2 green, 3 red
    sets = set.split(',')
    results = []
    for i in range(len(sets)):
        cubes = sets[i].strip()
        results.append(cubes.split(' '))
    
    return results

#print(getSetResults(" 1 blue, 2 green, 3 red"))
print("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green".split(':'))


## Part 3 Look at the data and determine impossible games
