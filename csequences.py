import os, shutil

src = './SequenceFiles/'
src_files = os.listdir(src)
textToReplace = '.dpf\tTimed\t5.000\t' #5 seconds
newText = '.dpf\tTimed\t10.000\t' #10 seconds

for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    new_file_name = os.path.join(src, 'C_'+file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, new_file_name)
        with open(new_file_name) as new_file:
            file_contents = new_file.read()
        file_contents = file_contents.replace(textToReplace, newText)
        with open(new_file_name, 'w') as new_file:
            new_file.write(file_contents)