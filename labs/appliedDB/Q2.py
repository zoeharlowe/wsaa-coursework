
# Main function

def main():
	# Initialise array
	array = []

	display_menu()
	
	while True:
		choice = input("Enter choice: ")
		
		if (choice == "1"):
			array = fill_array()
			display_menu()
		elif (choice == "2"):
			print(array)
			display_menu()
		elif (choice == "3"):
			find_gt_in_array(array)
			display_menu()
		elif (choice == "4"):
			break;
		else:
			display_menu()
			
			
def fill_array():
	array = []
	input_num = int(input("Enter numbers separated by spaces (enter -1 to stop): "))
	
	while input_num != -1:
		array.append(input_num)
		input_num = int(input("Enter numbers separated by spaces (enter -1 to stop): "))
	if input_num == -1:
		return array
	if ValueError:
		print("Invalid input. Please enter numbers only.")
		return fill_array()

def find_gt_in_array(array):
	num_list = []
	num = int(input("Enter a number: "))

	for i in array:
		if num < i:
			num_list.append(i)
		elif num >= i:
			continue
		
	print(num_list)
		

def display_menu():
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - Fill Array")
    print("2 - Print Array")
    print("3 - Find > in Array")
    print("4 - Exit")

if __name__ == "__main__":
	# execute only if run as a script 
	main()
