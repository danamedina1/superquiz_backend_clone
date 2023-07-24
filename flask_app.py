from flask import Flask, request, jsonify
from api import generate_mcq_list, read, update, delete
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)################# DEBUGGING ######################

@app.route('/generate_mcq', methods=['POST'])
def generate_mcq():
    data = request.json
    url = data.get('url')
    number_of_questions = data.get('number_of_questions', 10)

    # Call generate_mcq_list function:
    mcq_list = generate_mcq_list(url, number_of_questions)

    # Convert MCQuestion objects to dictionaries
    serializable_mcq_list = []
    for mcq in mcq_list:
        mcq_dict = mcq.to_dict()
        serializable_mcq_list.append(mcq_dict)

    # return as a json:
    return jsonify(serializable_mcq_list)

@app.route('/read', methods=['GET'])
def get_mcq_list():
    id = request.args.get('id')
    url = request.args.get('url')
    tags = request.args.get('tags')
    # Call read function:
    mcq_list, result = read(id, url, tags)

    # Convert MCQuestion objects to dictionaries
    serializable_mcq_list = []
    for mcq in mcq_list:
        mcq_dict = mcq.to_dict()
        serializable_mcq_list.append(mcq_dict)

    # return as a json:
    return jsonify(serializable_mcq_list)


@app.route('/update', methods=['PUT'])
def update_mcq():
    data = request.args
    id = data.get('id')
    updated_mcq = data.get('updated_mcq')
    updated_question = data.get('updated_question')
    updated_answers = data.get('updated_answers')
    updated_correct_answer = data.get('updated_correct_answer')
    updated_quote = data.get('updated_quote')
    updated_url = data.get('updated_url')
    updated_tags = data.get('updated_tags')
    updated_date = data.get('updated_date')
    updated_type = data.get('updated_type')

    app.logger.debug(f"\nupdated_correct_answer: {updated_correct_answer}")  ################# DEBUGGING ######################
    app.logger.debug(f"\nupdated_tags: {updated_tags}")  ################# DEBUGGING ######################

    # Call update function:
    result,msg = update(id=id, updated_mcq=updated_mcq, updated_question=updated_question, updated_answers=updated_answers, updated_correct_answer=updated_correct_answer, updated_quote=updated_quote, updated_url=updated_url, updated_tags=updated_tags, updated_date=updated_date, updated_type=updated_type)
    if result is not None:
        return jsonify({"result": result, "message": msg}), 200
    else:
        return jsonify({"message": msg}), 500

@app.route('/delete', methods=['DELETE'])
def delete_mcq():
    id = request.args.get('id')
    # Call delete function:
    delete(id)
    return jsonify({'message': 'MCQ deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

