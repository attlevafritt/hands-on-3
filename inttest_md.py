import md
import os.path
import sys


md.run_md()
# make tests to verify that md program did run as intended.

# check that the output trajectory file exists. 
if os.path.isfile('./cu.traj'):
      print("The trajectory file exists")
else:
      #sys.exit(1)
      raise AssertionError("Output trajectory file doesn't exist.")
      
      
      

 
