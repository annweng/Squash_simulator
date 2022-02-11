import random  
#1

#a
'''If the random seed is set to 57, then calling the function with arguments 70 and 30 should
return (11, 5). '''

random.seed(57)


def game(ra, rb):

    if ra < 0 or ra > 100 or rb < 0 or rb > 100:
        return -1
    probA = ra / (ra + rb)  # probability of player A winning a point
    scoreA = 0
    scoreB = 0
    
    while ((scoreA >= 11 or scoreB >= 11) and (abs(scoreA - scoreB) >= 2)) == False:
        
        r = random.random()
        
        if r < probA:
            scoreA += 1
        else:
            scoreB += 1

    return scoreA, scoreB

#print(game(70, 30))

#b

'''Given sufficient simulations, calling the function with abilities 70 and 30 should give the
answer 0.98 when printed to 2 decimal places. '''


def winProbability(ra, rb, n=5000):  # law of large numbers
    wins = 0
    totalGames = 0
    for i in range(0, n):
        result = game(ra, rb)
        totalGames += 1
        if result[0] > result[1]:  # if Player A's score is higher than player B's, then they won the game
            wins += 1
    prob = float(wins / totalGames)
    return round(prob, 2)


#print(winProbability(60, 40, 5000))
      

#c

'''Reading in the data above should return: [(60, 20), (100, 55), (50, 40), (20,
70), (95, 85)]). '''


def readFile(file):
    import csv

    with open(file) as csvfile:
        rdr = csv.reader(csvfile)
        next(rdr)  # skip the headings
        listAbilities = []
        for row in rdr:
            listAbilities.append((row[0], row[1]))
        return listAbilities


abilities = readFile('ability.csv')

#d

'''Show the figure produced for data [(60, 20), (100, 55), (50, 40), (20, 70),
(95, 85)]
 '''
from matplotlib import pyplot as plt

# matplotlib shows p( player a beats player b in a game against ra/rb)


def graph(abilities):
    xpoints = []
    ypoints = []
    for i in abilities:
        lst = list(i)
        lst1 = [int(s) for s in lst]
        x = winProbability(lst1[0], lst1[1], 5000)
        y = lst1[0] / lst1[1]
        xpoints.append(round(float(x), 2))
        ypoints.append(round(float(y), 2))

    plt.plot(xpoints, ypoints)
    plt.xlabel("P(A beats B)")
    plt.ylabel("ra / rb")
    plt.show()


#graph(abilities)

#e

'''Show for abilities 60 and 40, the smallest value of n where the probability
that a wins the match is at least 0.9'''


def winMatch(ra, rb, n):  # first to n
    awins = 0
    bwins = 0
    totalGames = 0

    for i in range(0, n):
        while awins < n and bwins < n:
            result = game(ra, rb)
            totalGames += 1
            if result[0] > result[1]:
                awins += 1

            else:
                bwins += 1
        if awins == n:
            return "A wins", totalGames

        elif bwins == n:
            return "B wins", totalGames
        

def winMatchProbability(ra, rb, n, repeat = 50000):
    aMatches = 0
    bMatches = 0
    for i in range(0, repeat):
        matchResult = winMatch(ra, rb, n)
        if matchResult[0] == "A wins":
            aMatches += 1
        elif matchResult[0] == "B wins":
            bMatches += 1
    prob = float(aMatches / repeat)
    return round(prob, 2)


#print(winMatchProbability(60, 40, 2))

