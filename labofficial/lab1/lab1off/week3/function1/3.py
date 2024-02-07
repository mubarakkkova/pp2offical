def solve(numheads, numlegs):
    x = numheads * 2
    numlegs -= x
    numlegs /= 2
    numheads -=numlegs
    print("chicken num: " + str(numheads) +  "\nrabbit num: " + str(numlegs))

numh = float(input())
numl = float(input())
solve(numh, numl)