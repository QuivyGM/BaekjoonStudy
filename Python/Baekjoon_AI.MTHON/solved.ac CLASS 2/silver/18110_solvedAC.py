import sys

def round_half_up(n):
    if n >= 0:
        return int(n + 0.5)
    else:
        return int(n - 0.5)

score_count = int(sys.stdin.readline())

true_count = round_half_up(score_count * 0.15)

score_track = {i: 0 for i in range(1, 31)}

for _ in range(score_count):
    score = int(sys.stdin.readline())
    score_track[score] += 1

max_score, min_score = 30, 1

# 최소 점수 제거
remove = true_count
while remove > 0:
    if score_track[min_score] > 0:
        take = min(score_track[min_score], remove)
        score_track[min_score] -= take
        remove -= take
    else:
        min_score += 1

# 최대 점수 제거
remove = true_count
while remove > 0:
    if score_track[max_score] > 0:
        take = min(score_track[max_score], remove)
        score_track[max_score] -= take
        remove -= take
    else:
        max_score -= 1

valid_count = score_count - 2 * true_count

if valid_count == 0:
    print(0)
else:
    final_score = sum(score * count for score, count in score_track.items())
    print(round_half_up(final_score / valid_count))