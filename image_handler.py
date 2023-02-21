import os
from PIL import Image

UPLOAD_FOLDER = '/home/dietpi/Mine'


def save_image(base_folder, file):
    try:
        path = os.path.join(UPLOAD_FOLDER, base_folder)
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
        path_to_update = os.path.join(base_folder, file.filename)
        path = os.path.join(path, file.filename)
        file.save(path)
        print(path)
        return path_to_update
    except Exception as e:
        print(e)
    return None


def tnails():
    try:
        image = Image.open('images/cat.jpg')
        image.thumbnail((90, 90))
        image.save('images/thumbnail.jpg')
        image1 = Image.open('images/thumbnail.jpg')
        image1.show()
    except IOError:
        pass


def get_all_folders_and_images(upath):
    resp = []
    my_folder = os.path.join(UPLOAD_FOLDER, upath)
    for root, dirs, files in os.walk(my_folder):
        for dirc in dirs:
            resp.append({"path": os.path.join(
                root[len(my_folder):], dirc), "type": "directory"})
            print(os.path.join(root, dirc))
        for file in files:
            resp.append({"path": os.path.join(
                root[len(my_folder):], file), "type": "file"})
            print(os.path.join(root, file))

    return resp


def get_all_files_in_folder(upath, path):
    my_folder = os.path.join(UPLOAD_FOLDER, upath)
    if path is not None:
        my_folder = os.path.join(my_folder, path)
    dir_list = os.listdir(my_folder)
    resp = []
    for f in dir_list:
        if os.path.isfile(my_folder+'/'+f):
            resp.append({"name": f, "type": "file"})
        else:
            resp.append({"name": f, "type": "directory"})
    return resp


def get_full_path(upath, path):
    my_folder = os.path.join(UPLOAD_FOLDER, upath)
    file_path = os.path.join(my_folder, path)
    print(file_path)
    file_path = file_path.replace(' ', '\\ ')
    file = file_path.rsplit("/", 1)
    return file[0], file[1]


if __name__ == "__main__":
    get_all_folders_and_images("MRB")
