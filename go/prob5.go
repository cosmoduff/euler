//What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

package main

import "fmt"

func checkRemainders(n int) bool {
        for i := 20; i>0; i-- {
                if n % i == 0 {
                        continue
                } else {
                        return false
                        break
                }
        }
return true
}

func main() {
        number := 2520
        for checkRemainders(number) == false {
                number += 2520
                if checkRemainders(number) != false {
                        fmt.Println(number)
                        break
                }
        }
}
