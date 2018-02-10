"""This module contains some file / directory renaming methods"""
import os


def removeDashAndSheetName(path, fileName):
    """
    This function replaces '-' with '_' and \
    removes sheet names from the file names.
    Args:
        path: An absolute path to the directory on your system \
                where you want this operation to happen.
        fileName: Name of the file / directory in the parent \
                directory where this operation happens.
    """
    oldName = os.path.join(path, fileName)
    newFileName = fileName.replace("-", "_")
    sheetSizes = ["A0", "A1", "A2", "A3", "A4"]
    for sheet in sheetSizes:
        if sheet in fileName:
            newFileName = newFileName[3:]
            print "Sheet names removed"

    newName = os.path.join(path, newFileName)
    os.rename(oldName, newName)


def addPrefix(path, fileName, prefix):
    """
    This function adds a prefix to the file / directory name
    Args:
        path: An absolute path to the directory on your system \
                where you want this operation to happen.
        fileName: Name of the file / directory in the parent \
                directory where this operation happens.
        prefix: A string that needs to be added as prefix to the file \
                or the directory name.
    """
    oldName = os.path.join(path, fileName)
    newFileName = prefix + fileName
    newName = os.path.join(path, newFileName)
    os.rename(oldName, newName)


def addSuffixToFile(path, fileName, suffix):
    """
    This function adds a suffix to the file name. It adds the suffix\
    before the file extension.
    Args:
        path: An absolute path to the directory on your system \
                where you want this operation to happen.
        fileName: Name of the file / directory in the parent \
                directory where this operation happens.
        suffix: A string that needs to be added as prefix to the file \
                or the directory name.
    """
    oldName = os.path.join(path, fileName)
    firstPart = fileName.split(".")[0]
    secondPart = fileName.split(".")[-1]
    newFileName = firstPart + suffix + "." + secondPart
    newName = os.path.join(path, newFileName)
    os.rename(oldName, newName)


def addSuffix(path, fileName, suffix):
    """
    This function adds a suffix to the directory name
    Args:
        path: An absolute path to the directory on your system \
                where you want this operation to happen.
        fileName: Name of the file / directory in the parent \
                directory where this operation happens.
        suffix: A string that needs to be added as prefix to the file \
                or the directory name.
    """
    oldName = os.path.join(path, fileName)
    newFileName = fileName + suffix
    newName = os.path.join(path, newFileName)
    os.rename(oldName, newName)
