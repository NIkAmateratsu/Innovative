import os

filetodelete = input("Enter the file name:")
if os.path.exists(filetodelete):
   os.remove(filetodelete)
else:
	print("The file does not exits")