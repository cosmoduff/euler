// What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20

fn remainder (n: u32) -> bool {
    for x in 20..2 {
	if n%x == 0 {
	    continue;
	} else {
	    return False
	}
    }
}

fn main() {

    println!("Hello, world!");
}
