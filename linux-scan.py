###############################################################################
 
import time
import os
import sys
  
line_count = 0  # Initialize the line number
#search_term = "DevWeb"
#file_endswith = ".config"
start_time = time.time() # We want to see how long the script executes.

print("This application will scan the directory structure of this linux-system for a string...\n")
print("If no values are entered, the defaults will be used: \n")

server = input("Server Name or directory: / (root) : ")
if not server:
    server = "/"
search_term = input("Enter the Search String (default is web ) : ")
if not search_term:
    #search_term = "DevWeb"
	search_term = "web"
# //after this point, the program returns annything with config.
# //need to fix this as it is providng erronious reports.
file_endswith = input("Enter the file extention you are looking for: ( Eg: .config) : ")
if not file_endswith:
    file_endswith = ".config"
                    
  
print("Starting scan: .. Looking for srting " + search_term)
   
# rootdir=('Z:\\') # Mapped a Network Share to a local Drive (Z)
rootdir=(server) # Use a local Drive 
  
for folder, dirs, files in os.walk(rootdir):
    
    for file in files:
        
        if file.endswith('.config'):
            
            fullpath = os.path.join(folder, file)
              
            with open(fullpath, 'r') as f:
                
                print("\n")
                line_count = 0
                print(fullpath) 
                for line in f.readlines():
                    
                    line_count += 1
                    if search_term in line:
                        print( search_term + " Found on  line: %d " % line_count)
                           
 
# Print the time taken sumary.                            
print("\nScript Took : --- %s seconds --- " % round( (time.time() - start_time)))
 
