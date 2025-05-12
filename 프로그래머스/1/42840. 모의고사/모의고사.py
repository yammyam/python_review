# 12345-12345
# 21232425-21232425
# 3311224455-3311224455
# 인덱스갯수,1,2,3으로저장하고
def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],       
        [2, 1, 2, 3, 2, 4, 2, 5],  
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  
    ]
    
    scores = [0, 0, 0]  
    
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:  # 패턴을 반복하며 비교
                scores[j] += 1
    
    # 가장 많이 맞힌 수포자의 점수 찾기
    max_score = max(scores)
    
    # 최대점수찾기 중복허용
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]
    
    return result