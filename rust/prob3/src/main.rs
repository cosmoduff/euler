//What is the largest prime factor of the number 600851475143?

fn prime_factor(n: u64) {
    let mut num = n;
    for x in 2..num {
        if num % x == 0 {
            num = num / x;
            println!("{}", x);
        }
    }
}

fn main() {
    let num = 600851475143;
    prime_factor(num);
}
