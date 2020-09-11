class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        final = []
        for i in range(1, n+1):
            if int(i) % 5 == 0 and int(i) % 3 == 0:
                final.append("FizzBuzz")
            elif int(i) % 3 == 0:
                final.append("Fizz")
            elif int(i) % 5 == 0:
                final.append("Buzz")
            else:
                final.append(str(i))
        return final
