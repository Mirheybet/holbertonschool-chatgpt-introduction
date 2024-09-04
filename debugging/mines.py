#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.first_move = True

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if self.first_move:
            self.first_move = False
            if (y * self.width + x) in self.mines:
                self.mines.remove(y * self.width + x)
                # Reassign a new mine position
                new_mine_pos = random.choice(
                    [i for i in range(self.width * self.height) if i not in self.mines and i != y * self.width + x]
                )
                self.mines.add(new_mine_pos)

        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        return all(
            self.revealed[y][x] or (y * self.width + x) in self.mines
            for y in range(self.height)
            for x in range(self.width)
        )

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input(f"Enter x coordinate (0 to {self.width - 1}): "))
                y = int(input(f"Enter y coordinate (0 to {self.height - 1}): "))
                
                if x < 0 or x >= self.width or y < 0 or y >= self.height:
                    print("Coordinates out of bounds. Please try again.")
                    continue
                
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You've cleared the minefield!")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
