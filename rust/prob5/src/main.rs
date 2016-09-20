// What is the smallest positive number that is evenly divisible by all the 
// numbers from 1 to 20

fn remainder(x: u64) -> bool {
    let mut escape = true;
    for y in 2..21 {
        if x % y == 0 {
            continue;
        } else {
            escape = false;
        }
    }
    return escape;
}

fn main() {
    let mut base_num = 2520;

    while !remainder(base_num) {
        base_num += 2520
    }
    
    println!("{}", base_num);
}
