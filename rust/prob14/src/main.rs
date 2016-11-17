// Collatz Sequence
// Which starting number, under one million, produces the longest chain?
fn collatz_length(mut x: u64) -> u64 {
    let mut count: u64 = 1;
    while x != 1 {
        if x % 2 == 0 {
            x = x/2
        } else {
            x = (x * 3) +1
        }
        count = count + 1
    }
    return count
}

fn main() {
    let mut greatest: u64 = 0;
    let mut num: u64 = 0;

    for n in 1..1000000 {
        let collatz_num: u64 = collatz_length(n);
        if collatz_num > greatest {
            greatest = collatz_num;
            num = n;
        }
    }
    println!("{}", num)
}
