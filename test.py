"""This file is to be used simply to import fucntions from \
other files and execute them."""

import file_rename as rename
import os

path = "C:\Users\dchauhan\Desktop\New folder"
filenames = os.listdir(path)
for fileName in filenames:
    # remove dash and sheet names
    rename.removeDashAndSheetName(path, fileName)
    # Adding prefix to a file
    # rename.addPrefix(path, fileName, "RCD_SGS_")

    # Adding suffix to a file
    # rename.addSuffixToFile(path, fileName, "_DCI COMMENTS")

    # Adding suffix to a directory
    # rename.addSuffix(path, fileName, "_DCI COMMENTS")
