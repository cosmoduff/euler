// Find the difference between the sum of the squares of the first one hundred
// natural numbers and the square of the sum

fn main() {
    let mut sum_squares: u64 = 0;
    let mut square_sums: u64 = 0;

    for x in 1..101 {
        square_sums = square_sums + x;
        sum_squares = sum_squares + x * x;
    }

    square_sums = square_sums * square_sums;

    let difference = square_sums - sum_squares;

    println!("{}", difference);
}
