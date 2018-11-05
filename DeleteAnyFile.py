mport os

filetodelete = input("Enter the file name:")
os.chdir(r'd:/')
path = os.getcwd()


all_file = []
for path, dirs, files in os.walk(path):

      for file in files:
            all_file.append(file)

            if file == filetodelete:
                  os.chdir(path)
                  os.unlink(file)
                  print(file + ' is removed at ' + path)
                  exit()
           
print("file no more")
