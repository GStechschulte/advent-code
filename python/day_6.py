

 



def main():
    
    with open('./data/buffer.txt', 'r') as f:
        data = f.read()
    
    # identify the first position where the four most recently
    # received chars. were all different. 

    for idx, char in enumerate(data):
        
        # marker 
        ptnl_marker = data[:idx+4]
        print(f"ptnl marker = {ptnl_marker}")    
        # in these 4 chars. does a char. repeat?
        #print(set(ptnl_marker).intersection(set(ptnl_marker)))
        print(set(ptnl_marker))

        break



if __name__ == "__main__":
    main()