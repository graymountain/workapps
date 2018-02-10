"""This file is to be used simply to import fucntions from \
other files and execute them."""

import file_rename as rename
import os

path = "C:\Users\dchauhan\Desktop\New folder"
filenames = os.listdir(path)
for fileName in filenames:
    rename.addPrefix(path, fileName, "RCD_SGS_")
    # rename.addSuffixToFile(path, fileName, "_DCI COMMENTS")
    # rename.addSuffix(path, fileName, "_DCI COMMENTS")
