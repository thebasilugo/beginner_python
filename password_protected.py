while True:
	password = input("What is the password? >>")
	if password == 'What':
		print("That's the password.")
		break

	elif password == 'what':
		print("Try again ;)")

	else:
		print("Wrong password. Try again >>")