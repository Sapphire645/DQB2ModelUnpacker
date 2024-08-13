import os #directory
import struct
import pickle as pk
import math

def Folder_Size(start_path):
    total_size = 0
    folder_add = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
            folder_add += 8
            total_size += 8
        for i in dirnames:
            folder_add += 12
            total_size += 12
    return total_size,folder_add

def Pack_Data(List,number,Current_Path):
    with open(Current_Path+"/"+a, 'rb') as f2:
        content = f2.read()
        f1.write(content[List[0]:List[0]+List[1]])

def Pack_Files(List,path,f1,start = 0):
    Past_Path = path
    files = [f for f in os.listdir(path) if f != 'Struct']
    folder = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f)) and f != 'Struct']
##    for folders in os.listdir(path):  # loop over all files
##        if os.path.isdir(os.path.join(path, folders)):  # if it's a directory
##            folder =   # increment counter

#    print("There are {} folders".format(folder_count))
##    #print(os.listdir(path))
##    print(files)
##    print(folder)
    #print(len(files))
    
    Folder_Num = 0
    Header = struct.pack('I', (len(files)))
    f1.write(Header)
    AddedSize = 0
    AddedSize_past = 0
    Size = 0
    AddedFolder = 0
    AddedFolder_past = 0
    Size_Total = Size
    for i in files:
        if i in folder:
            AddedSize += 4
            start = 4
            Size,AddedFolder = Folder_Size(path+"/"+i)
        else:
            Size = os.path.getsize(path+"/"+i)
            start = 0
        Pointer = (8*(len(files))) + Size_Total + AddedSize_past + 4
        Pointer_Byte = struct.pack('I', Pointer)
        f1.write(Pointer_Byte)
        Size_Total += Size
        Size_Byte = struct.pack('I', math.ceil((Size+start)/4)*4)
        f1.write(Size_Byte)
        AddedFolder_past += AddedFolder
        AddedSize_past = AddedSize

    for i in files:
        if i in folder:
            Pack_Files(List,path+"/"+i,f1)
        else:
            with open(path+"/"+i, 'rb') as fileAp:
                fileAp_content = fileAp.read()
                fileAp_size = len(fileAp_content)
            f1.write(fileAp_content)
                

        
        #print(i,Folder_Size(path+"/"+i))
##    for Iterate_File in List:
##        if type(Iterate_File[0]) == type(0):
##            if(Iterate_File[1] > 0):
##                Current_Path = path+"/"+str(Iterate_File[0])
##                f1.seek()
##                f1.write(
##            else:
##                Current_Path = path
##                f1.seek(0)
##                f1.write(len(List)-1)
##                f1.write
        
def Main(name):
    Folder_Name = name.replace(".", "")
    Directory = os.getcwd()+"/"+Folder_Name
    with open(Folder_Name+"/Struct", 'rb') as f1:
        File_Structure = pk.load(f1)
    with open(os.getcwd()+"/"+name+".edit", 'wb') as f1:   
        Pack_Files(File_Structure,Directory,f1,4)
        
print("Name:")
name = input()
#name = "06033GodrothAn.unpack"
Main(name)
#name = "02050MalModel.unpack"
