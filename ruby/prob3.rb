#Work in progress`
#What is the largest prime factor of the number 600851475143 ?
#
#
def prime_factor(n)
   for i in 2..n
       if n % i == 0
           i = i / n
           puts #(i)
       end
   end
end

num = 600851475143

prime_factor(num)
