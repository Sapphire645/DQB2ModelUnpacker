# DQB2ModelUnpacker
Basic python scripts to split the files from the linkdata into their respective g1m and g1t files and merge the files back into the game's format

## How it works

**Extractor.py**
- Place the raw binary file in the same folder as the script. Run Extractor.py and write the file's name (with the extension). It will split the original file into its g1t and g1m files.

**Packer.py**
- Place the g1t and g1m files in the same folder as the script. Run Packer.py and write the original binary file's name (with the extension). It will pack the 2 files back into a single file with the ".edit" extension.

## How to extract and inject the binary files

https://github.com/turtle-insect/DQB2. As always use turtle-insect's Linkdata Browser. (Many thanks!)

## How to edit the files

**g1t**
- https://www.youtube.com/watch?v=htxLAINoKZE This video by BenXC has all information on how to edit g1t files. (Many thanks to him too!)

**g1m**
- FOR VIEWING: Use Noesis:*https://richwhitehouse.com/index.php?content=inc_projects.php* with *https://github.com/Joschuka/Project-G1M* Project G1M's plugin.
- FOR EXTRACTING: Use *https://github.com/eArmada8/gust_stuff* to turn the g1m file into .vb and .ib files. (and viceversa)
- FOR EDITING: Use Blender with this plugin: *https://github.com/DarkStarSword/3d-fixes/blob/master/blender_3dmigoto.py* that will allow you to open and edit the .vb and .ib files. If that script seemingly does not work properly (for me it saved a .vb0 file instead of the .vb file) try this one *https://www.loverslab.com/topic/194350-modders-resource-blender-add-on-for-3dmigoto-version-293-or-above/*.

(Also many thanks to everyone who worked on all these tools!)

**Example of edited model:**
![image](https://github.com/Sapphire645/DQB2ModelUnpacker/assets/167467641/e7c3636e-7131-4181-8d84-d6e5a7aea957)
