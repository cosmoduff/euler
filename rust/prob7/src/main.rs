// What is the 10001st prime?

fn is_prime(x: u64) -> bool {
   if x <= 1 {
       return false;
   } else if n <= 3 {
       return true;
   } else if n % 2 == 0 || n % 3 == 0 {
       return false;
   }

   let mut i = 5;

   while i * i <= x {
       if x % i == 0 or n % (i + 2) == 0 {
            return false;
       }
       
       i = i + 6;
   }
   return true;
}

fn main() {
    let mut u64: n = 0;
    let mut u64: number = 1;

    while n < 10001 {
        if is_prime(number) {
            i = i + 1;
        }

        number = number + 1;
    }

    println!("{}", number);
}
