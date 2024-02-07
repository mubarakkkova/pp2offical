def histogram(list):
    for x in list:
        print('*'*x)

def main():
    list = [int(x) for x in input().split()]
    histogram(list)
main()