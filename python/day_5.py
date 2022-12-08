from dataclasses import dataclass

@dataclass
class SupplyStacks:

    crates: dict

    def decode_rule(self, rule_str):

        self.rule = [int(i) for i in rule_str.split() if i.isdigit()]


    def remove(self):

        removed = [self.crates[self.rule[1]].pop(-1) for _ in range(1, self.rule[0]+1)]

        return removed
        

    def add(self, removed_crates):

        for crate in removed_crates:
            self.crates[self.rule[2]].append(crate)
        
    def top(self):

        top = [stack[-1] for stack in list(self.crates.values())]
        
        return top
        

def main():

    shipping = {
        1: ['G', 'F', 'V', 'H', 'P', 'S'],
        2: ['G', 'J', 'F', 'B', 'V', 'D', 'Z', 'M'],
        3: ['G', 'M', 'L', 'J', 'N'],
        4: ['N', 'G', 'Z', 'V', 'D', 'W', 'P'],
        5: ['V', 'R', 'C', 'B'],
        6: ['V', 'R', 'S', 'M', 'P', 'W', 'L', 'Z'],
        7: ['T', 'H', 'P'],
        8: ['Q', 'R', 'S', 'N', 'C', 'H', 'Z', 'V'],
        9: ['F', 'L', 'G', 'P', 'V', 'Q', 'J']
        }

    with open('./data/cargo.txt', 'r') as f:
        rules = [row.strip() for row in f.readlines()[10:]]
    
    ss = SupplyStacks(shipping)

    for rule in rules:
        ss.decode_rule(rule) 
        removed_crates = ss.remove()
        ss.add(removed_crates)
        
    print(f"stack tops are: {ss.top()}")
   

if __name__ == '__main__':
    main()