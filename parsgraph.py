# Getting graph for QUESTION 2


import random


def game(ra, rb):

    if ra < 0 or ra > 100 or rb < 0 or rb > 100:
        return -1
    probA = ra / (ra + rb) 
    scoreA = 0
    scoreB = 0
    time = 0
    
    while ((scoreA >= 11 or scoreB >= 11) and (abs(scoreA - scoreB) >= 2)) == False:
        
        r = random.random()
        
        if r < probA:
            scoreA += 1
            time += 26
        else:
            scoreB += 1
            time += 26

    return scoreA, scoreB, time


def winProbability(ra, rb, n):
    wins = 0
    totalGames = 0
    times = []
    for i in range(0, n-1):
        result = game(ra, rb)
        totalGames += 1
        times.append(result[2])
        if result[0] > result[1]:
            wins += 1
    prob = wins / totalGames
    averageTime = sum(times) / totalGames
    return "%.2f" % prob, "%.2f" % averageTime


print(winProbability(45, 55, 5000))



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
    x = winProbability(i, 20, 5000)
    xpoints.append(float(i))
    ypoints.append(float(x[0]))

for i in range(0, 101, 20):
    z = winProbability(i, 40, 5000)
    fortyrb.append(float(z[0]))

for i in range(0, 101, 20):
    y = winProbability(i, 60, 5000)
    sixtyrb.append(float(y[0]))

for i in range(0, 101, 20):
    a = winProbability(i, 80, 5000)
    eightyrb.append(float(a[0]))

for i in range(0, 101, 20):
    b = winProbability(i, 100, 5000)
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





