tasks = []
try:
	with open("data.txt","r") as file:    # try means if file exists open it otherwise its ok                            
		for line in file:
			tasks.append(line.strip())
except:
	pass
while True:
	print("\n...To do list....")
	print("1.Add tasks")
	print("2.Show tasks")
	print("3.Delete tasks")
	print("4.Exit")
	choice = input("enter your choice:")
	if choice == '1':
		task = input("enter task: ")
		tasks.append(task)
		print("Task added")
	elif choice == '2':
		if not tasks:
			print("No tasks available")
		else:
			for i in range(len(tasks)):
				print(i+1,tasks[i])
	elif choice == "3":
		if not tasks:
			print("No tasks available")
		else:
			for i in range(len(tasks)):
				print(i+1,tasks[i])
			num = int(input("enter task number:"))
			tasks.pop(num - 1)
	elif choice == "4":
		with open("data.txt","w") as file:
			for task in tasks:      #if file doesnt exists python creates it , if exists python overwrites it,  
				file.write(task + "\n")
		break


