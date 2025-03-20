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


# 빈 grid 생성 (모든 값이 0인 4*6 배열)
grid = [[0 for _ in range(6)] for _ in range(4)]

# 예: 각 셀에 특정 값이 있는 grid
# grid = [
#     [10, 20, 30, 40, 50, 60],
#     [15, 25, 35, 45, 55, 65],
#     [17, 27, 37, 47, 57, 67],
#     [19, 29, 39, 49, 59, 69]
# ]


# 함수 호출
dfs_search(grid)  # 또는 다른 탐색 함수들
