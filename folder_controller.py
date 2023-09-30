from flask import Blueprint, request, send_from_directory
from flask import current_app as app
import image_handler
from authentication import token_required
import folder_manager as fm

folder_con = Blueprint('folder_con', __name__)


@folder_con.route("/create_folder", methods=['GET'])
@token_required
def create_folder(user):
    basepath = user["upath"]
    folder = request.args["folder"]
    print(folder)
    name = request.args["name"]
    print(name)
    fm.create_folder(basepath, folder, name)
    return {'status': 'success'}

    
