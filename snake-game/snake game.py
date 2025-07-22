import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.game_running = True

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.snake_direction = "Down"
        self.food = self.create_food()

        self.score = 0
        self.score_label = tk.Label(self.root, text="Score: {}".format(self.score), font=("Arial", 12))
        self.score_label.pack()

        self.root.bind("<Up>", self.change_direction)
        self.root.bind("<Down>", self.change_direction)
        self.root.bind("<Left>", self.change_direction)
        self.root.bind("<Right>", self.change_direction)

        self.move_snake()
    
    def create_food(self):
        food_x = random.randint(0, 19) * 20
        food_y = random.randint(0, 19) * 20
        return food_x, food_y

    def move_snake(self):
        if not self.game_running:
            return
        
        head_x, head_y = self.snake[-1]

        if self.snake_direction == "Up":
            head_y -= 20
        elif self.snake_direction == "Down":
            head_y += 20
        elif self.snake_direction == "Left":
            head_x -= 20
        elif self.snake_direction == "Right":
            head_x += 20

        # Check for collisions with walls
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400:
            self.game_over()
            return

        # Check for collisions with self
        if (head_x, head_y) in self.snake:
            self.game_over()
            return

        self.snake.append((head_x, head_y))

        # Check for food
        if (head_x, head_y) == self.food:
            self.score += 1
            self.score_label.config(text="Score: {}".format(self.score))
            self.food = self.create_food()
        else:
            self.snake.pop(0)

        self.update_canvas()
        self.root.after(100, self.move_snake)

    def update_canvas(self):
        self.canvas.delete(tk.ALL)

        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="green")

        food_x, food_y = self.food
        self.canvas.create_rectangle(food_x, food_y, food_x + 20, food_y + 20, fill="red")

    def change_direction(self, event):
        if event.keysym == "Up" and self.snake_direction != "Down":
            self.snake_direction = "Up"
        elif event.keysym == "Down" and self.snake_direction != "Up":
            self.snake_direction = "Down"
        elif event.keysym == "Left" and self.snake_direction != "Right":
            self.snake_direction = "Left"
        elif event.keysym == "Right" and self.snake_direction != "Left":
            self.snake_direction = "Right"

    def game_over(self):
        self.game_running = False
        self.canvas.create_text(200, 200, text="Game Over", fill="red", font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
