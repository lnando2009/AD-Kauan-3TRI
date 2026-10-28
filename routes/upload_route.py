from flask import Blueprint
from controllers.upload_controller import UploadsControllers

upload_bp = Blueprint('uplead_bp', __name__)

@upload_bp.route('/upload', methods=['POST'])
def uploads_file():
    return UploadsControllers.uploads_file()
