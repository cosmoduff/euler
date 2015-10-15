//Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

package main

import "fmt"

func main() {
    sumSquares := 0
    squareSums := 0

    for i := 1; i <= 100; i++ {
            sumSquares = sumSquares + i * i
            squareSums = squareSums + i
    }

answer := squareSums * squareSums - sumSquares

fmt.Println(answer)
}
