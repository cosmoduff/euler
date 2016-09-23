// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc

fn main() {
    'a: for a in (1..501).rev() {
        'b: for b in (1..501).rev() {
            'c: for c in (1..501).rev() {
                if a + b + c == 1000 && (a*a) + (b*b) == (c*c) {
                    let product = a * b * c;
                    println!("{}", product);
                }
            }
        }
    }
}
