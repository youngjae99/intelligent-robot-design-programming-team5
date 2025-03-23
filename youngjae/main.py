import time
from collections import deque

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output, display


def robot_search_animation(grid, start_row=0, start_col=0):
    rows, cols = 4, 6
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # 상하좌우 이동 방향
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 시각화를 위한 배열
    visual_grid = np.zeros((rows, cols, 3))
    
    # 그리드 색상 초기화
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:  # 빈 공간
                visual_grid[r, c] = [1, 1, 1]  # 흰색
            elif grid[r][c] == 1:  # 장애물(Box)
                visual_grid[r, c] = [0.6, 0.4, 0.2]  # 갈색
            elif grid[r][c] == 2:  # RedCell
                visual_grid[r, c] = [1, 0, 0]  # 빨간색
    
    # 로봇 위치, 방문한 위치 시각화 함수
    def update_visual_grid(robot_pos, visited_cells):
        visual_copy = visual_grid.copy()
        
        # 방문한 위치 표시
        for r, c in visited_cells:
            if grid[r][c] != 1 and grid[r][c] != 2:  # 장애물이나 RedCell이 아닌 경우
                visual_copy[r, c] = [0.8, 0.8, 1]  # 연한 파란색
        
        # 로봇 위치 표시
        r, c = robot_pos
        visual_copy[r, c] = [0, 0, 1]  # 파란색
        
        return visual_copy
    
    # 두 위치 간의 맨해튼 거리 계산
    def manhattan_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    # BFS로 두 위치 간의 최단 경로 찾기
    def find_path(start, end):
        if start == end:
            return []
            
        queue = deque([start])
        path_parent = {start: None}
        
        while queue:
            current = queue.popleft()
            
            if current == end:
                # 경로 역추적
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
        
        return []  # 경로가 없는 경우
    
    # 로봇 상태 변수
    robot_pos = (start_row, start_col)
    start_pos = (start_row, start_col)  # 시작 위치 저장
    visited_cells = [(start_row, start_col)]
    visited[start_row][start_col] = True
    red_cells_found = 0
    red_cell_positions = []
    
    # 각 단계별 애니메이션 프레임
    frames = []
    
    # 초기 상태 (시작 위치)
    frames.append(update_visual_grid(robot_pos, visited_cells))
    
    # 방문할 수 있는 모든 셀 찾기
    all_reachable_cells = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1:  # 장애물이 아니면
                all_reachable_cells.append((r, c))
    
    # 로봇이 이동하며 탐색
    search_complete = False
    returning_to_start = False
    
    while not search_complete:
        if not returning_to_start:
            # RedCell을 모두 찾았는지 확인
            if red_cells_found >= 2:
                print("모든 RedCell을 찾았습니다. 원점으로 돌아갑니다.")
                returning_to_start = True
                # 원점으로 가는 경로 찾기
                return_path = find_path(robot_pos, start_pos)
                
                if not return_path:
                    print("원점으로 돌아가는 경로를 찾을 수 없습니다.")
                    search_complete = True
                    continue
                
                # 원점으로 돌아가기
                for next_pos in return_path:
                    # 로봇 이동
                    robot_pos = next_pos
                    if next_pos not in visited_cells:
                        visited_cells.append(next_pos)
                    
                    # 프레임 추가
                    frames.append(update_visual_grid(robot_pos, visited_cells))
                
                # 원점 도착 메시지
                print(f"원점 ({start_pos[0]}, {start_pos[1]})에 도착했습니다.")
                search_complete = True
                continue
            
            # 다음 방문할 위치 찾기 (가장 가까운 미방문 위치)
            next_target = None
            min_distance = float('inf')
            
            for cell in all_reachable_cells:
                r, c = cell
                # 이미 방문했거나 장애물이면 건너뛰기
                if visited[r][c] or grid[r][c] == 1:
                    continue
                    
                # 현재 로봇 위치에서의 거리 계산
                dist = manhattan_distance(robot_pos, cell)
                if dist < min_distance:
                    min_distance = dist
                    next_target = cell
            
            # 더 이상 방문할 위치가 없으면 RedCell 탐색 종료
            if next_target is None:
                print("모든 도달 가능한 위치를 탐색했습니다.")
                
                # RedCell을 모두 찾았으면 원점으로 돌아가기
                if red_cells_found >= 2:
                    returning_to_start = True
                    continue
                else:
                    search_complete = True
                    continue
            
            # 목표 위치까지의 경로 찾기
            path = find_path(robot_pos, next_target)
            
            # 경로가 없으면 다음 위치로
            if not path:
                print(f"위치 {next_target}까지 경로를 찾을 수 없습니다.")
                # 다음에 재방문하지 않도록 표시
                r, c = next_target
                visited[r][c] = True
                continue
            
            # 경로를 따라 이동
            for next_pos in path:
                # 로봇 이동
                robot_pos = next_pos
                r, c = next_pos
                
                if not visited[r][c]:
                    visited[r][c] = True
                    visited_cells.append(next_pos)
                
                # 프레임 추가
                frames.append(update_visual_grid(robot_pos, visited_cells))
                
                # RedCell 확인
                if grid[r][c] == 2 and next_pos not in red_cell_positions:
                    red_cells_found += 1
                    red_cell_positions.append(next_pos)
                    print(f"RedCell 발견! 위치: {next_pos}")
    
    print(f"총 {len(frames)} 프레임의 애니메이션이 생성되었습니다")
    
    # matplotlib 애니메이션 실행
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 애니메이션 함수
    def update(frame_num):
        if frame_num < len(frames):
            ax.clear()
            ax.imshow(frames[frame_num])
            
            # 그리드 라인 추가
            ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
            ax.set_xticks(np.arange(-0.5, cols, 1))
            ax.set_yticks(np.arange(-0.5, rows, 1))
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            
            # 제목 업데이트
            found_cells = sum(1 for pos in red_cell_positions if pos in visited_cells[:frame_num+1])
            
            # 모든 RedCell을 찾은 후 원점으로 돌아가는 상태 표시
            if found_cells == 2 and frame_num >= len(frames) - len(find_path(red_cell_positions[-1], start_pos)):
                ax.set_title(f"RedCell: {found_cells}/2 - 원점으로 돌아가는 중")
            else:
                ax.set_title(f"로봇 탐색 (RedCell: {found_cells}/2)")
    
    # 범례 추가
    import matplotlib.patches as mpatches
    legend_elements = [
        mpatches.Patch(color='white', label='빈 공간'),
        mpatches.Patch(color='brown', label='장애물(Box)'),
        mpatches.Patch(color='red', label='RedCell'),
        mpatches.Patch(color='blue', label='로봇'),
        mpatches.Patch(color=[0.8, 0.8, 1], label='방문한 위치')
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1, 1))
    
    # 애니메이션 생성
    anim = animation.FuncAnimation(
        fig, update, frames=len(frames), interval=500, repeat=False)
    
    plt.tight_layout()
    plt.show()
    
    return anim, red_cell_positions

# 테스트 코드
if __name__ == "__main__":
    # 예: 0은 빈 공간, 1은 장애물(Box), 2는 RedCell
    grid = [
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 2],  # RedCell 하나
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 2, 0, 0]   # RedCell 하나 더
    ]
    
    # 애니메이션 실행
    anim, found_positions = robot_search_animation(grid)
