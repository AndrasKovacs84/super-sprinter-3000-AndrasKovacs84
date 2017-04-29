# super-sprinter-3000-AndrasKovacs84
Story
Write an app to store your team's Agile development process through sprints and represent it to your client.

Requirements
The web application should consist of 3 pages:

Adding page [/story]

Empty form (there is no data in the inputs) with a "Create" button. It should create a new User Story.super sprinter - add story-1.png
 

Editor page [/story/<story_id>]

The same form as the create page, but filled in with data of the given User Story.
The "Update" button should update an existing entry, not create a new entry.
super sprinter - update-1.png

 

List page [/ and /list]

It should have a HTML table containing all the data.
In the end of every row, you should add a pen and a bin icon. Both should be links, the pen should redirect to the editing page of the given row and the bin icon should perform a DELETE on the given row.
Add an "Add a new User Story" button to the page. It should redirect to the (Creating) /story page.
User Story webapp - list.png

Persistence

The application should persist data using a .CSV file.

Other requirements

You should create 2 templates (Links to an external site.)Links to an external site.: form.html and list.html
All the 3 pages should have a different title (use HTML title tag):
Super Sprinter 3000 (for the list page)
Super Sprinter 3000 - Add new Story (for the /story page)
Super Sprinter 3000 - Edit Story (for the /story/<story_id> page)
The input boxes should have some rules, you can find them in the wireframe images above
The labels of for the form inputs should be label tags connected to the specific field.
All input fields and buttons should have a specific id attribute.
The Create/Update button should submit the form to your server via a HTTP request. Use the right HTTP request to perform the operations!
You don't have to use CSS!

Submission
Create a repository for this project, named "super-sprinter-3000-annakonda", where annakonda is your GitHub username.

Submit the Github HTTPS link to this repository!