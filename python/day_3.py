import string
import numpy as np

def main():


    with open('./data/rucksack.txt', 'r') as f:
        items = [row.strip() for row in f.readlines()]
        f.close()
    
    ## Part 1 ##

    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    lower_scoring = np.arange(1, 27, 1)
    upper_scoring = np.arange(27, 53, 1)

    lower_guide = {
        letter:score for letter, score in zip(alphabet_lower, lower_scoring)
        }
    upper_guide = {
        letter:score for letter, score in zip(alphabet_upper, upper_scoring)
        }

    priorities = []
    for item in items:
        half = len(item) // 2
        half_1 = item[:half]
        half_2 = "".join(item[half:])
        halfs = [half_1, half_2]

        sets = [set(x) for x in halfs]
        common_chars = sets[0].intersection(*sets[1:])
        
        for char in common_chars:
            if char.islower():
                priorities.append(lower_guide[char])
            elif char.isupper():
                priorities.append(upper_guide[char])
        
    print(f"Total sum of priorities = {sum(priorities)}")
 
    ## Part 2 ##

    groups = np.array_split(np.array(items), len(items) // 3)
    group_priorities = []
    for group in groups:
        
        sets = [set(x) for x in group]
        common_chars = sets[0].intersection(*sets[1:])
        
        for char in common_chars:
            if char.islower():
                group_priorities.append(lower_guide[char])
            elif char.isupper():
                group_priorities.append(upper_guide[char])

    print(f"Sum priorities grouped by group = {sum(group_priorities)}")

if __name__ == '__main__':
    main()