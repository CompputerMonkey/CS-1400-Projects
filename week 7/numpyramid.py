def pyrimid(number):

    # Set up variables
  
  num = number
  count = 0
  final = ""

    # if the number is less then 10 then do a regular pyramid
  
  if number < 10:
    for j in range(1, number+1):       # starting at 1 and going to number plus one so it gets included
      for i in range(0, number-count):    # sets up spacing
        final = final + " "
      for p in range(0, count+1):      # adds the amount of numbers to the row
        final = final + str(j) + " " 
      final = final +"\n"
      count += 1
  else:

          # if i t is greater it will do the first 9 rows with 6 extra spaces so it will be mostly centered
          
    for j in range(1, 10):
      for i in range(0, number-count+6):   # adds 6 because its roughply a six digit difference on each side of the pyrimid
        final = final + " "
      for p in range(0, count+1):
        final = final + str(j) + " "
      final = final +"\n"
      count += 1

      # then it wil generate the rest of the pyrimid with the regular spacing
      
    for j in range(10, number+1):
      for i in range(0, number-count):
        final = final + " "
      for p in range(0, count+1):
        final = final + str(j) + " "
      final = final +"\n"
      count += 1

      # then it will return the final pyramid as a string
  
  return final