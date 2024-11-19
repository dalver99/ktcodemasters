from itertools import combinations

def calculate_score(team, S):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            score += S[team[i]][team[j]] + S[team[j]][team[i]]
    return score

def solution(N,S):

    
    # 가능한 모든 팀의 조합을 확인
    all_indices = set(range(N))
    min_diff = float('inf')  # 최소 점수 차이
    
    # N/2개의 재료를 선택하는 모든 조합을 계산
    for team1 in combinations(range(N), N // 2):
        team1 = set(team1)
        team2 = all_indices - team1
        
        # 각 팀의 영양 점수를 계산
        score1 = calculate_score(list(team1), S)
        score2 = calculate_score(list(team2), S)
        
        # 점수 차이의 절댓값을 계산하고, 최소값 갱신
        min_diff = min(min_diff, abs(score1 - score2))
    return min_diff
N = int(input())  # 식재료의 개수
S = [list(map(int, input().split())) for _ in range(N)]
print(solution(N,S))