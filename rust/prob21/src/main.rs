// Evaluate the sum of all the amicable numbers under 10000.
// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
// 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
// 71 and 142; so d(284) = 220.

fn sum_divisors(x: u64) -> u64 {
    // Takes a number and returns the sum of its divisors

    let max_range = x-1;
    let mut divisors: Vec<u64> = Vec::new();
    
    for y in 1..max_range as u64 {
        if x % y == 0 {
            divisors.push(y as u64);
        }
    }

    return divisors.iter().sum()
}

fn check_amicable(x: u64) -> Option<u64> {
// Checks to see if x is an amicable number
    // Find the sum of the divisors of x
    let x_sum: u64 = sum_divisors(x);
    // 
    let y_sum: u64 = sum_divisors(x_sum);
    
    if x == x_sum {
        return None
    }

    if x == y_sum {
        return Some(x_sum)
    } else {
       return None
    } 
}

fn main() {

    let mut amicables: Vec<u64> = Vec::new();

    for x in 3..10000 {
        let pair = check_amicable(x);
        match pair {
            Some(pair) => {
                amicables.push(x);
                amicables.push(pair);
            },
            None => continue
        }
    }
    
    amicables.sort();
    amicables.dedup();

    let sum: u64 = amicables.iter().sum();

    println!("{:?}", sum);
}
