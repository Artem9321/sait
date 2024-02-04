from flask import Blueprint, render_template, request
import json

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/')
def a():
    return render_template('index.html')

@main_blueprint.route('/search')
def filter_page():
    from_value = request.args.get('s')
    with open('posts.json', 'r', encoding='utf-8') as f:
        a = []
        d = json.load(f)
        for i in d:
            if from_value in i['content']:
                a.append(i)
        return render_template('post_list.html', a=a, from_value=from_value)