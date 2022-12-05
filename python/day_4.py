


def main():
    
    with open('./data/assignments.txt', 'r') as f:
        content = [row.strip().split(',') for row in f.readlines()]

    ## Part 1 ##
    
    cnt_contains = []
    for pair in content:

        partition_1 = pair[0].rpartition('-')
        partition_2 = pair[1].rpartition('-')

        if int(partition_1[0]) <= int(partition_2[0]) and \
        int(partition_1[2]) >= int(partition_2[2]):
                cnt_contains.append(1)
        elif int(partition_2[0]) <= int(partition_1[0]) and \
            int(partition_2[2]) >= int(partition_1[2]):
                cnt_contains.append(1)


    print(f"# of pairs where one range fully contain the other: {sum(cnt_contains)}")

    ## Part 2 ##

    


if __name__ == '__main__':
    main()