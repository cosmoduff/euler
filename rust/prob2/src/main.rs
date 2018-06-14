// By considering the terms in the Fibonacci sequence whose values do not
// exceed four million find the sum of the even-valued terms

fn main() {
    let mut first_n = 1;
    let mut second_n = 1;
    let mut fib = 0;
    let mut total = 0;

    while fib < 4_000_000 {
        fib = first_n + second_n;
        if fib % 2 == 0 {
            total += fib;
        }
        first_n = second_n;
        second_n = fib;
    }
    println!("{}", total);
}
