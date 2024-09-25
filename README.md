# Simple Dictionary Attack Password Crack

There are multiple versions of this program.  
Version 1 takes a SHA-256 hash as input and checks it against the list of passwords in the textfile.   
Version 2 takes a SHA-256 hash as input and checks it against the textfile passwords, but also against potential variations of the passwords 
that contain special characters for "added security."  
Version 3 will ask for a SHA-256 hash as input from the command line using argparse for a more user-friendly interface.   
