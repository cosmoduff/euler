// Find the sum of all the multiples of 3 or 5 below 1000

fn main() {
        let mut sum = 0u32;
        for n in 1..1000 {
                if n % 3 == 0 {
                        sum += n
                }
                else if n % 5 == 0 {
                        sum += n
                }
        }
        println!("{}", sum);
}
