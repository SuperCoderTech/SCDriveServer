from image_handler import UPLOAD_FOLDER
import os
import logging

logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


def create_folder(basepath, folderpath, foldername):
    my_folder = os.path.join(UPLOAD_FOLDER, basepath, folderpath, foldername)
    logging.info("directory to make path ::"+my_folder)
    os.mkdir(my_folder)
