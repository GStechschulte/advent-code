import pandas as pd
import numpy as np

def main():

    strat = pd.read_csv(
        './data/strategy_guide.txt', sep=" ", names=['opponent', 'you']
        )
    part_1_df = strat.copy()
    part_2_df = strat.copy()

    ## part 1 ##

    equiv = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
        }

    guide = {
        'X': 'C',
        'Y': 'A',
        'Z': 'B'
        }

    point_sys = {
        'X': 1,
        'Y': 2,
        'Z': 3
        }

    part_1_df['meth_pts'] = part_1_df['you'].map(point_sys)
    part_1_df['should_be'] = part_1_df['you'].map(guide)
    part_1_df['you'] = part_1_df['you'].map(equiv)

    part_1_df['game_pts'] = np.where(
        part_1_df['opponent'] == part_1_df['you'], 3,
        np.where(
            ((part_1_df['opponent'] != part_1_df['should_be']) & 
            (part_1_df['opponent'] != part_1_df['you'])), 
            0, 6
            ))

    print(sum((part_1_df['game_pts'] + part_1_df['meth_pts'])))

    ## part 2 ##

    point_sys = {
        'A': 1,
        'B': 2,
        'C': 3
        }
    
    guide_pts = {
        'X': 0,
        'Y': 3,
        'Z': 6
        }

    # this is not Pythonic or vectorized, but it works...
    you_should_play = []
    for idx, row in part_2_df.iterrows():
        if row['you'] == 'Y':
            you_should_play.append(row['opponent'])
        elif row['you'] == 'Z':
            if row['opponent'] == 'A':
                you_should_play.append('B')
            elif row['opponent'] == 'B':
                you_should_play.append('C')
            elif row['opponent'] == 'C':
                you_should_play.append('A')
        elif row['you'] == 'X':
            if row['opponent'] == 'A':
                you_should_play.append('C')
            elif row['opponent'] == 'B':
                you_should_play.append('A')
            elif row['opponent'] == 'C':
                you_should_play.append('B')
        

    part_2_df['you_should_play'] = you_should_play
    part_2_df['meth_pts'] = part_2_df['you_should_play'].map(point_sys)
    part_2_df['game_pts'] = part_2_df['you'].map(guide_pts)

    print(sum(part_2_df['meth_pts'] + part_2_df['game_pts']))

    
if __name__ == '__main__':
    main()