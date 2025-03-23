import time
from collections import deque

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output, display


def sequential_search(grid):
    rows, cols = 4, 6
    
    for row in range(rows):
        for col in range(cols):
            # 현재 위치 (row, col)에서 작업 수행
            print(f"로봇이 ({row}, {col}) 위치 탐색 중")
            
            # 여기에 실제 로봇 작업 코드 추가
            # 예: 센서 읽기, 데이터 수집 등
            
    print("모든 칸 탐색 완료!")

def zigzag_search(grid):
    rows, cols = 4, 6
    
    for row in range(rows):
        if row % 2 == 0:  # 짝수 행은 왼쪽에서 오른쪽으로
            for col in range(cols):
                print(f"로봇이 ({row}, {col}) 위치 탐색 중")
                # 작업 수행
        else:  # 홀수 행은 오른쪽에서 왼쪽으로
            for col in range(cols-1, -1, -1):
                print(f"로봇이 ({row}, {col}) 위치 탐색 중")
                # 작업 수행
                
    print("모든 칸 탐색 완료!")



def bfs_search(grid, start_row=0, start_col=0):
    rows, cols = 4, 6
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # 상하좌우 이동 방향
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    
    while queue:
        row, col = queue.popleft()
        print(f"로봇이 ({row}, {col}) 위치 탐색 중")
        # 작업 수행
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                not visited[new_row][new_col]):
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
    
    print("모든 칸 탐색 완료!")



def dfs_search(grid, start_row=0, start_col=0):
    rows, cols = 4, 6
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # 상하좌우 이동 방향
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(row, col):
        visited[row][col] = True
        print(f"로봇이 ({row}, {col}) 위치 탐색 중")
        # 작업 수행
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                not visited[new_row][new_col]):
                dfs(new_row, new_col)
    
    dfs(start_row, start_col)
    print("모든 칸 탐색 완료!")

def spiral_search(grid):
    rows, cols = 4, 6
    
    # 방문 여부 추적
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # 시작 지점
    row, col = 0, 0
    
    # 우, 하, 좌, 상 순서로 이동
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    direction = 0  # 초기 방향 (우측으로)
    
    for _ in range(rows * cols):
        print(f"로봇이 ({row}, {col}) 위치 탐색 중")
        visited[row][col] = True
        
        # 다음 위치 계산
        next_row, next_col = row + dr[direction], col + dc[direction]
        
        # 방향 전환 필요 여부 확인
        if (next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or 
            visited[next_row][next_col]):
            direction = (direction + 1) % 4  # 방향 변경
            next_row, next_col = row + dr[direction], col + dc[direction]
        
        row, col = next_row, next_col
    
    print("모든 칸 탐색 완료!")



# BFS나 DFS 함수 호출 시 장애물 처리 추가
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs_search_with_obstacles(grid, start_row=0, start_col=0):
    rows, cols = 4, 6
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    
    
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    
    while queue:
        row, col = queue.popleft()
        print(f"로봇이 ({row}, {col}) 위치 탐색 중")
        
        # 목표 지점에 도달했는지 확인
        if grid[row][col] == 2:
            print("목표 지점에 도달했습니다!")
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                not visited[new_row][new_col] and grid[new_row][new_col] != 1):  # 장애물(1) 피하기
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
    
    print("탐색 완료!")



# 함수 호출
# bfs_search_with_obstacles(grid)  # 또는 다른 탐색 함수들

def robot_search(grid, start_row=0, start_col=0):
    rows, cols = 4, 6
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # 상하좌우 이동 방향 (가로/세로 인접 칸만)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_names = ["오른쪽", "아래쪽", "왼쪽", "위쪽"]
    
    # 경로 추적을 위한 부모 노드 저장
    parent = {}
    
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    
    # 로봇의 현재 위치
    current_position = (start_row, start_col)
    print(f"로봇이 ({start_row}, {start_col}) 위치로 이동했습니다")
    
    # RedCell 발견 횟수 추적
    red_cells_found = 0
    red_cell_positions = []
    
    # 로봇의 이동 경로 기록
    path = [(start_row, start_col)]
    
    while queue:
        row, col = queue.popleft()
        
        # 현재 위치에서 인접한 칸의 장애물 확인
        for i, (dr, dc) in enumerate(directions):
            check_row, check_col = row + dr, col + dc
            if (0 <= check_row < rows and 0 <= check_col < cols):
                if grid[check_row][check_col] == 1:  # 장애물 감지
                    print(f"({row}, {col})에서 {direction_names[i]} 방향에 장애물이 감지되었습니다")
        
        # RedCell(목표 지점) 확인
        if grid[row][col] == 2 and (row, col) not in red_cell_positions:
            red_cells_found += 1
            red_cell_positions.append((row, col))
            print(f"RedCell 발견! 위치: ({row}, {col})")
            
            # 모든 RedCell을 찾았는지 확인 (최대 2개)
            if red_cells_found == 2:
                print("모든 RedCell을 찾았습니다!")
                print(f"RedCell 위치들: {red_cell_positions}")
                return red_cell_positions
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # 유효한 위치이고, 아직 방문하지 않았고, Box(장애물)가 아닌 경우에만 이동
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                not visited[new_row][new_col] and grid[new_row][new_col] != 1):
                
                # 로봇이 실제로 이동할 때만 출력
                print(f"로봇이 ({new_row}, {new_col}) 위치로 이동했습니다")
                
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
                parent[(new_row, new_col)] = (row, col)
    
    # 모든 탐색이 끝났지만 RedCell을 모두 찾지 못한 경우
    if red_cells_found < 2:
        print(f"탐색 완료! {red_cells_found}개의 RedCell만 찾았습니다.")
    else:
        print("탐색 완료!")
    
    return red_cell_positions


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
    
    # BFS 탐색 - 부모 노드 맵 구성
    def bfs_and_get_parent_map():
        # BFS를 위한 큐 초기화
        bfs_queue = deque([(start_row, start_col)])
        # 방문 여부 기록
        bfs_visited = set([(start_row, start_col)])
        # 부모 노드 기록 (경로 추적용)
        parent = {}
        
        # 시작 위치는 부모가 자기 자신 (순환 방지)
        parent[(start_row, start_col)] = (start_row, start_col)
        
        while bfs_queue:
            r, c = bfs_queue.popleft()
            
            # 인접 셀 탐색
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                
                # 유효하고 아직 방문하지 않은 셀이면서 장애물이 아닌 경우
                if (0 <= new_r < rows and 0 <= new_c < cols and 
                    (new_r, new_c) not in bfs_visited and grid[new_r][new_c] != 1):
                    
                    bfs_queue.append((new_r, new_c))
                    bfs_visited.add((new_r, new_c))
                    parent[(new_r, new_c)] = (r, c)  # 부모 노드 기록
        
        return parent, bfs_visited
    
    # 부모 노드 맵 구성 및 BFS로 방문 가능한 모든 셀 확인
    parent_map, reachable_cells = bfs_and_get_parent_map()
    
    # 현재 위치에서 목표 위치까지의 경로 찾기 (무한 루프 방지)
    def get_path(current, target):
        # 시작 위치와 목표 위치가 같으면 빈 경로 반환
        if current == target:
            return []
        
        # 목표 위치가 도달 불가능하면 빈 경로 반환
        if target not in reachable_cells:
            print(f"경고: 위치 {target}에 도달할 수 없습니다.")
            return []
        
        # 경로를 저장할 리스트
        path = []
        temp = target
        visited_in_path = set()  # 순환 감지용
        
        # 경로 역추적 (무한 루프 방지)
        max_iterations = rows * cols  # 최대 반복 제한
        iterations = 0
        
        while temp != current:
            # 무한 루프 방지
            if temp in visited_in_path or iterations >= max_iterations:
                print(f"경고: 경로 탐색 중 문제 발생. 부분 경로만 반환합니다.")
                return list(reversed(path))
            
            visited_in_path.add(temp)
            path.append(temp)
            
            # parent_map에 키가 없는 경우 처리
            if temp not in parent_map:
                print(f"오류: 위치 {temp}의 부모 노드를 찾을 수 없습니다.")
                return list(reversed(path))
            
            temp = parent_map[temp]
            iterations += 1
        
        # 경로 역순으로 변환
        return list(reversed(path))
    
    # 로봇 상태 변수
    robot_pos = (start_row, start_col)
    visited_cells = [(start_row, start_col)]
    red_cells_found = 0
    red_cell_positions = []
    
    # 각 단계별 애니메이션 프레임
    frames = []
    
    # 초기 상태 (시작 위치)
    frames.append(update_visual_grid(robot_pos, visited_cells))
    
    # 탐색할 위치들 - BFS 순으로 정렬
    cells_to_visit = []
    
    # BFS 순서로 모든 셀 탐색
    bfs_queue = deque([(start_row, start_col)])
    bfs_visited = set([(start_row, start_col)])
    
    while bfs_queue:
        r, c = bfs_queue.popleft()
        
        # 시작 위치는 이미 방문했으므로 추가하지 않음
        if (r, c) != (start_row, start_col):
            cells_to_visit.append((r, c))
        
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            
            if (0 <= new_r < rows and 0 <= new_c < cols and 
                (new_r, new_c) not in bfs_visited and grid[new_r][new_c] != 1):
                
                bfs_queue.append((new_r, new_c))
                bfs_visited.add((new_r, new_c))
    
    print(f"방문할 셀 수: {len(cells_to_visit)}")
    
    # 실제 탐색 및 애니메이션 프레임 생성
    for target in cells_to_visit:
        # 이미 방문했거나 RedCell을 모두 찾은 경우 건너뛰기
        if target in visited_cells or red_cells_found >= 2:
            continue
        
        print(f"현재 위치 {robot_pos}에서 목표 {target}까지 경로 계산 중...")
        
        # 현재 위치에서 목표까지의 경로 찾기
        path = get_path(robot_pos, target)
        
        if not path:
            print(f"유효한 경로를 찾을 수 없습니다: {robot_pos} -> {target}")
            continue
        
        print(f"경로 찾음 (길이: {len(path)}): {path}")
        
        # 경로를 따라 이동
        for next_pos in path:
            # 로봇 이동
            robot_pos = next_pos
            if next_pos not in visited_cells:
                visited_cells.append(next_pos)
                visited[next_pos[0]][next_pos[1]] = True
            
            # 프레임 추가
            frames.append(update_visual_grid(robot_pos, visited_cells))
            
            # RedCell 확인
            r, c = robot_pos
            if grid[r][c] == 2 and (r, c) not in red_cell_positions:
                red_cells_found += 1
                red_cell_positions.append((r, c))
                print(f"RedCell 발견! 위치: ({r}, {c})")
                
                # 모든 RedCell을 찾았으면 종료
                if red_cells_found == 2:
                    break
    
    print(f"총 {len(frames)} 프레임의 애니메이션이 생성되었습니다")
    
    # 터미널 애니메이션으로 대체 (matplotlib 문제 방지)
    def terminal_animation():
        print("\n터미널 애니메이션 시작...")
        
        for i, frame in enumerate(frames):
            # 화면 지우기 (시스템에 따라 다름)
            print("\033c", end="")
            
            # 현재 로봇 위치 찾기 (파란색 픽셀)
            robot_r, robot_c = None, None
            for r in range(rows):
                for c in range(cols):
                    if tuple(frame[r, c]) == (0, 0, 1):  # 파란색 == 로봇
                        robot_r, robot_c = r, c
            
            # 그리드 출력
            print(f"프레임 {i+1}/{len(frames)}")
            print("+" + "-" * (cols * 2 - 1) + "+")
            for r in range(rows):
                line = "|"
                for c in range(cols):
                    if r == robot_r and c == robot_c:
                        line += "R"  # 로봇
                    elif grid[r][c] == 1:
                        line += "■"  # 장애물
                    elif grid[r][c] == 2:
                        line += "X"  # RedCell
                    elif tuple(frame[r, c]) == (0.8, 0.8, 1):  # 연한 파란색 == 방문한 위치
                        line += "·"  # 방문한 위치
                    else:
                        line += " "  # 빈 공간
                    
                    if c < cols - 1:
                        line += " "
                line += "|"
                print(line)
            print("+" + "-" * (cols * 2 - 1) + "+")
            print("R: 로봇, ■: 장애물, X: RedCell, ·: 방문한 위치")
            
            # RedCell 상태 출력
            print(f"찾은 RedCell: {len(red_cell_positions)}/{2}")
            
            # 지연
            time.sleep(0.5)
    
    # 터미널 애니메이션 실행
    try:
        terminal_animation()
    except KeyboardInterrupt:
        print("애니메이션이 중단되었습니다.")
    
    # matplotlib 애니메이션 실행 (선택적)
    try:
        # 애니메이션 설정
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
                found_cells = sum(1 for r, c in visited_cells if grid[r][c] == 2)
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
    except Exception as e:
        print(f"matplotlib 애니메이션 오류: {e}")
        return None, red_cell_positions

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
