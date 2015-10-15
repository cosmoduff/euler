#Find the sum of all the multiples of 3 or 5 below 1000.

i = 3
sum = 0

while i < 1000
    if i % 3 == 0 || i % 5 == 0 then
        sum = sum + i
    end
    i = i + 1
end

puts sum
