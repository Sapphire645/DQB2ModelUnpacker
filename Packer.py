import os #directory
import struct

print("Name:")
name = input()
with open(name, 'rb') as file:
    content = file.read()
    with open(name+".edit", 'wb') as f1:
        f1.write(bytearray([2,0,0,0]))
        f1.write(bytearray([0x14,0,0,0]))
        with open(name+".g1m", 'rb') as g1m:
            g1m_content = g1m.read()
            g1m_size = len(g1m_content)
            f1.write(struct.pack("i", g1m_size))
            f1.write(struct.pack("i", g1m_size+20))
        with open(name+".g1t", 'rb') as g1t:
            g1t_content = g1t.read()
            g1t_size = len(g1t_content)
            f1.write(struct.pack("i", g1t_size))
        f1.write(g1m_content)
        f1.write(g1t_content)
