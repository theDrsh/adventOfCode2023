def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data) -> int:
  data = data.split("\n")[0:-1]
  set_of_powers = []
  for game in data:
    red_limit = 0
    blue_limit = 0
    green_limit = 0
    game_power = 0
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
            red_limit = number_cubes
        elif color_cubes == "blue":
          if number_cubes > blue_limit:
            blue_limit = number_cubes
        elif color_cubes == "green":
          if number_cubes > green_limit:
            green_limit = number_cubes
    game_power = red_limit * blue_limit * green_limit
    set_of_powers.append(game_power)
  return sum(set_of_powers)


if __name__ == '__main__':
  main()
