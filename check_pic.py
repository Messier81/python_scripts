# script to print picture names by folders after selecting random ones from all pictures

import os

with open("output.txt", "w") as a:
  alb_files = []
  for path, subdirs, files in os.walk(r'insert path to list of wanted photos'):
    for filename in files:
      alb_files.append(filename)
  for path, subdirs, files in os.walk(r'insert path to folder with all photos'):
    pic_d = {}
    for filename in files:
      f = os.path.join(path, filename)
      f = str(f)
      f = f.split("\\")
      s = " > ".join(f[4:len(f)])
      p = " > ".join(f[4:len(f)-1])
      if p not in pic_d:
        pic_d[p] = []
      if f[len(f)-1] in alb_files:
        pic_d[p].append(f[len(f)-1])
    for fol in pic_d:
      a.write("Folder: " + fol + os.linesep)
      for pic in pic_d[fol]:
        a.write(pic + '\n')
      a.write(os.linesep)
  print("pics checked")