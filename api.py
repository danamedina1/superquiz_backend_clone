from flask import Flask, request, jsonify
import superquiz_app
import os

print("Starting API server...")
app = Flask(__name__)

# Check if the app is running on Vercel or locally
if 'VERCEL_URL' in os.environ:
    # If running on Vercel, use the Vercel configuration
    app.config['BASE_URL'] = 'https://superquiz-v1-backend-fjicox52e-danamthriveprojectearth-gmailcom.vercel.app'
else:
    # If running locally, use the local configuration
    app.config['BASE_URL'] = '__name__'
def string_to_list(string):
    #trim the brackets and split the string into an array:
    array = [element.strip() for element in string.strip('[').strip(']').split(',')]
    #strip the whitespace from each element in the array:
    # array = [element.strip() for element in array]
    return array
@app.route('/generate_mcq', methods=['POST'])
def generate_mcq():
    data = request.json
    url = data.get('url')
    number_of_questions = data.get('number_of_questions', 10)

    # Input validation
    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    # Call generate_mcq_list function:
    mcq_list = superquiz_app.generate_mcq_list(url, number_of_questions)

    # Convert MCQuestion objects to dictionaries
    serializable_mcq_list = []
    for mcq in mcq_list:
        mcq_dict = mcq.to_dict()
        serializable_mcq_list.append(mcq_dict)

   # return as a json with status code 200 for successful response:
    return jsonify(serializable_mcq_list), 200

@app.route('/read', methods=['GET'])
def get_mcq_list():
    id = request.args.get('id')
    url = request.args.get('url')
    tags = request.args.get('tags[]')
    approved = request.args.get('approved')

    # Convert arrays from string to list:
    tags = string_to_list(tags) if tags else None

    # Call read function:
    mcq_list = superquiz_app.read(id, url, tags, approved)

    # Check if the result is None, indicating an error occurred
    if mcq_list is None:
        return jsonify({"message": "Error: MCQ not found"}), 404  # Not Found

    # Convert MCQuestion objects to dictionaries
    serializable_mcq_list = []
    for mcq in mcq_list:
        mcq_dict = mcq.to_dict()
        serializable_mcq_list.append(mcq_dict)

    # return as a json with status code 200 for successful response:
    return jsonify(serializable_mcq_list), 200

@app.route('/update', methods=['PUT'])
def update_mcq():
    data = request.json
    id = data.get('id')
    updated_question = data.get('updated_question')
    updated_answers = data.get('updated_answers[]')
    updated_correct_answer = data.get('updated_correct_answer')
    updated_quote = data.get('updated_quote')
    updated_url = data.get('updated_url')
    updated_tags = data.get('updated_tags[]')
    updated_date = data.get('updated_date')
    updated_type = data.get('updated_type')
    updated_approved = data.get('updated_approved')
    updated_approved_by = data.get('updated_approved_by')


    # Convert arrays from string to list:
    updated_answers = string_to_list(updated_answers) if updated_answers else None
    updated_tags = string_to_list(updated_tags) if updated_tags else None

    # Call update function:
    result,msg = superquiz_app.update(id=id, updated_question=updated_question, updated_answers=updated_answers,
                                      updated_correct_answer=updated_correct_answer, updated_quote=updated_quote,
                                      updated_url=updated_url, updated_tags=updated_tags, updated_date=updated_date,
                                      updated_type=updated_type, updated_approved=updated_approved,
                                      updated_approved_by=updated_approved_by)

    if result is not None:
        return jsonify({"result": result, "message": msg}), 200
    else:
        return jsonify({"message": msg}), 500

@app.route('/delete', methods=['DELETE'])
def delete_mcq():
    id = request.args.get('id')
    # Call delete function:
    result, msg = superquiz_app.delete(id)

    # Check if the deletion was successful or not
    if result != 1:
        return jsonify({"message": msg}), 404  # Not Found
    else:
        # return as a json with status code 204 for successful deletion:
        return jsonify({"message": msg}), 204

if __name__ == '__main__':
    app.run(debug=True)

