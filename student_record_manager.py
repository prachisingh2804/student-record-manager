while True:
	print("===== STUDENT RECORD MANAGER =====")
	print("1. Add Student ")
	print("2. View Student ")
	print("3. Exit")
	choice = input("Enter your choice: ")
	if choice == "1":
		name = input("Enter your name: ")
		age = int(input("Enter your age: "))
		with open("students.txt", "a") as file:
			file.write("Name:" + name + "\n")
			file.write("Age:" + str(age) + "\n")
		print("Student added successfully!")
		
	if choice == "2":
		with open("students.txt", "r") as file:
		  content = file.read()
		  print(content)
	if choice == "3":
	 	  print("Thank you for using Student Record Manager!")
	 	  break
