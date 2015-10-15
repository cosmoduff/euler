//By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

package main

import "fmt"

func main() {
	var (
		num1 = 1
		num2 = 1
		fib = 0
		total = 0
	)
	for fib < 4000000 {
		fib = num1 + num2
		if fib % 2 == 0 {
			total += fib
		}
		num1 = num2
		num2 = fib
	}
	fmt.Println(total)
}
