// How many such routes are there through a 20x20 grid?
fn factorial(mut x: f64) -> f64 {
    let mut factorial_val: f64 = 1.0;
    while x > 1.0 {
        factorial_val = factorial_val * x;
        x = x - 1.0;
    }
    return factorial_val
}

fn lattice_routes(x: f64, y: f64) -> f64{
    let routes: f64;
    routes = factorial(x) / (factorial(y) * factorial(x - y));
    return routes
}

fn main() {
    println!("{}", lattice_routes(40.0, 20.0));
}
