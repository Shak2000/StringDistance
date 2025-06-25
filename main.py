class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_distance(self):
        grid = [[0 for i in range(len(self.b) + 1)] for j in range(len(self.a) + 1)]
        for i in range(1, len(self.a) + 1):
            grid[i][0] = i
        for i in range(1, len(self.b) + 1):
            grid[0][i] = i

        for i in range(1, len(self.a) + 1):
            for j in range(1, len(self.b) + 1):
                if self.a[i - 1] == self.b[j - 1]:
                    grid[i][j] = grid[i - 1][j - 1]
                else:
                    grid[i][j] = 1 + min(min(grid[i - 1][j], grid[i][j - 1]), grid[i - 1][j - 1])
        return grid


def main():
    print("Welcome to the string distance calculator!")
    while True:
        user_input = input("Press enter to calculate the distance between two strings or 'quit' to stop the program: ")
        if user_input.lower() == "quit":
            break

        print("Please enter two strings:")
        pair = Pair(input(), input())
        grid = pair.calc_distance()

        string = "  -"
        for i in range(len(pair.b)):
            string += f" {pair.b[i]}"
        print(string)

        string = "-"
        for i in range(len(pair.b) + 1):
            string += f" {i}"
        print(string)

        for i in range(0, len(pair.a)):
            string = f"{pair.a[i]} {i + 1}"
            for j in range(0, len(pair.b)):
                string += f" {grid[i + 1][j + 1]}"
            print(string)


if __name__ == "__main__":
    main()
