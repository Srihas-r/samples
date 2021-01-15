age = input("Enter your age: ")
# if age is less than 18 - say you are not allowed 
# if age is greater than or equal  to 18 but less than 21 - say you are allowed but you cannot drink
# if age is greater than 21 - say you allowed to drink 


#if age:
    #if int(age) < 18:
	  #  print("sorry, you are not allowed as people with age " + age + " are considered minor")
	#elif int(age) >= 18 and int(age) < 21:
	 #   print("you are allowed as people with age " + age + " are not considered minor but you cant drink")
	#elif int(age) >= 21:
	  #  print("you are allowed to drink as people with age " + age + " are considered major")
	#else:
		#print(input("please enter a valid age: "))
#else:
	#input("Enter a valid age: ")

if age:
	if int(age) < 18:
		print("sorry, you are not allowed as people with age " + age + " are considered minor")
	elif int(age) >= 18 and int(age) < 21:
		print("you are allowed as people with age " + age + " are not considered minor but you cant drink")
	elif int(age) >= 21:
		print("you are allowed to drink as people with age " + age + " are considered major")
else:
	input("Enter a valid age: ")


