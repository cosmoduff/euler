//Find the sum of all the multiples of 3 or 5 below 1000.

package main

import "fmt"

func main () {
	total := 0
	for i := 1; i < 1000; i++ {
		if i % 3 == 0 || i % 5 == 0 {
			total += i
		}
	}
	fmt.Println(total)
}
