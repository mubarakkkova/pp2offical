def unique(list):
    new_list = []
    for x in list:
        if x not in new_list:
            new_list.append(x)
    return new_list

def main():
    list = [x for x in input().split()]
    print(unique(list))
main()