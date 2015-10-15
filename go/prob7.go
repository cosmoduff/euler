//what is the 10001st prime?

package main

import "fmt"
import "math"

func isPrime(x float64) bool {
        if x < 2 {
                return true
        }
        if x == 2.0 || x == 3.0 {
                return true
        }
        if math.Remainder(x, 2) == 0 || math.Remainder(x, 3) == 0 {
                return false
        }
        var max_divisor float64
        var divisor float64
        max_divisor = math.Sqrt(x)
        for divisor = 5; divisor <= max_divisor; divisor +=6 {
                if math.Remainder(x, divisor) == 0 || math.Remainder(x, (divisor + 2.0)) == 0 {
                        return false
                }
        }
        return true
}

func main () {
        p := 0.0
        x := 0.0
        for p < 10001 {
                x += 1
                if isPrime(x) {
                        p += 1
                }
        }
fmt.Println(x)
}
