from PIL import Image
import os
import image_handler

THUMBNAIL = ".thumbnail"


def create_thumbnail(path, file):
    if not os.path.exists(os.path.join(path, THUMBNAIL)):
        os.makedirs(os.path.join(path, THUMBNAIL))
    if (os.path.exists(os.path.join(path, THUMBNAIL, file))):
        print(file + " already exists ")
        return
    image = Image.open(os.path.join(path, file))
    MAX_SIZE = (533, 300)
    image.thumbnail(MAX_SIZE)
    # creating thumbnail
    image.save(os.path.join(path, THUMBNAIL, file))
    print(file + " thumnail created ")


def create_thumbnail_for_all():
    images = image_handler.get_all_images("MRB")
    print(len(images))
    for i in images:
        try:
            print(i)
            file = i.rsplit("/", 1)
            if file[0].endswith(THUMBNAIL):
                continue
            create_thumbnail(file[0], file[1])
        except Exception as e:
            print(e)


if __name__ == "__main__":
    create_thumbnail_for_all()
