# Fibonacci in Natural Number

Although Fibonacci rules are usually a sequence whose domain is a natural number starting from 1, and 0 is often adopted as the first value, while I was eating pizza while lying in bed, I became curious as to why Fibonacci's domain should not be an integer.

My assumption is this:

1. If $Fibonacci(n-2) + Fibonacci(n-1) = Fibonacci(n), $
    then $Fibonacci(n-2) = Fibonacci(n) - Fibonacci(n-1)$.
2. Let’s say Fibonacci(0) = 0.

As a result, the range oscillates in the area where the domain has negative values, and the range diverges to positive infinity in the area where the domain has positive values.

The next question is what happens if the domain is a real number.