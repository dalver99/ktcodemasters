def min_award_winners(n, scores):
    # Initialize a list to count how many films each film can defeat
    defeats_count = [0] * n

    # Compare each pair of films
    for i in range(n):
        for j in range(n):
            if i != j:
                # If film j defeats film i
                if (scores[j][0] >= scores[i][0] and
                    scores[j][1] >= scores[i][1] and
                    scores[j][2] >= scores[i][2]):
                    defeats_count[i] += 1

    # Count how many films have been defeated by more than 2 other films
    winners = sum(1 for defeats in defeats_count if defeats <= 2)

    return winners

# Input reading
N = int(input())
score = [list(map(int, input().strip().split())) for _ in range(N)]
print(min_award_winners(N, score))
