Accessing Form Data with flask.request.form
[File: server.py, Line: 10-22] | [File: index.html]
    You can use flask.request.form to access form data that a user has submitted via a POST request. For instance, this feature can be used if you have a login form with username and password fields.

Redirecting to a URL with flask.redirect
[File: server.py, Line: 29-33]
    Flask provides a function called flask.redirect to guide users to a different webpages (or endpoints). The flask.redirect function can be useful in several scenarios. For example, you can use the flask.redirect function to redirect a user to a login page when they try to access a restricted admin page.

Generating Dynamic URLs with flask.url_for
[File: server.py, Line: 36-43]
    The flask.url_for function dynamically generates URLs for a given endpoint. Dynamically generating URLs can be particularly useful when the URL for a route is altered. The flask.url_for function automatically updates the URL throughout your templates or code, minimizing manual work. For example, consider the scenario where a user is trying to access the admin page and must be redirected to the login page. In this scenario, url_for('login') will retrieve the URL for the login page from the existing routes.


CURD
[File: crud.py] | [Files: create.html, update.html, delete.html]
    Create, Read, Update, and Delete (CRUD) are basic functions that any application with a database must perform. To effectively implement the CRUD operations, you will need to manage different HTTP methods, such as GET and POST requests. A GET request is generally used to retrieve or read data and is often used to display a form. A POST request is commonly used to send data to create or update data. An example of a POST request is form submission.