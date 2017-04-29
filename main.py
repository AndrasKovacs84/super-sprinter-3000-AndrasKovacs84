from flask import Flask, render_template, request
import csv
import pprint
app = Flask(__name__)


@app.route("/")
def index():
    data = load_from_file()
    return render_template('list.html', data=data)


@app.route("/story")
def new_story():
    pass


def load_from_file():
    '''Function to open and process the csv file which contains saved data. Returns a list
    of nested dictionaries of each entry
    '''
    line_of_data = []
    loaded_data = []
    '''
    entry_dict = {'ID': '',
                  'Story title': '',
                  'User story': '',
                  'Acceptance criteria': '',
                  'Business value': 0,
                  'Estimation': 0.0,
                  'Status': '',
                  }'''
    with open('sprint.csv', newline='\n') as csvfile:
        file_content = csv.reader(csvfile, delimiter='|')
        for row in file_content:
            '''entry_dict['ID'] = row[0]
            entry_dict['Story title'] = row[1]
            entry_dict['User story'] = row[2]
            entry_dict['Acceptance criteria'] = row[3]
            entry_dict['Business value'] = row[4]
            entry_dict['Estimation'] = row[5]
            entry_dict['Status'] = row[6]'''
            loaded_data.append(row)
        # pprint.pprint(loaded_data)
    return loaded_data


if __name__ == '__main__':
    app.run()