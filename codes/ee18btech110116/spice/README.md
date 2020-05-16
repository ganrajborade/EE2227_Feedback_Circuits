 # Details regarding files in the directory:
 ee18btech11016_sim.net is a netlist for simulating the feedback system having PM = 45 degrees 
 
 ee18btech11016_simulation.py is a python file to plot the ee18btech11016_sim.dat  
 
 ## Instructions for Simulation and plotting the output.
 
 ### Setup
 --> In the terminal use the 'cd' command to move to the directory where .net files and .py files are present.  
 --> Make Sure that all the .net and .py files are present in your present directory . 'ls' command is used to list out the files in the present directory.
 
 
 ### Simulation : 
 -->Enter the following command . This simulates the 'ee18btech11016_sim.net' file and creates a 'ee18btech11016_sim.dat' file.
 ``` 
ngspice ee18btech1016_sim.net
```

--> Exit from ngspice cmd line using the following code . This gets you back to the present working directory.
 ``` 
exit
```

--> Enter the following command . This runs  'ee18btech11016_simulation.py'  which plots a plot of 'ee18btech11016_sim.dat' file
and save it as 'ee18btech11016_spice_result.pdf'
``` 
python3 ee18btech11016_simulation.py
```

