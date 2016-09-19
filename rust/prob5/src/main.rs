// What is the smallest positive number that is evenly divisible by all the 
// numbers from 1 to 20

fn remainder(x: u32) -> bool {
    for y in 20..2 {
        if x % y == 0 {
            continue;
        } else {
            return false;
        }
    }
}

fn main() {
    base_num = 2520;

}
