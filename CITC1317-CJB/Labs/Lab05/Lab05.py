#C.J. Bales
#CITC1317
#Lab05
#cbales6@stumail.northeaststate.edu
#9/25/24
import random

def teleport_cat(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = False

    columns = random.randint(0,999)
    rows = random.randint(0,999)
    grid[columns][rows] = True
    return (columns,rows)
# set all values in the grid to False. Pick a randomly generated location (indices) in the grid and set the value at that location to True

def find_cat(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                return (i,j)
# perform a linear search on the grid, return the index values as a tuple in (row,col) form, such as (0, 3).

def main():
    grid = [ [False for cat in range(1000)] for cat in range(1000)]

    for cat in range(5):
        tpKitty = teleport_cat(grid)  # Teleport the cat
        newCat = find_cat(grid)  # Find the cat
        
        print(f"The kitty cat is at {newCat} :)")
main()