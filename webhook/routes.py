from webhook import app
import json


@app.route('/idea/<int:idea_id>', methods=['GET'])
def get_idea(idea_id):
    return json.dumps({
        'id': idea_id
    }), 200
