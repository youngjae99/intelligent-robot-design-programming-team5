import time
from collections import deque

import matplotlib.animation as animation
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output, display


def robot_search_animation(grid, start_row=0, start_col=0):    
    
    rows, cols = 4, 6
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Up, down, left, right movement directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Array for visualization
    visual_grid = np.zeros((rows, cols, 3))
    
    # Initialize grid colors and print obstacles/RedCells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:  # Empty space
                visual_grid[r, c] = [1, 1, 1]  # White
            elif grid[r][c] == 1:  # Obstacle (Box)
                visual_grid[r, c] = [0.6, 0.4, 0.2]  # Brown
                print(f"({r}, {c}, B)")  # Print Block position
            elif grid[r][c] == 2:  # RedCell
                visual_grid[r, c] = [1, 0, 0]  # Red
                print(f"({r}, {c}, R)")  # Print RedCell position
    
    # Robot position and visited position visualization function
    def update_visual_grid(robot_pos, visited_cells):
        visual_copy = visual_grid.copy()
        
        # Mark visited positions
        for r, c in visited_cells:
            if grid[r][c] != 1 and grid[r][c] != 2:  # If not an obstacle or RedCell
                visual_copy[r, c] = [0.8, 0.8, 1]  # Light blue
        
        # Mark robot position
        r, c = robot_pos
        visual_copy[r, c] = [0, 0, 1]  # Blue
        
        return visual_copy
    
    # Calculate Manhattan distance between two positions
    def manhattan_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    # Find shortest path between two positions using BFS
    def find_path(start, end):
        if start == end:
            return []
            
        queue = deque([start])
        path_parent = {start: None}
        
        while queue:
            current = queue.popleft()
            
            if current == end:
                # Backtrack path
                path = []
                while current != start:
                    path.append(current)
                    current = path_parent[current]
                return list(reversed(path))
            
            for dr, dc in directions:
                next_r, next_c = current[0] + dr, current[1] + dc
                next_pos = (next_r, next_c)
                
                if (0 <= next_r < rows and 0 <= next_c < cols and 
                    next_pos not in path_parent and grid[next_r][next_c] != 1):
                    queue.append(next_pos)
                    path_parent[next_pos] = current
        
        return []  # If no path exists
    
    # Robot status variables
    robot_pos = (start_row, start_col)
    start_pos = (start_row, start_col)  # Store starting position
    visited_cells = [(start_row, start_col)]
    visited[start_row][start_col] = True
    red_cells_found = 0
    red_cell_positions = []
    
    # Animation frames for each step
    frames = []
    
    # Initial state (starting position)
    frames.append(update_visual_grid(robot_pos, visited_cells))
    
    # Find all cells that can be visited
    all_reachable_cells = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1:  # If not an obstacle
                all_reachable_cells.append((r, c))
    
    # Robot moves and explores
    search_complete = False
    returning_to_start = False
    
    while not search_complete:
        if not returning_to_start:
            # Check if all RedCells are found
            if red_cells_found >= 2:
                print("All RedCells found. Returning to origin.")
                returning_to_start = True
                # Find path to origin
                return_path = find_path(robot_pos, start_pos)
                
                if not return_path:
                    print("Cannot find path back to origin.")
                    search_complete = True
                    continue
                
                # Return to origin
                for next_pos in return_path:
                    # Robot movement
                    robot_pos = next_pos
                    if next_pos not in visited_cells:
                        visited_cells.append(next_pos)
                    
                    # Add frame
                    frames.append(update_visual_grid(robot_pos, visited_cells))
                
                # Origin arrival message
                print(f"Arrived at origin ({start_pos[0]}, {start_pos[1]}).")
                search_complete = True
                continue
            
            # Find next position to visit (closest unvisited position)
            next_target = None
            min_distance = float('inf')
            
            for cell in all_reachable_cells:
                r, c = cell
                # Skip if already visited or is an obstacle
                if visited[r][c] or grid[r][c] == 1:
                    continue
                    
                # Calculate distance from current robot position
                dist = manhattan_distance(robot_pos, cell)
                if dist < min_distance:
                    min_distance = dist
                    next_target = cell
            
            # End RedCell search if no more positions to visit
            if next_target is None:
                print("Explored all reachable positions.")
                
                # If all RedCells found, return to origin
                if red_cells_found >= 2:
                    returning_to_start = True
                    continue
                else:
                    search_complete = True
                    continue
            
            # Find path to target position
            path = find_path(robot_pos, next_target)
            
            # If no path, move to next position
            if not path:
                print(f"Cannot find path to position {next_target}.")
                # Mark to avoid revisiting
                r, c = next_target
                visited[r][c] = True
                continue
            
            # Move along the path
            for next_pos in path:
                # Robot movement
                robot_pos = next_pos
                r, c = next_pos
                
                if not visited[r][c]:
                    visited[r][c] = True
                    visited_cells.append(next_pos)
                
                # Add frame
                frames.append(update_visual_grid(robot_pos, visited_cells))
                
                # Check for RedCell
                if grid[r][c] == 2 and next_pos not in red_cell_positions:
                    red_cells_found += 1
                    red_cell_positions.append(next_pos)
                    print(f"({r}, {c}, R)")  # Print RedCell with format (row, col, R)
    
    print(f"Total {len(frames)} animation frames generated.")
    
    # Run matplotlib animation
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Animation function
    def update(frame_num):
        if frame_num < len(frames):
            ax.clear()
            ax.imshow(frames[frame_num])
            
            # Add grid lines
            ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
            ax.set_xticks(np.arange(-0.5, cols, 1))
            ax.set_yticks(np.arange(-0.5, rows, 1))
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            
            # Update title
            found_cells = sum(1 for pos in red_cell_positions if pos in visited_cells[:frame_num+1])

            # Display in English
            if found_cells == 2 and frame_num >= len(frames) - len(find_path(red_cell_positions[-1], start_pos)) - 1:
                ax.set_title(f"RedCell: {found_cells}/2 - Returning to origin")
            else:
                ax.set_title(f"Robot Search (RedCell: {found_cells}/2)")
    
    # Add legend
    import matplotlib.patches as mpatches
    
    legend_elements = [
            mpatches.Patch(color='white', label='Empty'),
            mpatches.Patch(color='brown', label='Box (Obstacle)'),
            mpatches.Patch(color='red', label='RedCell'),
            mpatches.Patch(color='blue', label='Robot'),
            mpatches.Patch(color=[0.8, 0.8, 1], label='Visited')
        ]
    
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
    
    # Create animation
    anim = animation.FuncAnimation(
        fig, update, frames=len(frames), interval=500, repeat=False)
    
    plt.tight_layout()
    plt.show()
    
    return anim, red_cell_positions

# Test code
if __name__ == "__main__":
    # Example: 0 is empty space, 1 is obstacle (Box), 2 is RedCell
    grid = [
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 2],  # One RedCell
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 2, 0, 0]   # One more RedCell
    ]
    
    # Run animation
    anim, found_positions = robot_search_animation(grid)
