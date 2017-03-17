// What is the value of the first triangle number to have over five hundred
// divisors

use std::f64;

fn create_triangle_num(x: u64) -> f64 {
    let triangle = x * (x + 1) / 2;
    return triangle as f64;
}

fn count_divisors(x: f64) -> u64 {
    let x_sqrt = x.sqrt();
    let x_sqrt = x_sqrt as u64;
    let x = x as u64;
    let end_range = x_sqrt + 1;
    let end_range = end_range as u64;
    let mut count:u64 = 0;

    for y in 1..end_range {
        if x % y == 0 {
            count = count + 1
        }
    }
    let count = count * 2;
    if x_sqrt * x_sqrt != x {
        return count;
    } else {
        return count + 1;
    }
}

fn main() {
    let mut counter: u64 = 1;

    loop {
        if count_divisors(create_triangle_num(counter)) > 500 {
            println!("{}", create_triangle_num(counter));
            break
        }
        counter = counter + 1
    }
}
