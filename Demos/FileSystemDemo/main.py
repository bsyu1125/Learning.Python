import FileWriter
import os.path

# Defining main function
def main():
    print("hey there")
    print("Give me a file name to create. I will keep appending 'Poop' to the name until it is unique:")
    file = os.path.join(os.getcwd(), input())
    createdFile = FileWriter.CreateFileWithName(file)
    print(f"Created file: {createdFile}")
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()