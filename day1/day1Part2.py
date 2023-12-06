def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

spelled_out = [
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
]

def solve(data) -> int:
  data = data.strip().split("\n")
  calibration_value = ""
  calibration_list = []
  for line in data:
    first_value = ""
    last_value = ""
    start_char = 0
    end_char = len(line)
    length = len(line)-1
    for i in range(len(line)):
      for number in spelled_out:
        if number in line[start_char:i] and (first_value == ""):
          first_value = str(spelled_out.index(number) + 1)
          start_char = i
        if number in line[length - i:end_char] and (last_value == ""):
          last_value = str(spelled_out.index(number) + 1)
          end_char = length - i

      # Check for numbers
      if line[i].isnumeric() and (first_value == ""):
        first_value = line[i]
      if line[length - i].isnumeric() and (last_value == ""):
        last_value = line[length - i]

      if first_value != "" and last_value != "":
        calibration_value = first_value + last_value
        calibration_list.append(int(calibration_value))
        break
  return sum(calibration_list)


if __name__ == '__main__':
  main()
