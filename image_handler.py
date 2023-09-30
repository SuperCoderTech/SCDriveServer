import os
import shutil
from PIL import Image
import logging
logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

UPLOAD_FOLDER = '/home/dietpi/Mine'
TRASH_FOLDER = '/home/dietpi/.Trash/'


def set_upload_folder(folder):
    global UPLOAD_FOLDER
    UPLOAD_FOLDER = folder


def save_image(base_folder, file):
    try:
        path = os.path.join(UPLOAD_FOLDER, base_folder)
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
        path_to_update = os.path.join(base_folder, file.filename)
        path = os.path.join(path, file.filename)
        file.save(path)
        logging.info(path)
        return path_to_update
    except Exception as e:
        logging.error(e)
    return None


def get_all_images(upath):
    resp = []
    my_folder = os.path.join(UPLOAD_FOLDER, upath)
    for root, dirs, files in os.walk(my_folder):
        for file in files:
            resp.append(os.path.join(root, file))
    return resp


def get_all_folders_and_images(upath):
    resp = []
    print(UPLOAD_FOLDER)
    my_folder = os.path.join(UPLOAD_FOLDER, upath)
    for root, dirs, files in os.walk(my_folder):
        for dirc in dirs:
            resp.append({"path": os.path.join(
                root[len(my_folder):], dirc), "type": "directory"})
            logging.info(os.path.join(root, dirc))
        for file in files:
            if file.lower().endswith(".jpg") or file.lower().endswith(".png"):
                resp.append({"path": os.path.join(
                    root[len(my_folder):], file), "type": "image"})
            else:
                resp.append({"path": os.path.join(
                    root[len(my_folder):], file), "type": "file"})
            logging.info(os.path.join(root, file))

    return resp


def get_all_files_in_folder(upath, path):
    print(UPLOAD_FOLDER)
    my_folder = os.path.join(UPLOAD_FOLDER, upath)
    if path is not None:
        my_folder = os.path.join(my_folder, path)
    dir_list = os.listdir(my_folder)
    resp = []
    for f in dir_list:
        if ".thumbnail" in f:
            continue
        if os.path.isfile(my_folder+'/'+f):
            if f.lower().endswith(".jpg") or f.lower().endswith(".png"):
                resp.append({"name": f, "type": "image"})
        else:
            resp.append({"name": f, "type": "directory"})
    return resp


def get_full_path(upath, path):
    my_folder = os.path.join(UPLOAD_FOLDER, upath)
    file_path = os.path.join(my_folder, path)
    logging.info(file_path)
    file_path = file_path.replace(' ', '\\ ')
    file = file_path.rsplit("/", 1)
    return file[0], file[1]


def remove_file(upath, path):
    my_folder = os.path.join(UPLOAD_FOLDER, upath)
    file_path = os.path.join(my_folder, path)
    logging.info(file_path)
    file_path = file_path.replace(' ', '\\ ')
    print("remove file "+file_path)
    file = file_path.rsplit("/", 1)
    thumbnail = file[0] + "/.thumbnail/" + file[1]
    print("remove thumbnail file "+thumbnail)
    os.remove(thumbnail)
    shutil.move(file_path, TRASH_FOLDER)
    return "removed"


def save_image(upath, path, file):
    try:
        print(file.filename)
        path = os.path.join(UPLOAD_FOLDER, upath, path)
        print(path)
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
        path = os.path.join(path, file.filename)
        file.save(path)
        print(path)
        return path
    except Exception as e:
        print(e)
    return None


if __name__ == "__main__":
    get_all_folders_and_images("MRB")
