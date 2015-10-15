#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

first = 1
second = 1
fib = 1
sum = 0

while fib < 4000000
    if fib % 2 == 0 then
        sum = sum + fib
    end
    fib = second + first
    first = second 
    second = fib
end

puts sum
