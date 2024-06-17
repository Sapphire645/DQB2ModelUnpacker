import os #directory
import struct

def extractFile(content, beggining, end):
    loop = True
    while loop == True:
        if content[beggining] == 0x47:
            extension = ".g1t"
            loop = False
        else:
            if content[beggining] == 0x5F:
                extension = ".g1m"
                end = end + 16
                loop = False
            else:
                beggining = beggining + 4
    with open(name+extension, 'wb') as f1:
        f1.write(content[beggining:end+4])
    
print("Name:")
name = input()
with open(name, 'rb') as file:
    content = file.read()
    header_number = content[:4]
    print(content[:4])
    number_files = struct.unpack('I', header_number)[0]
    for i in range(number_files):
        a,b,c = 4+(i*4),8+(i*4),12+(i*4)
        pointer1 = content[a:b]
        number_pointer1 = struct.unpack('I', pointer1)[0]
        pointer2 = content[b:c]
        number_pointer2 = struct.unpack('I', pointer2)[0]
        if number_files - 1 == i:
            number_pointer2 = len(content)
        extractFile(content, number_pointer1,number_pointer2)

    
