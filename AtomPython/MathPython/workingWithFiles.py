import os
# os.getcwd()
# os.chdir('C:\\Windows\System32)
# os.path.getsize(path) - size in bytes of path
# os.listdir(path) - will return a list of filename strings for each file in path
# os.path.exists(path) - will return True if a file or folder exists
# os.path.isdir(path) - returns true if path is a folder
# os.path.isfile(path) - returns true if pathe is a file
# shutil.copy(source, destination) - returns a string of the pathe of the copied file
# shutil.copytree(source, destination) - returns a string of the pati of the copied folder
# shutil.move(source, destination) - returns the path of the new location, can rename as well
# os.unlink(path) - deletes the file at path
# os.rmdir(path) - deletes the folder at path, must be empty folder
# shutil.rmtree(path) - deletes folder and files at path
# import send2trash - send2trash.send2trash() to send items to recycle bin

for folderName, subfolders, filenames in os.walk('C:\\MyDocuments'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)

        print('')

# import zipfile
# zipfile.ZipFile(file) - returns a file object of the zip file at file
# zipfile.namelist() - returns a list of strings for all the files and folders in the ZIP file
# zipfile.getinfo(file) - attributes of the file in zipfile object
# zipfile.extractall(path - extracts all the files and folders from a ZIP file to path or the current working directory if path is blank
# zipfile.close()
# zipfile.extract(file,destination) - extract a single file to the destination, returns the absolute path to which file was extracted
import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
# use 'a' in second parameter to append ot existing ZIP file
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
