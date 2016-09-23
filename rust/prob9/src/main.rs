// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc

fn pythagorean_triplet(n: u32) {
    for a in (1..501).rev() {
        for b in (1..501).rev() {
            for c in (1..501).rev() {
                if a + b + c == n && (a*a) + (b*b) == (c*c) {
                    let product = a * b * c;
                    println!("{}", product);
                }
            }
        }
    }
}

fn main() {
    pythagorean_triplet(1000)
}
