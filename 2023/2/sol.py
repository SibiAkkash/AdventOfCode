bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def parse_game(game: str) -> tuple[int, list[list[str]]]:
    # input of the form: Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    '''
    {
    game_no: [
                ["3 blue", "4 red", "5 green"],
                ["2 red", "1 green"],
                ["15 green"],
            ]
    }
    '''
    game_no_str, sets = game.split(": ")
    game_no = int(game_no_str.split(" ")[1])
    
    sets = sets.split('; ')
    
    parts: list[list[str]] = []
    
    for set in sets:
        cubes = set.split(", ")  # ["3 blue", "4 red", "10 green"]
        parts.append(cubes)
        
    return game_no, parts
    

def is_possible_game(game: str) -> int:
    """ Return the game number if its a possible game, else 0"""

    game_no, parts = parse_game(game)

    for part in parts:
        for cube_color_and_count in part:
            cube_count, cube_color = cube_color_and_count.split(" ")
            
            if (cube_color not in bag) or (int(cube_count) > bag[cube_color]):
                return 0

    return game_no


def game_power(game: str) -> int:
    _, parts = parse_game(game)
    
    min_count_required = {
        "blue": 0,
        "red": 0,
        "green": 0
    }
    for part in parts:
        for cube_color_and_count in part:
            cube_count, cube_color = cube_color_and_count.split(" ")
            min_count_required[cube_color] = max(min_count_required[cube_color], int(cube_count))
        
    
    return min_count_required["blue"] * min_count_required["red"] * min_count_required["green"]
        
        

with open('./input.txt', 'r') as file:
    sum_of_possible_games = 0
    sum_of_game_powers = 0
    
    for line in file.readlines():
        # sum_of_possible_games += is_possible_game(line.strip())
        sum_of_game_powers += game_power(line.strip())
        
    # print(sum_of_possible_games)
    print(sum_of_game_powers)