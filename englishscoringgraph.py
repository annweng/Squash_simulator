# question2 simulation

import random
# english scoring


def englishgame(ra,rb):

    if ra < 0 or ra > 100 or rb < 0 or rb > 100:
        return -1
    probA = ra / (ra + rb)
    scoreA = 0
    scoreB = 0
    A = 'player1'
    B = 'player2'
    players = [A, B]
    time = 0
    server = random.choice(players)  # randomly chooses which player will serve first
    ties = [9, 10]

    while (scoreA >= 9 or scoreB >= 9) == False:

        r = random.random()

        if r <= probA and server == A:
            scoreA += 1
            time += 26
        elif r <= probA and server == B:
            server = A
            time += 26
        elif r >= probA and server == B:
            scoreB += 1
            time += 26
        elif r >= probA and server == A:
            server = B
            time += 26

        if scoreA == 8 and scoreB == 8:
            playto = random.choice(ties)  # decides if the game will be played to 9 or 10

            if playto == 9:
                while (scoreA >= 9 or scoreB >= 9) == False:
                    r = random.random()
                    if r <= probA and server == A:
                        scoreA += 1
                        time += 26
                    elif r <= probA and server == B:
                        server = A
                        time += 26
                    elif r >= probA and server == B:
                        scoreB += 1
                        time += 26
                    elif r >= probA and server == A:
                        server = B
                        time += 26
            if playto == 10:
                while (scoreA >= 10 or scoreB >= 10) == False:
                    r = random.random()
                    if r <= probA and server == A:
                        scoreA += 1
                        time += 26
                    elif r <= probA and server == B:
                        server = A
                        time += 26
                    elif r >= probA and server == B:
                        scoreB += 1
                        time += 26
                    elif r >= probA and server == A:
                        server = B
                        time += 26

    return scoreA, scoreB, time


def winProbabilityenglish(ra, rb, n):
    wins = 0
    totalGames = 0
    times = []
    for i in range(0, n-1):
        result = englishgame(ra, rb)
        totalGames += 1
        times.append(result[2])
        if result[0] > result[1]:
            wins += 1
    prob = wins / totalGames
    averageTime = sum(times) / totalGames
    return "%.2f" % prob, "%.2f" % averageTime


from matplotlib import pyplot as plt

'''Creates a graph that shows he results from all abilities from 0, 20, 40, ..., 100 playing each other
to see if there is any difference in probability results from similar abililties playing'''


xpoints = []
fortyrb = []
sixtyrb = []
eightyrb = []
centrb = []
ypoints = []
for i in range(0, 101, 20):
    x = winProbabilityenglish(i, 20, 5000)
    xpoints.append(float(i))
    ypoints.append(float(x[0]))

for i in range(0, 101, 20):
    z = winProbabilityenglish(i, 40, 5000)
    fortyrb.append(float(z[0]))

for i in range(0, 101, 20):
    y = winProbabilityenglish(i, 60, 5000)
    sixtyrb.append(float(y[0]))

for i in range(0, 101, 20):
    a = winProbabilityenglish(i, 80, 5000)
    eightyrb.append(float(a[0]))

for i in range(0, 101, 20):
    b = winProbabilityenglish(i, 100, 5000)
    centrb.append(float(b[0]))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(xpoints, sorted(ypoints), 'b', label='rb = 20')
ax.plot(xpoints, sorted(fortyrb), 'r', label='rb = 40')
ax.plot(xpoints, sorted(sixtyrb), 'g', label='rb = 60')
ax.plot(xpoints, sorted(eightyrb), 'y', label='rb = 80')
ax.plot(xpoints, sorted(centrb), 'k', label='rb = 100')
plt.ylabel("P(A wins a game)")
plt.xlabel("ra")
ax.legend()
plt.show()
