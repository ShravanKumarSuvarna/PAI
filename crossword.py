import random

class Crossword:
    def __init__(self, height, width):
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

    def add_word(self, word):
        word = word.upper()
        if len(word) > max(len(self.grid), len(self.grid[0])):
            print(f"Word '{word}' is too long to fit in the grid.")
            return
        directions = [(1, 0), (0, 1)]
        while True:
            direction = random.choice(directions)
            if direction == (1, 0):
                x = random.randint(0, len(self.grid[0]) - 1)
                y = random.randint(0, len(self.grid) - len(word))
            else:
                x = random.randint(0, len(self.grid[0]) - len(word))
                y = random.randint(0, len(self.grid) - 1)
            if all(self.check_fit(word, x + i * direction[0], y + i * direction[1]) for i in range(len(word))):
                for i, letter in enumerate(word):
                    self.grid[y + i * direction[1]][x + i * direction[0]] = letter
                break

    def check_fit(self, word, x, y):
        if x < 0 or y < 0 or x >= len(self.grid[0]) or y >= len(self.grid):
            return False
        return self.grid[y][x] in [' ', word]

    def display(self):
        for row in self.grid:
            print(' '.join(row))


def main():
    crossword = Crossword(12, 12)
    words = ["PYTHON", "ALGORITHM", "PROGRAMMING", "COMPUTER", "LANGUAGE"]
    for word in words:
        crossword.add_word(word)

    crossword.display()


if __name__ == "__main__":
    main()
