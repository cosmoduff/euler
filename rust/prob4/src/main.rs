// Find the largest palindrome made from the product of two
// 3-digit numbers

fn is_palindrome(s: u32) -> bool {
    let s = s.to_string();
    let reverse: String = s.chars().rev().collect();
    
    if s == reverse {
        return true;
    } else {
        return false;
    }
}

fn main() {
    let mut palindrome: u32 = 0;
    let mut product: u32;
    for x in (900..1000).rev() {
        for y in (900..1000).rev() {
            product = x * y;
            if is_palindrome(product) {
                if product > palindrome {
                    palindrome = product;
                    println!("{}", palindrome);
                    break
                }
            }
        }
    }
}
