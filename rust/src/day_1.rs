use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() {

    let mut file = File::open("../data/deer_calories.txt")
        .expect("can't open file!");

    
    // Store file contents into vector

    //let mut calories_vec = Vec::new();
    //file.read_to_end(&mut calories_vec);
    // to print a vector, use {:?}
    // println!("calories = {:?}", calories_vec);

    // Store file contents as string

    // let mut calories_str = String::new();
    // file.read_to_string(&mut calories_str)
    //     .expect("oops: cannot read the file");
    
    // println!("file contents: {calories_str}");

    // let char_count = calories_str.chars().count();

    // println!("char count: {char_count}");

    let buf_reader = BufReader::new(file);

    let sum i32 = buf_reader
        .lines()
        .map(|line| line.unwrap().parse()::<i32>().unwrap())
        .sum();

    // let summation: i32 = buf_reader
    //     .lines()
    //     .map(|line| line.unwrap().parse::<i32>().unwrap())
    //     .sum();
    // println!("{}", summation);


}
