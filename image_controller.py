from flask import Blueprint, request, send_from_directory
from flask import current_app as app
import image_handler
from authentication import token_required

image_con = Blueprint('image_con', __name__)


@image_con.route("/saveImage", methods=['POST'])
@token_required
def saveImage(user):
    try:
        user_id = user['upath']
        print(user_id)
        print(request.files)
        file = request.files['file_field']
        update_url = image_handler.save_image(user_id, file)
        return {"update_img_url": update_url}
    except Exception as e:
        print(e)
    return {"error": "Internal Error Occured"}


@image_con.route("/getAllData", methods=['GET'])
@token_required
def get_all_info(user):
    info = image_handler.get_all_folders_and_images(user["upath"])
    return info



@image_con.route("/getImageByFolder", methods=['GET'])
@token_required
def getImageByFolder(user):
    folder = request.args["folder"]
    info = image_handler.get_all_files_in_folder(user["upath"], folder)
    return info


@image_con.route('/send_image', methods=['GET'])
@token_required
def send_images(user):
    path = request.args["path"]
    upath = user["upath"]
    file_path, name = image_handler.get_full_path(upath, path) 
    print(file_path)
    print(name)
    return send_from_directory(file_path, name)