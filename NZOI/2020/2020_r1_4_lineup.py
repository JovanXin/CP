"""
Optimizations made:
1) Sort both lists, to maximize efficency (as we can match the lowest ranking with the lowest ranking for both)
2) Use 'score' as both the actual score and a count in order to run in O(n), we match each increasing ranking
todd player with the lowest UNDEFEATED other player (using 'score').
"""

player_num = int(input())
todd = sorted(list(map(int, input().split())))
other = sorted(list(map(int, input().split())))


def lineup(player_num, todd, other):
    score = 0
    for player in todd:
        if player > other[score]:
            score += 1

    print(score)


lineup(player_num, todd, other)