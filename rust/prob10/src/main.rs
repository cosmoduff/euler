// Find the sum of all the primes below 2 million

fn is_prime(x: u64) -> bool {
   if x <= 1 {
       return false;
   } else if x <= 3 {
       return true;
   } else if x % 2 == 0 || x % 3 == 0 {
       return false;
   }

   let mut i: u64 = 5;

   while i * i <= x {
       if x % i == 0 || x % (i + 2) == 0 {
            return false;
       }
       
       i = i + 6;
   }
   return true;
}

fn main() {
    let mut result: u64 = 0;
    for x in 1..2000000 {
        if is_prime(x) {
            result = result + x;
        }
    }
    println!("{}", result);
}
