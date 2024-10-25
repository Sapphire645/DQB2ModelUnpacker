# DQB2ModelUnpacker
Basic python scripts to split the files from the linkdata into their respective g1m and g1t files and merge the files back into the game's format

Now with added support for animation files. You can extract the animation files, and add/remove/replace the files you want. If you don't know what you're doing (like me) it will break most of the time

Has not been tested with the giant item model file but it should work too.

Uses the libraries os, struct, and pickle. Packer also uses the library math.

## How it works

**ExtractorV3.py**
- Place the raw binary file (Turtle Insect LINKDATA browser's .unpack file) in the same folder as the script. Run ExtractorV3.py and write the file's name (with the extension). It will split the original file into folders, g1m, g1t, g2a, and other binary files.
- Some files will look weird/empty. That's how the file is formatted. They probably are important so don't remove them. The folder-> File extraction is an aproximation, but it's probably more complicated than that, involving various pointers to the same data through different "folder" paths.
- A "Struct" file is generated. This ended up not being important but don't delete it. 

**PackerV3.py**
- Run PackerV3.py and write the original .unpack file's name (with the extension). It will repack the contents of the extracted folder back into the original file with the ".edit" extension.
- Do not rename the folders or the files, the numbers are ordered.
  
### Outdated, works only for g1m-g1t pairs
  
**Extractor.py**
- Place the raw binary file (Turtle Insect LINKDATA browser's .unpack file) in the same folder as the script. Run Extractor.py and write the file's name (with the extension). It will split the original file into its g1t and g1m files.

**Packer.py**
- Place the g1t and g1m files in the same folder as the script. Run Packer.py and write the original .unpack file's name (with the extension). It will pack the 2 files back into a single file with the ".edit" extension.

## How to extract and inject the binary files

https://github.com/turtle-insect/DQB2. As always use turtle-insect's Linkdata Browser. (Many thanks!)

## How to edit the files

**g1t**
- https://www.youtube.com/watch?v=htxLAINoKZE This video by BenXC has all information on how to edit g1t files. (Many thanks to him too!)

**g1m**
- FOR VIEWING: Use Noesis:*https://richwhitehouse.com/index.php?content=inc_projects.php* with *https://github.com/Joschuka/Project-G1M* Project G1M's plugin.
- FOR EXTRACTING: Use *https://github.com/eArmada8/gust_stuff* to turn the g1m file into .vb and .ib files. (and viceversa)
- FOR EDITING: Use Blender with this plugin: *https://github.com/DarkStarSword/3d-fixes/blob/master/blender_3dmigoto.py* that will allow you to open and edit the .vb and .ib files. If that script seemingly does not work properly (for me it saved a .vb0 file instead of the .vb file) try this one *https://www.loverslab.com/topic/194350-modders-resource-blender-add-on-for-3dmigoto-version-293-or-above/*.

**g2a**
- FOR VIEWING: Use Noesis:*https://richwhitehouse.com/index.php?content=inc_projects.php* with *https://github.com/Joschuka/Project-G1M* Project G1M's plugin.
- You have to manually change a variable from "False" to "True" in the script. It's listed on the readme.

  
(Also many thanks to everyone who worked on all these tools!)

**Example of edited model:**
![image](https://github.com/Sapphire645/DQB2ModelUnpacker/assets/167467641/e7c3636e-7131-4181-8d84-d6e5a7aea957)
**Example of edited animations:**
<br>https://www.tumblr.com/sapphire-rb/758698080353828864/mild-success-on-unrelated-news-local-winged-god
