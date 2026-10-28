from flask import jsonify, send_from_directory

UPLOAD_FOLDER = 'uploads'

class DownloadController:

    @staticmethod
    def dowload_file(filename):
        try:
            return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
            except FileNotFoundError:
                return jsonify({"error": "Arquivo não encontrado"}), 400