import random

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


def winProbability(ra, rb, n):  
    wins = 0
    totalGames = 0
    for i in range(0, n):
        result = game(ra, rb)
        totalGames += 1
        if result[0] > result[1]:  
            wins += 1
    prob = wins / totalGames
    return "%.2f" % prob
      

#e
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
        

def winMatchProbability(ra, rb, n, repeat):
    aMatches = 0
    bMatches = 0
    for i in range(0, repeat):
        matchResult = winMatch(ra, rb, n)
        if matchResult[0] == "A wins":
            aMatches += 1
        elif matchResult[0] == "B wins":
            bMatches += 1
    prob = aMatches / repeat
    return "%.2f" % prob


print(winMatchProbability(60, 40, 3, 50000))
