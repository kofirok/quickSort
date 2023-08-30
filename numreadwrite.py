import os

def reading(folder_name): 
    # List to store the numbers read from each file
    list_of_nums = []
    
    # Iterate through each file in the folder
    for filename in os.listdir(folder_name):
        # Open the file in read mode
        infile = open(os.path.join(folder_name, filename), 'r')
        
        # List to store the numbers read from the current file
        current_file_nums = []
        
        # Iterate through each line in the file
        for num in infile:
            
            # Convert the string representation of a number to an integer
            anumber = int(num)
            # Append the integer to the list of numbers for the current file
            current_file_nums.append(anumber)
        
        # Append the list of numbers for the current file to the overall list of numbers
        list_of_nums.append(current_file_nums)
        
        # Close the file
        infile.close()
    
    # Print the list of numbers
    print(list_of_nums)
    
    # Return the list of numbers
    return list_of_nums

def writing(list_of_nums, current_assignment):

    
    # Default filename if none is provided
    filename = f"input{current_assignment}_sorted.txt"
    
    # Open the file in write mode
    outfile = open(filename, 'w')
        
    # Iterate through each number in the list
    for num in list_of_nums:
        # Write the string representation of the number to the file
        outfile.write(str(num) + '\n')
    
    # Close the file
    outfile.close()