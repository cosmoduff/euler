// What is the 10001st prime?

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
    let mut n: u64 = 0;
    let mut number: u64 = 0;

    while n < 10001 {
        number = number + 1;

        if is_prime(number) {
            n = n + 1;
        }
    }

    println!("{}", number);
}
