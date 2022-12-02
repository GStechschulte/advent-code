use std::fs::File;
use std::io::prelude::*;


fn main() {

    // let path = Path::new("/Users/gabestechschulte/Documents/repos/advent-code/data/deer_calories.txt");

    let mut file = File::open("/Users/gabestechschulte/Documents/repos/advent-code/data/deer_calories.txt")
        .expect("can't open file!");

    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("oops: cannot read the file");

    print!("file contents: {}", contents);
}
