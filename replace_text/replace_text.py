import os

print(r'Kindly provide the path of folder')
path = str(input())
print(r'for how many words you want to replace')
num_times = int(input())
raw = []
replacement = []

for i in range(num_times):
  print('Which word you want to replace')
  raw.append(str(input()))
  print('What is the word you want')
  replacement.append(str(input()))

folder_path = r'replaced_str'
if os.path.exists(folder_path) == False:
  os.mkdir(folder_path)

for root,fpaths,files in os.walk(path):
  for file in files:
    single_path = os.path.join(root, file)
    try:
      f = open(single_path)
      lines = f.readlines()
      if os.path.exists(os.path.join(folder_path, file)) == True:
        f_change = open(os.path.join(folder_path, r'copy'+file), 'w')
      else:
        f_change = open(os.path.join(folder_path, file), 'w')
      for line in lines:
        for idx in range(num_times):
          line = line.replace(raw[idx], replacement[idx])
        f_change.writelines(line)
      f_change.close()
    except:
      print(f'{file} cannot be written')