from collections import Counter


def main():

    sum = 0
    deer_idx = 0
    calories = {}
    with open('../data/deer_calories.txt', 'r') as f:
        
        for row in f.readlines():
            if (row[0] != '\n'):
                sum += int(row)
                deer_idx += 1
                calories[f'deer_{deer_idx}_total'] = sum
            else:
                sum = 0
        
        f.close()

    top_n = dict(Counter(calories).most_common(3))
    print(top_n)
    
    total = 0
    for val in top_n.values():
        total += val
    
    print(total)


if __name__ == '__main__':
    main()