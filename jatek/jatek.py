import time
import sys

def move_cursor(row, col):
    print(f"\033[{row};{col}H", end="")

# Clear screen first
print("\033[2J")

grid = [
    "Row 1: AAA",
    "Row 2: BBB",
    "Row 3: CCC"
]

for i, line in enumerate(grid, start=1):
    print(line)

time.sleep(1)

move_cursor(2, 1)
print("Row 2: UPDATED", end="")
sys.stdout.flush()
