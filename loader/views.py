from flask import Blueprint, request, render_template, send_from_directory
import json

loader_blueprint = Blueprint('loader_blueprint', __name__)

@loader_blueprint.route('/post', methods=["POST","GET"])
def add_page():
    if request.method == "GET":
        return render_template('post_form.html')
    if request.method == "POST":
        task = request.form['content']
        picture = request.files.get("picture")
        filename = picture.filename
        picture.save(f"uploads/images/{filename}")
        a = {'pic':f'uploads/images/{filename}',
             'content': task}
        with open('posts.json', 'r', encoding='utf-8') as f:
            h = json.load(f)
            h.append(a)
        with open('posts.json', 'w', encoding='utf-8') as v:
            json.dump(h, v, indent=4, ensure_ascii=False) 
        return render_template('post_uploaded.html', a=a)
@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)