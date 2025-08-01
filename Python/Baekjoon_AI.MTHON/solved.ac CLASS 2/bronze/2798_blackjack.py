N, M = map(int, input().split())
card_list = list(map(int, input().split()))

closest = 0

for card1 in range(N):
    for card2 in range(card1 + 1, N):
        for card3 in range(card2 + 1, N):
            card_sum = card_list[card1] + card_list[card2] + card_list[card3]
            if card_sum <= M and card_sum > closest:
                closest = card_sum

print(closest)
