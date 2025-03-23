from collections import deque


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

# 예: 0은 빈 공간, 1은 장애물, 2는 목표 지점
grid = [ 
    [0, 0, 0, 1, 0, 0],
    [0, 1, 2, 0, 0, 0],
    [0, 0, 0, 1, 2, 0],
    [0, 1, 0, 0, 0, 0]
]
found_positions = robot_search(grid)
print(f"찾은 RedCell 위치: {found_positions}")