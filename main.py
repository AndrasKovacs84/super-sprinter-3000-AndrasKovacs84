from flask import Flask, render_template, request
import csv
import pprint
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    data = load_from_file()
    if request.method == 'POST':
        new_id = 1
        existing_ids = []
        for i in range(len(data)):
            existing_ids.append(int(data[i]['id']))
        while new_id in existing_ids:
            new_id += 1
        data.append({'id': new_id,
                     'story_title': request.form['story_title'],
                     'user_story': request.form['user_story'],
                     'acceptance_criteria': request.form['acceptance_criteria'],
                     'business_value': request.form['business_value'],
                     'estimation': request.form['estimation'],
                     'status': request.form['status']})
    return render_template('list.html', data=data)


@app.route("/story/")
def empty_form():
    entry = []
    return render_template('form.html', entry=entry)


@app.route("/story/<id>")
def update_story(id=None):
    data = load_from_file()
    entry = []
    for line in data:
        if line['id'] == id:
            entry = line
    # entry = data[int(id)]
    return render_template('form.html', entry=entry)


def load_from_file():
    '''Function to open and process the csv file which contains saved data. Returns a list
    of nested dictionaries of each entry
    '''
    line_of_data = []
    loaded_data = []
    with open('sprint.csv', newline='\n') as csvfile:
        file_content = csv.reader(csvfile, delimiter='|')
        for row in file_content:
            loaded_data.append({'id': row[0],
                                'story_title': row[1],
                                'user_story': row[2],
                                'acceptance_criteria': row[3],
                                'business_value': row[4],
                                'estimation': row[5],
                                'status': row[6]})
        # pprint.pprint(loaded_data)
    return loaded_data


if __name__ == '__main__':
    # load_from_file()
    # new_story(id=1)
    app.run(debug=True)