import time
import os
start_time = time.time()

rootdir=('/root/')
        
for folder, dirs, files in os.walk(rootdir):
   for file in files:
        if file.endswith('.config'):
                fullpath = os.path.join(folder, file)
                with open(fullpath, 'r') as f:
                    for line in f:
                        if "redirect" in line:
                                 print(fullpath)
                                 break

print("Script Took : --- %s seconds --- " % (time.time() - start_time))

