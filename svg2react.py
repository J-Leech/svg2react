import sys
import os
from os import listdir

files = listdir(sys.argv[1])
os.chdir(sys.argv[1])

for f in files:
  if ".svg" in f:
    thisOne = open("./" + f, "r")

    currentText = thisOne.read()
    name = f.replace(".svg", "").replace("_", "").capitalize()

    thisOne.close()

    newText = "import Svg, {Path} from 'react-native-svg'\nimport React from 'react'\nimport {View} from 'react-native'\n\nexport default class " + name + " extends React.Component {\nrender() {\nreturn (\n<View>\n" + currentText + "</View>\n)\n}\n}"

    newOne = open(name + ".js", "w")
    newOne.write(newText)
    
    newOne.close()