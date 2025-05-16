mod fibonacci;

use fibonacci::Fibonacci;
use std::io;

fn main() {
    let fib = Fibonacci::new();

    println!("Enter in the amount of Fibonacci numbers you would like to calculate: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let n: usize = input.trim().parse().expect("Please enter a valid number");


    for number in fib.take(n) {
        println!("{}", number);
    }
    
}
