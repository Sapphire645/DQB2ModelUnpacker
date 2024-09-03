import os #directory
import struct
import pickle as pk

def Split_Folder(content,pointer,Folder_Structure,Full):
    Number_Files = content[pointer:pointer+4]
    Number_Files = struct.unpack('I', Number_Files)[0]
    for Iterate in range(Number_Files):
        Pointer = content[pointer+4+(8*Iterate):pointer+8+(8*Iterate)]
        Pointer = struct.unpack('I', Pointer)[0]
        Size = content[pointer+8+(8*Iterate):pointer+12+(8*Iterate)]
        Size = struct.unpack('I', Size)[0]
        if [Pointer+pointer,Size] in Full or Size == 0:
            Folder_Structure.append([False,Pointer+pointer,Size,Iterate])
        else:
            Folder_Structure.append([True,Pointer+pointer,Size,Iterate])
            Full.append([Pointer+pointer,Size])
    return Folder_Structure,Full
    
def Proccess_Folder_Files(content,Folder_Structure,Full):
    index = 0
    end = True
    Iter = Folder_Structure[1].copy()
    for [Real,Pointer,Size,Number_Files] in Iter:
        if Real:
            Header = content[Pointer:Pointer+4]
            Header = struct.unpack('I', Header)[0]
            if Header < 0x26F and Header > 0x00 and Size > 0:
                end = False
                Folder_Data = [[Number_Files,Pointer,Size]]
                Folder_After = []
                del Folder_Structure[1][index]
                #print(Folder_Structure)
                Folder_After,Full = Split_Folder(content,Pointer,[],Full)
                Folder_Data.append(Folder_After)
                Folder_Structure.append(Folder_Data)
                #print("FOLDER: ",Folder_Structure)
            else:
                index += 1
        else:
            index += 1
    if Folder_Structure[1] == []:
        del Folder_Structure[1]
    return Folder_Structure, end,Full

def Extract_Data(content,List,Current_Path):
    if content[List[1]] == 0x47:
        extension = ".g1t"
    else:
        if content[List[1]] == 0x5F:
            if content[List[1]+1] ==  0x41:
                extension = ".g2a"
            else:
                extension = ".g1m"
        else:
            extension = ".bin"
    if not os.path.exists(Current_Path):
        os.makedirs(Current_Path)
    with open(Current_Path+"/"+str(List[3]).zfill(3)+extension, 'wb') as f1:
        f1.write(content[List[1]:List[1]+List[2]])
        
def Extract_Files(content,List,path):
    Past_Path = path
    Current_Path = path
    for Iterate_File in List:
        if type(Iterate_File[0]) == type(0):
            if(Iterate_File[1] > 0):
                Current_Path = path+"/"+str(Iterate_File[0]).zfill(3)
            else:
                Current_Path = path
        else:
            if type(Iterate_File[0]) == type([]):
                Extract_Files(content,Iterate_File,Current_Path)
            else:
                Extract_Data(content,Iterate_File,Current_Path)


def loop(File_Structure,content):
    
    return File_Structure

def Main(name):
    File_Structure = [[0,-1,-1]]
    Folder = 0
    with open(name, 'rb') as file:
        content = file.read()
    Header = content[:4]
    Header = struct.unpack('I', Header)[0]
    if Header < 0x26F and Header > 0x00:
        File_After,Full = Split_Folder(content,0,[],[])
        File_Structure.append(File_After)
        File_Structure, end,Full = Proccess_Folder_Files(content,File_Structure,Full)
        if end == False:
            index = 1
            for Folder_List in File_Structure[1:]:
                if type(Folder_List[0][0]) == type(0):
                    Folder_Struct, end,Full = Proccess_Folder_Files(content,Folder_List,Full)
                    File_Structure[index] = Folder_Struct
                index += 1
                    
    name = name.replace(".", "")
    with open(os.getcwd()+"/Struct.txt", 'w') as f1:
        Text = str(File_Structure)
        Text = Text.replace(", [", ",\n   [")
        ##for I in File_Structure:
        f1.write(Text)
    if not os.path.exists(os.getcwd()+"/"+name):
        os.makedirs(os.getcwd()+"/"+name)
    with open(os.getcwd()+"/"+name+"/Struct", 'wb') as f1:
        pk.dump(File_Structure, f1)
    #print(File_Structure)
    #print(Full)
    Extract_Files(content,File_Structure,os.getcwd()+"/"+name)





print("Name:")
name = input()
#name = "06033GodrothAn.unpack"
Main(name)
#Main("05976animation.unpack")

