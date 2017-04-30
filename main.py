from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    '''Renders list of saved user stories. If we get here through POST method, it means that
    a new entry has been added. Generates a not yet existing ID for it and adds the new entry to loaded data.
    Saves data to file before rendering the list template. 
    '''
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
    write_to_file(data)
    return render_template('list.html', data=data)


@app.route("/<id>", methods=['GET', 'POST'])
def delete_or_update_entry(id):
    '''Function to delete or update an existing entry. GET method used by the trash-can icons in list.html view.
    POST method used by the form.html template, when updating existing entries. Writes changes to file, before rendering new list.html
    '''
    data = load_from_file()
    for i in range(len(data)):
        if data[i]['id'] == id:
            if request.method == 'GET':  # Deleting rows in list.html through the trash-can icon
                del data[i]
                break
            elif request.method == 'POST':  # Updating existing data in form.html
                data[i]['story_title'] = request.form['story_title']
                data[i]['user_story'] = request.form['user_story']
                data[i]['acceptance_criteria'] = request.form['acceptance_criteria']
                data[i]['business_value'] = request.form['business_value']
                data[i]['estimation'] = request.form['estimation']
                data[i]['status'] = request.form['status']
                break
    write_to_file(data)
    return render_template('list.html', data=data)


@app.route("/story/")
def empty_form():
    '''We get here by using the "Add new User Story" button in list.html. The function renders an empty form
    ready to be filled out.
    '''
    entry = []
    title = "Super Sprinter 3000 - Add new story"
    submit_caption = "Create"
    return render_template('form.html', entry=entry, title=title, submit_caption=submit_caption)


@app.route("/story/<id>")
def update_story(id=None):
    '''Looks up data for the entry to be edited and passes it to the form to populate the relevant fields
    with them.'''
    data = load_from_file()
    entry = []
    title = "Super Sprinter 3000 - Edit Story"
    submit_caption = "Update"
    for line in data:
        if line['id'] == id:
            entry = line
            break
    return render_template('form.html', entry=entry, title=title, submit_caption=submit_caption)


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
    return loaded_data


def write_to_file(data):
    '''Function to save data passed to it into csv file. Parameter data variable is expected
    to be a list of dictionaries, each dict is one entry.'''
    export_data = []
    for entry in data:
        export_data.append([entry['id'], entry['story_title'], entry['user_story'],
                           entry['acceptance_criteria'], entry['business_value'],
                           entry['estimation'], entry['status']])

    with open('sprint.csv', 'w', newline='\n') as csvfile:
        datawriter = csv.writer(csvfile, delimiter='|')
        for line in export_data:
            datawriter.writerow(line)

if __name__ == '__main__':
    app.run(debug=True)
