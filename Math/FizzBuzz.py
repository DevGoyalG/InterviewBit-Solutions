class Solution:
	# @param A : integer
	# @return a list of strings
	def fizzBuzz(self, A):
        result=[]
        for i in range(1, A+1):
            if i%3==0 and i%5==0:
                result.append("FizzBuzz")
            elif i%3==0:
                result.append("Fizz")
            elif i%5==0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
