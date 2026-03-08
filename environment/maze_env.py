# ── MAZE CONSTANTS ───────────────────────────────────────
ROWS = 16          # int   — number of rows in maze
COLS = 16          # int   — number of columns
WALL = 1           # int   — a cell that is blocked
FREE = 0           # int   — a cell the agent can walk on

maze_name = "default_maze"   # str  — name of this maze
is_solved = False             # bool — has agent reached goal?

print(ROWS)
print(type(ROWS))
print(maze_name)
print(type(is_solved))

# ── WALL COLLISION LOGIC ─────────────────────────────────
def check_cell(cell_value):
    if cell_value == WALL:
        print("🚫 Wall! Agent cannot move here. Penalty: -1.0")
    elif cell_value == FREE:
        print("✅ Free cell! Agent can move here. Reward: +1.0")
    else:
        print("❓ Unknown cell type")

# Test it
check_cell(1)   # should hit WALL
check_cell(0)   # should hit FREE
check_cell(9)   # should hit unknown

# ── BUILD A SIMPLE MAZE GRID ─────────────────────────────
maze = []

for row in range(ROWS):
    current_row = []
    for col in range(COLS):
        if row == 0 or row == ROWS-1:
            current_row.append(WALL)   # top and bottom walls
        elif col == 0 or col == COLS-1:
            current_row.append(WALL)   # left and right walls
        else:
            current_row.append(FREE)   # everything inside is free
    maze.append(current_row)

# Print maze to terminal
for row in maze:
    print(row)

# ── AGENT WALKING THROUGH MAZE ───────────────────────────
agent_row = 1      # agent starts at row 1
agent_col = 1      # agent starts at col 1
steps = 0          # step counter

print("\nAgent walking right across the maze:")

while agent_col < COLS - 2:          # stop before right wall
    cell = maze[agent_row][agent_col]
    print(f"  Step {steps} → Position ({agent_row},{agent_col}) → ", end="")
    check_cell(cell)
    agent_col += 1
    steps += 1

print(f"\nAgent stopped after {steps} steps.")