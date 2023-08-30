import quicksort

# Import the reading and writing functions from the numreadwrite class
from numreadwrite import reading, writing


import sys

def main(folder_name):
    # Read the contents of the file specified in the filename argument
    num_arrays = reading(folder_name)
    current_assignment = ""
    count = 0
    # Sort the array and gather the runtime statistics
    for array in num_arrays:
      # Initialize the number of values, comparisons, and assignments
      num_values = len(array)
      num_comparisons = 0
      num_assignments = 0
  
     

      sorted_array, c, a = quicksort.quickSort(array, 0, len(array)-1, num_comparisons, num_assignments)
      num_comparisons = c
      num_assignments = a
      file_Name = "Input"
      count += 1
      

      # Write the sorted array to the file
      writing(sorted_array, sorted_array[0])
   
      # Print the number of values, comparisons, and assignments
      print("")
      print(file_Name, count, "Results:")
      print("Number of values sorted:", num_values)
      print("Number of comparisons:", c)
      print("Number of assignments:", a)
      print("")
 
# Call the main function if the script is run as the main program
if __name__ == "__main__":
  main(sys.argv[1])

