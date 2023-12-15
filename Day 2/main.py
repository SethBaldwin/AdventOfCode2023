# 12 red cubes, 13 green cubes, and 14 blue cubes
cube_count = {"red": 12,
              "green": 13,
              "blue": 14}

def cubeConundrum():
    with open('input', 'r') as file:
        # Read file line by line
        game_number = 1
        answer = 0
        for line in file:
            game = line.split(':')
            sets = game[1].split(';')
            for set in sets:
                set_result = getSetResults(set)
                if not isPossible(set_result):
                    break
                if set == sets[-1]:
                    # if we make it to the last set and all previous sets were possible we can add this game to the answer sum.
                    answer += game_number

            game_number += 1
        
        return answer
    
# Will take in one "set". 1 of 3 in a game line
# input: game set. "1 blue, 2 green, 3 red"
# returns: Dict of set results. {'blue': 1, 'green': 2, 'red': 3}
def getSetResults(set):
    # a set should come in the form: 1 blue, 2 green, 3 red
    sets = set.split(',')
    results = {}
    for i in range(len(sets)):
        cubes = sets[i].strip()
        cubes = cubes.split(' ')
        results[cubes[1]] = int(cubes[0])
    
    return results

# input: {'blue': 1, 'green': 2, 'red': 3}
# returns: Bool
def isPossible(set_results):
    for item in set_results:
        if item in cube_count:
            if set_results[item] > cube_count[item]:
                return False
    return True


print(cubeConundrum())

### Cube Conundrum

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

## Part 3 Look at the data and determine impossible games
