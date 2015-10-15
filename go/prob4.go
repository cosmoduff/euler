//Find the largest palindrome made from the product of two 3-digit numbers.

package main

import(
        "fmt"
        "strconv"
      )

func isPalindrome(n string) bool {
    end := len(n) - 1
    for _, x := range n {
        if int(x) == int(n[end]) {
            end--
        } else {
            return false
        }
    }
return true
}

func main () {
    palindrome := 0
    for i := 999; i >= 100; i-- {
        for n := 999; n >= 100; n-- {
            total := i * n
            if total > palindrome {
                if isPalindrome(strconv.Itoa(total)) {
                    palindrome = total
                }
            }
        }
    }
    fmt.Println(palindrome)
}
