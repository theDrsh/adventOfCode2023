def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data) -> int:
  data = data.split("\n")[0:-1]
  total_of_impossible_games = 0
  red_limit = 12
  green_limit = 13
  blue_limit = 14
  for game in data:
    game_possible = True
    game_num_text = game.split(":")[0]
    game_num = int(game_num_text.split(" ")[-1])
    game_text = game.split(":")[-1]
    cube_pulls = game_text.split(";")
    for cube_pull in cube_pulls:
      cube_nums = cube_pull.split(", ")
      for num_color in cube_nums:
        num_color = num_color.strip()
        number_cubes = int(num_color.split(" ")[0])
        color_cubes = num_color.split(" ")[-1]
        if color_cubes == "red":
          if number_cubes > red_limit:
            game_possible = False
        elif color_cubes == "blue":
          if number_cubes > blue_limit:
            game_possible = False
        elif color_cubes == "green":
          if number_cubes > green_limit:
            game_possible = False
    if game_possible:
      total_of_impossible_games += game_num
  return total_of_impossible_games


if __name__ == '__main__':
  main()
