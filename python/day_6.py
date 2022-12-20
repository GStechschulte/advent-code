

class Packets:

    def __init__(self, num_dist_chars: int) -> int:
        self.num_distinct = num_dist_chars

    def marker_pos(self, stream):
        first_pos = []
        for idx, char in enumerate(stream):
            
            if idx < 1:
                ptnl_first = stream[:idx+self.num_distinct]
            else:
                ptnl_marker = stream[idx:idx+self.num_distinct] 
                if len(ptnl_marker) == len(set(ptnl_marker)):
                    first_pos.append(idx+self.num_distinct)
        
        return first_pos


def main():
    
    with open('./data/buffer.txt', 'r') as f:
        data = f.read()

    pos = Packets(4).marker_pos(data)
    print(f"char. position of first marker: {min(pos)}") 

    pos = Packets(14).marker_pos(data)
    print(f"char. position of first marker: {min(pos)}") 


if __name__ == "__main__":
    main()