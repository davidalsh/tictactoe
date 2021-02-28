
def check_winner():
    winner = ([zone[0][0], zone[0][1], zone[0][2]],
              [zone[1][0], zone[1][1], zone[1][2]],
              [zone[2][0], zone[2][1], zone[2][2]],
              [zone[0][0], zone[1][0], zone[2][0]],
              [zone[0][1], zone[1][1], zone[2][1]],
              [zone[0][2], zone[1][2], zone[2][2]],
              [zone[0][0], zone[1][1], zone[2][2]],
              [zone[0][2], zone[1][1], zone[2][0]])
    for i in winner:
        if i[0] == i[1] == i[2] and i[0] != '*':
            return i[0]


def clean():
    for i in range(3):
        for k in range(3):
            if values[i][k] != -1:
                if i == 1 and k == 1:
                    values[i][k] = 1
                else:
                    values[i][k] = 0


def check_stars(stars):
    if zone[0][0] == '*':
        stars += 1
    if zone[1][1] == '*':
        stars += 1
    if zone[2][2] == '*':
        stars += 1
    return stars


def check_enemies(enemies):
    if zone[0][0] == move:
        enemies += 1
    if zone[1][1] == move:
        enemies += 1
    if zone[2][2] == move:
        enemies += 1
    return enemies


def check_friends(friends):
    if zone[0][0] == move_bot:
        friends += 1
    if zone[1][1] == move_bot:
        friends += 1
    if zone[2][2] == move_bot:
        friends += 1
    return friends


def check_stars_back(stars):
    if zone[0][2] == '*':
        stars += 1
    if zone[1][1] == '*':
        stars += 1
    if zone[2][0] == '*':
        stars += 1
    return stars


def check_enemies_back(enemies):
    if zone[0][2] == move:
        enemies += 1
    if zone[1][1] == move:
        enemies += 1
    if zone[2][0] == move:
        enemies += 1
    return enemies


def check_friends_back(friends):
    if zone[0][2] == move_bot:
        friends += 1
    if zone[1][1] == move_bot:
        friends += 1
    if zone[2][0] == move_bot:
        friends += 1
    return friends


def print_zone():
    print('—' * 7)
    for i in zone:
        print('|', ' | '.join(i), '|')
        print('—'*7)


def print_values():
    pass
    # for z in values:
    #     for y in z:
    #         print(y, end=' ')
    #     print()


def score(stars, enemies, friends):
    if stars == 1 and friends == 2:  # 5
        values[fir][sec] += 100
    if stars == 1 and enemies == 2:  # 4
        values[fir][sec] += 15
    if stars == 2 and friends == 1:  # 2
        values[fir][sec] += 2
    if stars == 2 and enemies == 1:  # 3
        values[fir][sec] += 1


def score2(star11, enemy11, friend11, star22, enemy22, friend22):
    if friend11 == 2:  # 5
        values[fir][sec] += 100
    if friend22 == 2:  # 5
        values[fir][sec] += 100

    if star11 == 2 and friend11 == 1:  # 2
        values[fir][sec] += 2
    if star22 == 2 and friend22 == 1:  # 2
        values[fir][sec] += 2

    if star11 == 2 and enemy11 == 1:  # 3
        values[fir][sec] += 1
    if star22 == 2 and enemy22 == 1:  # 3
        values[fir][sec] += 1

    if enemy11 == 2:  # 4
        values[fir][sec] += 15
    if enemy22 == 2:  # 4
        values[fir][sec] += 15


RAZM = 3
zone = [['*' for i in range(RAZM)] for k in range(RAZM)]
values = [[0 for d in range(RAZM)] for z in range(RAZM)]
values[1][1] = 1
com = 0
flag = True
f2 = True
win = None
part = input()
if part == 'X' or part == 'x' or part == 'Cross':
    move = 'X'
    move_bot = '0'
    s = 0
else:
    move = '0'
    move_bot = 'X'
    s = 1
while com < 9 and win is None:
    f2 = True
    if (com + s) % 2 == 0:
        f = input().split()
        x = int(f[0]) - 1
        y = int(f[1]) - 1
        if zone[x][y] == '*':
            zone[x][y] = move
            values[x][y] = -1
    else:
        print_values()
        maxx = -1
        for k in range(RAZM):
            for d in range(RAZM):
                if values[k][d] > maxx:
                    maxx = values[k][d]
                    max_movek = k
                    max_moven = d
        zone[max_movek][max_moven] = move_bot
        values[max_movek][max_moven] = -1

        print_zone()
        f2 = False
    clean()
    com += 1
    star1, star2, enemy1, enemy2, friend1, friend2, star_dignl, enemy_dignl, friend_dignl = 0, 0, 0, 0, 0, 0, 0, 0, 0
    for fir in range(RAZM):
        for sec in range(RAZM):
            if values[fir][sec] != -1:
                star1, star2, enemy1, enemy2, friend1, friend2 = 0, 0, 0, 0, 0, 0
                if fir == sec:
                    star_dignl = check_stars(star_dignl)
                    enemy_dignl = check_enemies(enemy_dignl)
                    friend_dignl = check_friends(friend_dignl)
                    score(star_dignl, enemy_dignl, friend_dignl)
                star_dignl, enemy_dignl, friend_dignl = 0, 0, 0

                if (fir + sec) == 2:
                    star_dignl = check_stars_back(star_dignl)
                    enemy_dignl = check_enemies_back(enemy_dignl)
                    friend_dignl = check_friends_back(friend_dignl)
                    score(star_dignl, enemy_dignl, friend_dignl)
                star_dignl, enemy_dignl, friend_dignl = 0, 0, 0

                for b in range(RAZM):
                    if zone[fir][b] == '*':
                        star1 += 1
                    if zone[b][sec] == '*':
                        star2 += 1
                    if zone[fir][b] == move:
                        enemy1 += 1
                    if zone[b][sec] == move:
                        enemy2 += 1
                    if zone[fir][b] == move_bot:
                        friend1 += 1
                    if zone[b][sec] == move_bot:
                        friend2 += 1

                score2(star1, enemy1, friend1, star2, enemy2, friend2)

    win = check_winner()  # check winner info over


if f2:

    print_zone()
    print_values()

if win == 'X':
    print('Crosses won!!!\n-----')
elif win == '0':
    print('Zero won!!!\n-----')
else:
    print('Draw')
