import random

def get_min_max(ints):

   if ints is None:
      return

   if len(ints) <= 1:
      return ints

   min_value = ints[0]
   max_value = ints[-1]

   for i in range(len(ints)):
      if ints[i] < min_value:
         min_value = ints[i]

      if ints[i] > max_value:
         max_value = ints[i]

   return min_value, max_value
  


## Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

l2 = [100, -100]
l3 = []
l4 = [-300, -1, -4, -800]
l5 = [-8, 0, 6, -(-8)]
l6 = [6, 3]

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((-100, 100) == get_min_max(l2)) else "Fail")
print ("Pass" if ([] == get_min_max(l3)) else "Fail")
print ("Pass" if ((-800, -1) == get_min_max(l4)) else "Fail")
print ("Pass" if ((-8, 8) == get_min_max(l5)) else "Fail")
print ("Pass" if ((3, 6) == get_min_max(l6)) else "Fail")