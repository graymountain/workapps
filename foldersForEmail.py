"""A scrpt for file grouping and folder creation for limited size emailing by Devang """

"""
Emailing to someone is an integral part of our lives. In most mdern day workplaces, email
communication is central to general workflow and project delivery. When dealing with other
teams, we often have to limit our email size to suite to the recipient's requirement. This
processs entails, folder creation of size lesser than the incoming email size limit for the
recipient. At work, there were many instances when I had to go through this procedure, hence
I decided to capture this process in Python to automate file grouping and folder creation.
It goes like this.
"""

import os
import os.path
import shutil





def CheckPath(Path):

    """
    Checks is User input for path is as expected or not.
    """

    NormalInput = ":\\"
    ExitCall = "e"
    ExitCall01 = "E"

    if NormalInput not in Path and ExitCall not in Path and ExitCall01 not in Path:
        return False
    else:
        return True





def StripPath(Path):
    """
    Stimply strips quotes around the path
    and returns the path
    Input(Path) = The original folder path
    Return = The path stripped of quotes
    """
    
    if '"' in Path:
        Path = Path.strip('"')
        return Path
    else:
        return Path



def ReturnMailSize(MailSizeLimit):

    """
    Extracts the number if the user type (MailSize)MB or (MailSize)mbs
    or anythiing like that. Also running various checks on user input.
    Input(MailSizeLimit) = String
    Return = Integer
    """

    # Taking out zeroes if the number starts with a lot of zeroes
    if MailSizeLimit[0] == '0':
        Stripped = MailSizeLimit.strip('0')
        MailSizeLimit = Stripped

    elif MailSizeLimit[0] != '0':
        MailSizeLimit = MailSizeLimit

    # Extracting numbers from the string
    Number = " "
    for letter in MailSizeLimit:
        if letter.lower() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            Number += letter

    # Checking if an insanely large or small number is entered
    if len(Number) > 5:
        print " "
        print "Hey, there seems to be something wrong with the MailSizeLimit you entered."
        print "It's either too small or too big. Try someting in the range of 1 and 10 the next time we relaunch."
        print "\n"*5
        return Launch()
    
    # Checing if user input is less than 1
    # If you are making folders for attachments, 1 MB seems like a good minimum value.
    if float(Number) < 1 :
        print " "
        print "Hey, that's a bit too small for an email attachment size."
        print "Please choose a  MailSizeLiimit of at least 1 mb the next time we launch."
        print "\n"*5
        return Launch()  

    # Ideal email size shall not be greater than 10 as per Wikipedia article in the code
    if float(Number) > 11:
        print " "
        print "Hey, that's a bit too much for an email attachment size. The ideal email attachment size is 10 mbs."
        print "Check this article if you have time: https://en.wikipedia.org/wiki/Email_attachment "
        print "Please choose MailSizeLiimit less than 10mbs next time we launch."
        print "\n"*5
        return Launch()
    
    # Allowing certain user inpus
    if float(Number) < 11 or float(Number) == 1 or float(Number) == 10 :
        return float(Number)



def CheckDir(Path):

    """
    Makiing list of all the folders in the selected folder
    """
    
    DirCount = 0
    DirList = []

    for roots, dirs, files in os.walk(Path):
        for dir in dirs:
            DirList.append(dir)
            DirCount += 1

    return [DirList , DirCount]



def GetFileSize(Path):
    
    """
    Returns file size in MBs
    Input(Path) = String
    Return = Float
    
    """
    
    Size = os.path.getsize(Path)
    return round(float(Size)/1048576, 2)



def PrintSize(Path, dirs):

    """
    Returns file sizes for all the files in the dirs
    Input(Path) = String
    Input (dirs) = List
    Return = Float

    """
    
    i = 0
    Total = 0
    while i < len(dirs):
        FilePath = Path + '\\' + dirs[i]
        Total += GetFileSize(FilePath)
        i += 1
    return Total



def MinimumFileSize(Path, dirs):

    """
    Returns the file size of smallest file
    in the folder
    """
    
    i = 0
    Total = []
    while i < len(dirs):
        FilePath = Path + '\\' + dirs[i]
        Total.append(GetFileSize(FilePath))
        i += 1
    return min(Total)


def TrimList(dirs, SelectGroup):

    """
    Trims selected (Unnecessary) items from
    Dictionary.
    Input(dirs) = List
    Input(SelectGroup) = List
    Return = List

    """
    
    if len(dirs) > 0:
        for item in SelectGroup:
            dirs.remove(item)
        return dirs
    else:
        return dirs



def Updatedirs(Path, dirs, MailSizeLimit):

    """
    The role of this function is to form group of
    files for which total file size does not exceed
    the set size limit.
    Input(Path) = Location of Folder
    Input(dirs) = List
    Return(SelectGroup) = First Group of Files with total file size
    lesser than set limit
    Return(round(TotalSize,2) = Total size of selected group of files
    reounded to two decimals
    Return(dirs) = Returning the list after removing selected files
    from the list

    """
    
    i = 0
    TotalSize = 0
    SelectGroup = []

    while TotalSize < MailSizeLimit and i < len(dirs):

        # For every file in the list if file size is less than MailSizeLimit,
        # Then, add the size of that file to TotalSize
        if TotalSize + GetFileSize(Path + '\\' + dirs[i]) < MailSizeLimit:
            TotalSize += GetFileSize(Path + '\\' + dirs[i])
            SelectGroup.append(dirs[i])
        else:
            TotalSize = TotalSize
            
        # Very important to exit the loop
        if MailSizeLimit - TotalSize == 0.01:
            break
        else:
            i += 1
            
    # Trimming selected files from the list
    dirs = TrimList(dirs, SelectGroup)

    # Whenever want multiple outputs, make a list
    return [SelectGroup, round(TotalSize,2), dirs]



def SeparateFiles(Path, dirs, MailSizeLimit):

    """
    Very important function.
    Takes Updatedirs function and applies to
    rest of the items on the list
    Input(Path) = Location of Folder
    Input(dirs) = List
    Return(FinalOutput) = A list of multiple lists
    Return(j) = Number of Folders to be created

    """

    j = 0
    FinalOutput = []
    TotalSize = 0

    while len(dirs) > 1:
        if len(dirs) > 0:

            # Caputring list generated through Updatedrs in another variable called 'Data.'
            Data = Updatedirs(Path, dirs, MailSizeLimit)

            # Appending only first list of Updatedirs result
            # To find out why only first list, look at return statement in Updatedirs
            FinalOutput.append(Data[0])

            # Appending only second list of Updatedirs result
            # To find out why only second list, look at return statement in Updatedirs
            TotalSize += Data[1]

            # This is very important. The list(dirs) is being updated after everytime
            # Seclected files are removed from the list
            dirs = Data[2]
            
            j += 1

    return [FinalOutput, j]



def MakeFolders(Path, Finallist):

    """
    Creates folders for email sending
    Input(Path) = Location of Folder
    Input(Finallist) = Number of folders to be created.
    This variable Finallist is defined inside FileSizeScan function
    that is defined below.
    Output = Folders are created
    Nothing fancy here.

    """
    FolderCount = int(Finallist[-1])
    i = 1
    while i < FolderCount + 1:
        os.makedirs(Path + '\\' + "Mail-" + str(i))
        i += 1



def MoveFiles(SampleList, Count, Path):

    """
    Simply moving files from one location to another.
    Nothing fancy here.

    """
    
    for item in SampleList:
        src = Path + '\\' + item
        dst = Path + '\\' + "Mail-" + str(Count)
        shutil.move(src, dst)



def MoveAllFiles(Finallist, Path):

    """
    Migrating all the selected files to folders that we have created
    This variable Finallist is defined inside FileSizeScan function
    that is defined below.
    
    """

    # Retriving the last value from Finallist.
    # The value that govern the number of folders to be created
    # The same value is used here as a counter
    FolderCount = int(Finallist[-1])

    # SelectGroup: which has all the groups of files to be migrate to folders
    Primary = Finallist[0]
    i = 1
    while i < FolderCount + 1:
        for item in Primary:
            MoveFiles(item, i, Path)
            i += 1



def MoveRemainigFiles(Finallist, dirs, Path):

    """

    This function picks up the leftover files after the operation
    if there are any

    """
    
    FolderCount = int(Finallist[-1])

    # Making an extra forlder
    Count = FolderCount + 1
    os.makedirs(Path + '\\' + "Mail-" + str(Count))

    # Picking up leftover fles and shifting them in the
    # Newly created folder
    for item in dirs:
        src = Path + '\\' + item
        dst = Path + '\\' + "Mail-" + str(Count)
        shutil.move(src, dst)



def MoveBakFiles(Subdir, LocalPath):

    """

    To move files back to the original folder
    Input(Subdir) = Defined in the next function
    Input(LocalPath) = Defined in the next function
    Output = Shifting of Files

    """
    
    for item in Subdir:
        src = LocalPath + '\\' + item
        dst = Path
        shutil.move(src, dst)



def MoveBakAllFiles(Path, dirs):

    """
    One of the most important functions.
    You don't want people to cut paste all the files back
    and then have them manually delete the folders in case
    they want to change the generated folders.

    """

    Path = raw_input("Paste here the same path you pasted before. >>>")
    print " "

    # Returns a list of all the files in this directory
    dirs = os.listdir(Path)
    
    Count = 0
    for item in dirs:

        # If they are folder created through this process, they out to have nnumerical endings.
        if item[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            Count += 1
    
    i = 1
    while i < Count + 1:

        # Gettiing path of each mail folder for supplying the same to MoveBakFiles function
        LocalPath = Path + '\\' + "Mail-" + str(i)

        # Gettiing list of each mail folder for supplying the same to MoveBakFiles function
        Subdir = os.listdir(LocalPath)
        
        MoveBakFiles(Subdir, LocalPath)

        # Removing the empty folder
        os.rmdir(LocalPath)
        
        i += 1



def AskToMoveBak(Path):
    while True:
        print " "
        Prompt = raw_input("Are you happy with all the folders created? if yes, then enter Y, If no, then enter N, and we will relaunch. >>> ")
        if Prompt.lower() == "y":
            print " "
            print "Alright. Since you are happy, we will exit and let you be happy!"
            return Endit()
        elif Prompt.lower() == "n":
            print " "
            print "Alright. Since you are not happy, we will relaunch so that you can change MailSizeLimit or move LargeFiles out of the folder."
            print "\n"*5

            # Extracting name of all the folders present in the path selected 
            NameOfFolders = CheckDir(Path)[0]
            # Cunting the number of folders in the path selected
            NumberOfFolders = CheckDir(Path)[1]


            for item in NameOfFolders:
                LocalPath = Path + '\\' + item

                # If folders is empty, remove right away
                if os.listdir(LocalPath) == []:
                    os.rmdir(LocalPath)

                # Else, shift all its files to the main folder and then delete it.
                else:
                    ListOfFiles = os.listdir(LocalPath)
                    for file in ListOfFiles:
                        src = LocalPath + '\\' + file
                        dst = Path
                        try:
                            shutil.move(src, dst)
                        except shutil.Error:
                            os.remove(Path + '\\' + file)
                    os.rmdir(LocalPath)


            return Launch()



def FileSizeScan(Path, dirs, MailSizeLimit):

    """
    Everything happens here.

    """
    i = 0
    LargeFiles = []

    # First we want to catch files with size higher than our MailSizeLimit
    # We will simply call them Large files
    while i < len(dirs):

        # Measuring file size of all the size in the list(dirs)
        for item in dirs:
            FilePath = Path + '\\' + item
            FileSize = GetFileSize(FilePath)

            # If the file size is greater than MailSizeLimit we want to add them to
            # a new list called LargeFiles
            if FileSize > MailSizeLimit:
                print " *** File size of " + item + " is too high for this email. ***"
                LargeFiles.append(item)

        # If Large files are found
        if len(LargeFiles) > 0:

            # We want to remove them from our list(dirs)
            dirs = TrimList(dirs, LargeFiles)

            print " "
            print "Size of above mentioned files is greater than the MailSizeLimit, we call them the LargeFiles.  \
Either increase the MailSizeLimit, or use some other filesharing service to send those oversize files. \
These LargeFiles will not be included in Email folders unless MailSizeLimit is raised to include those LargeFiles, \
or those LargeFiles are shifted out of current folder. \n"
            print " "
            Prompt = raw_input("What do you want to do now? If you want to create folders for all files except LargeFiles anyway, enter 'Y' \
or if you want to shift the LargeFiles first, enter 'N' and will relaunch again \
or else, if you want all your files to stay out in the folder like they are right now and Exit the program, enter E >>> ")

            if Prompt.lower() == "y":
                PrintSize(Path, dirs)
                Finallist = SeparateFiles(Path, dirs, MailSizeLimit)
                MakeFolders(Path, Finallist)
                MoveAllFiles(Finallist, Path)
                # Checking for leftover files here
                if len(dirs) != 0:
                    MoveRemainigFiles(Finallist, dirs, Path)
                    print " "
                    print "Check your folder. Email folders are created and file shifting done!"
                    print "Total size of all the Email folders is less than or equal to MailSizeLimiit you set earlier."
                    return AskToMoveBak(Path)
                else:
                    print " "
                    print "Check inside the Folder. Email folders are created and file shifting done!"
                    print "Total size of all the Email folders is less than or equal to MailSizeLimiit you set earlier."
                    return AskToMoveBak(Path)

            elif Prompt.lower() == "n":
                    print " "
                    print "Alright, shift the file first or increase the MailSizeLimit and we relaunch again."
                    print "\n"*5
                    return Launch()

            elif Prompt.lower() == "e":
                print " "
                print "Alright, we will exit now. All your files are now out in the folder"
                return Endit()

        # If there are no Large files found
        else:
            PrintSize(Path, dirs)
            Finallist = SeparateFiles(Path, dirs, MailSizeLimit )
            MakeFolders(Path, Finallist)
            MoveAllFiles(Finallist, Path)
            if len(dirs) != 0:
                MoveRemainigFiles(Finallist, dirs, Path)
                print " "
                print "Check inside the Folder. Email folders are created and file shifting done!"
                print "Total size of all the Email folders is less than or equal to MailSizeLimiit you set earlier."
                return AskToMoveBak(Path)
            else:
                print " "
                print "Check inside the Folder. Email folders are created and file shifting done!"
                print "Total size of all the Email folders is less than or equal to MailSizeLimiit you set earlier."
                return AskToMoveBak(Path)





def InitialMoveFiles(Path, SubPath, NameOfFolders):

    """ Checks all the directories and moves files in those
    direcctories to the main folder.
    Input(Path) = Location of Folder
    Input(SubPath) = Defined in Launch()
    Input(NameOfFolders) = Defined in this function"""

    # Generating list of folders in the SubPath
    NameOfFolders = CheckDir(SubPath)[0]
    for item in NameOfFolders:
        LocalPath = SubPath + '\\' + item

        # Making a list of files in the folder inside SubPath
        ListOfFiles = os.listdir(LocalPath)
        for file in ListOfFiles:
            src = LocalPath + '\\' + file
            dst = Path
            try:
                shutil.move(src, dst)
            except shutil.Error, WindowsError:
                os.remove(Path + '\\' + file)





def InitialCheckEmptyDir(SubPath, NameOfFolders):

    """ Checks if all the directories in the folder are empty.
    Input(SubPath) = Defined in Launch()
    Input(NameOfFolders) = Defined in this ReturnDirs"""
    
    for item in NameOfFolders:
        LocalPath = SubPath + '\\' + item

        # Making a list of files in the folder inside SubPath
        ListOfFiles = os.listdir(LocalPath)

        # If the list is empty, delete the folder
        if ListOfFiles == []:
            os.rmdir(LocalPath)  





def ReturnDirs(Path, SubPath, NameOfFolders):

    """If all directories are empty, returns dirs.
    Input(Path) = Location of Folder
    Input(SubPath) = Defined in Launch()
    Input(NameOfFolders) = Defined in this function"""
    
    while True:
        NameOfFolders = CheckDir(Path)[0]

        #Move all the files to the main folder
        InitialMoveFiles(Path, SubPath, NameOfFolders)
        
        # Delete all the folders
        InitialCheckEmptyDir(SubPath, NameOfFolders)

        # Check if there are still any folders left
        Check = CheckDir(Path)[0]

        # if no folders left, return the files list(dirs)
        if Check == []:
            return os.listdir(Path)
        
         # Update the folder list
        else:
            NameOfFolders = CheckDir(Path)[0]





def Endit():
    return False





def Launch():

    """
    Everything is Launched from here.

    """

    while True:
        
        print " "
        # Prerequisites for this code to work
        Announcement01 = """*** Hi There! Program is successfully launched *** \n."""
        Announcement02 = "*** This code has only been tested on Windows XP and Windows 7 *** \n"
        print Announcement01
        print Announcement02
        print " "

        # Path of folder where you want this process to happen
        Path = raw_input("Paste path of your folder here, \
or else if you want to exit, Enter E >>> ")

        # If user input is not valid, relaunch
        if CheckPath(Path) == False:
            print " "
            print "Hey, this is not a valid input. We will relaunch now."
            print "\n"*5
            return Launch()

        # If user input is valid, go on
        elif CheckPath(Path) == True:
            
            if Path.lower() == "e":
                break
            else:
                Path = StripPath(Path)
                print " "
    
                # Extracting name of all the folders present in the path selected
                NameOfFolders = CheckDir(Path)[0]

                # Cunting the number of folders in the path selected
                NumberOfFolders = CheckDir(Path)[1]

                if NameOfFolders != []:
                    PlaceHolder = []

                    # Creating a list of all the paths for subfolders
                    PathList = [x[0] for x in os.walk(Path)]

                    # Calling ReturnDirs function on all the Subpaths
                    for SubPath in PathList:
                        PlaceHolder = ReturnDirs(Path, SubPath, NameOfFolders)
                        
                    # Returns a list of all the files in this directory
                    dirs = PlaceHolder


                else:
                    # Returns a list of all the files in this directory
                    dirs = os.listdir(Path)

                    
                # Maximum size of email you want to shoot
                MailSizeLimit = raw_input("Mention maximum size limit for an email in MBs here. Try something in the range of 1 to 10 mbs. >>> ")
                MailSizeLimit = ReturnMailSize(MailSizeLimit)
                print " "                    
                
                # Return is inportant here. Otherwise False will not be received here
                return FileSizeScan(Path, dirs, MailSizeLimit)

                # Just to break out of the loop
                if FileSizeScan(Path, dirs, MailSizeLimit) == False:
                    break                    




Launch()









