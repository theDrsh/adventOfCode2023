def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data) -> int:
  data = data.split("\n")
  return 0


if __name__ == '__main__':
  main()
