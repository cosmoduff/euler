// What is the value of the first triangle number to have over five hundred
// divisors

fn create_triangle_num(x: u64) -> u64 {
    let end_range = x + 1;
    let mut product: u64 = 0;

    for y in 1..end_range {
        product = product + y
    }
    return product;
}

fn main() {
    // Test triangle function. Should print 28
    println!("{}", create_triangle_num(7));
}
