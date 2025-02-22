def solution(board):
    # 위, 아래, 좌, 우, 대각선 방향 설정
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]
    
    # 정사각형의 크기
    n = len(board)
    
    # 초기 안전지대 개수
    answer = n * n
    
    # 지뢰 위치 저장
    ch = []
    
    # 모든 칸을 확인하여 지뢰 위치 저장 및 초기 안전지대 개수 감소
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                ch.append((i, j))
                answer -= 1
    
    # 모든 지역이 지뢰일 경우 0 반환
    if answer == 0:
        return 0
    
    # 지뢰 주변 위험지역 확인
    for w in ch:
        for k in range(8):
            nx, ny = w[0] + dx[k], w[1] + dy[k]
            
            # 유효한 위치이며 아직 위험지역이 아니라면
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                board[nx][ny] = 1
                answer -= 1
    
    return answer