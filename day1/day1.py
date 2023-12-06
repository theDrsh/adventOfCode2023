def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data) -> int:
  data = data.split("\n")[0:-1]
  calibration_value = ""
  calibration_list = []
  first_value = ""
  last_value = ""
  for line in data:
    for character in line:
      if character.isnumeric():
        if first_value == "":
          first_value = character
        else:
          last_value = character
    if last_value == "":
      calibration_value = first_value + first_value
    else:
      calibration_value = first_value + last_value
    calibration_list.append(int(calibration_value))
    first_value = ""
    last_value = ""
  return sum(calibration_list)


if __name__ == '__main__':
  main()
