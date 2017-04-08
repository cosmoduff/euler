// What is the sum of the digits of the number 2^1000?

extern crate num;
extern crate num_traits;

use num::bigint::BigUint;
use num::FromPrimitive;
use num_traits::pow;

fn add_digits_biguint(x: BigUint) -> u32 {
    let sum = x.to_string().chars().filter_map(|y| y.to_digit(10)).sum();
    return sum
}

fn main() {
    let pow: BigUint = pow(FromPrimitive::from_u8(2).unwrap(), 1000);
    println!("{}", add_digits_biguint(pow));
}
