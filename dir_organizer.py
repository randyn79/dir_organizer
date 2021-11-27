#! /usr/bin/env python3
import os

def dir_organizer():
    """Loops through each file in the current working directory,
and based on file extension moves them to a Documents, Images or
Text folder inside the current working directory. Ignores files
with undefined extensions.  Skips files if the file already exists
in the destination directory."""
    
    cwd = os.getcwd()
    
    # Add additional file extensions here if needed.
    document_ext = ('.doc', '.docx', '.pdf', '.odt', '.xls', '.xlsx')
    images_ext = ('.jpg', '.jpeg', '.tif', '.tiff', '.gif', '.bmp')
    text_ext = ('.txt', '.csv')
    

    # Set destination directory paths.
    documents_path = os.path.join(cwd, 'Documents')
    images_path = os.path.join(cwd, 'Images')
    text_path = os.path.join(cwd, 'Text')
    
    # Check to see if the destination directory paths, if not create them.
    if not os.path.isdir(documents_path):
        os.mkdir(documents_path)

    if not os.path.isdir(images_path):
        os.mkdir(images_path)

    if not os.path.isdir(text_path):
        os.mkdir(text_path)

    # Loop through files to determine file extension and move them to
    # the appropriate directory if a match is found.
    for file in os.listdir(cwd):
        source_path = os.path.join(cwd,file)
        
        if file.endswith(document_ext):
            destination_path = os.path.join(documents_path, file)
            if file not in os.listdir(documents_path):
                os.replace(source_path, destination_path)

        if file.endswith(images_ext):
            destination_path = os.path.join(images_path, file)
            if file not in os.listdir(images_path):
                os.replace(source_path, destination_path)

        if file.endswith(text_ext):
            destination_path = os.path.join(text_path, file)
            if file not in os.listdir(text_path):
                os.replace(source_path, destination_path)

        
        
    

dir_organizer()
