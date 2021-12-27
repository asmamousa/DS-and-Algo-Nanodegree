def find_sqrt(start, end, number):

   if start > end:
      raise Exception('Start boundary must be less than End boundary')

   # Base Case: when there's three consecutive numbers to find from
   if end - start == 2:
      mid_number = start + 1
      if (mid_number*mid_number) == number:
         return mid_number

      elif ((start*start) < number) and (number < (mid_number*mid_number)):
         return start

      elif ((mid_number*mid_number) < number) and (number < end*end):
         return mid_number

   else:      
      mid_number_index = (end - start)//2
      mid_number = start + mid_number_index

      if (mid_number*mid_number) == number:
         return mid_number

      elif (mid_number*mid_number) > number:
         return find_sqrt(start, mid_number, number)

      elif (mid_number*mid_number) < number:
         return find_sqrt(mid_number, end, number)


    

def sqrt(number):
   if number in [0, 1]:
      return number

   if number < 0:
      raise Exception("Can't find sqrt for a negative value")

   start = 0
   end = number

   return find_sqrt(start, end, number)

# base sqrts
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")

print ("Pass" if  (1 == sqrt(2)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (12 == sqrt(145)) else "Fail")
print ("Pass" if  (5 == sqrt(35)) else "Fail")
sqrt(-144)
# raise Exception: Can't find sqrt for a negative value
