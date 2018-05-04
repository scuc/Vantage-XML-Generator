#!python3

import os
import shutil


#change the python working directory to the project watch folder
watch_folder = 'path/to/project/watch/folder'
output_dir01 = 'path/to/project/output/folder'
output02 = 'path/to/project/secondary/output/folder'
path_list=[]

def project_zip():
    os.chdir(watch_folder)
    #check the watch folder for .DS files, if exists, remove it. this is so the script does not create and XML from the .DS
    if os.path.isfile(os.path.join(watch_folder,'.DS_Store')): 
        os.remove('.DS_Store')
        
    #get a list of all the folder names under the given path.
    dir_list =[name for name in os.listdir(watch_folder)
        if os.path.isdir(os.path.join(watch_folder, name))]
    dir_count = len(dir_list)
    len_Lists = [[] for i in range(dir_count)]
    count = 0

    #loop through directory list, check the len of the file path, if its < 260, archive and move
    for project_folder in dir_list:
        full_path = os.path.join(watch_folder, project_folder) 
        len_Lists[count].append(project_folder)
        for root, dirs, files in os.walk(full_path):
            len_Lists[count].append(len(root))
            for file in files: 
                file_path = os.path.join(root,file)
                len_Lists[count].append(len(file_path))
        count = count + 1


    for lenList in len_Lists:
        x = os.chdir(watch_folder)
        y = os.path.join(watch_folder,lenList[0])
        z = lenList[0]
        for n,num in enumerate(lenList):
            if type(num) == str:
                pass
            elif num >= 250:
                shutil.move(y,name02)
                break
            elif (n == len(lenList)-1) and not (os.path.exists(z + '.xml')) or (os.path.exists(z + '.zip')):
                xml_name = open(z + '.xml','a')
                xml_name.write(
                    "<?xml version=\"1.0\" encoding=\"utf-8\"?>" + "\n" +
                        "<project>" + "\n" + 
                            "<ProjectName>" + z + "</ProjectName>" + "\n" +
                            "<ProjectPath>"+ y + "</ProjectPath>" + "\n" +
                        "</project>" + "\n"
                    )
                xml_name.close()
                os.chmod(y + '.xml', 0o777)
            else: 
                continue
    exit()

project_zip()

