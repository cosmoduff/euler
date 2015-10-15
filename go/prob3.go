//What is the largest prime factor of the number 600851475143?

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
	var max_divisor float64
	var divisor float64
	max_divisor = math.Sqrt(x)
	for divisor = 5; divisor<= max_divisor; divisor += 6 {
		if math.Remainder(x, divisor) == 0 ||  math.Remainder(x, (divisor + 2.0)) == 0 {
			return false
		}
	}
	}
	return true
}

func main() {
	var num float64 = 600851475143
	var n float64
	for n = 2; n <= num / 2; n ++ {
            if math.Remainder(num, n) == 0 {
	        num = num / n
            }
        }
        fmt.Println(num)
}
