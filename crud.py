from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
data = []
id_counter = 0

@app.route('/')
def home():
    return "Welcome to the homepage"

# Create operation
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        record = create_new_record(name)
        return redirect(url_for('read', id=record['id']))
    return render_template('create.html')


def create_new_record(name):
    global id_counter
    id_counter += 1
    record = {'id': id_counter, 'name': name}
    data.append(record)
    return record

# Read opeartion
@app.route('/read/<int:id>', methods=['GET'])
def read(id):
    record = get_record(id)
    if record:
        return f"Record ID: {record['id']}, Name: {record['name']}"
    return "Record not found"


def get_record(record_id):
    for record in data:
        if record['id'] == record_id:
            return record
    return None

# Update operation
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    record = get_record(id)
    if not record:
        return "Record not found"
    
    if request.method == 'POST':
        name = request.form['name']
        update_record(id, name)
        return redirect(url_for('read', id=id))
    
    return render_template('update.html', record=record)


def update_record(record_id, record_name):
    for record in data:
        if record['id'] == record_id:
            record['name'] = record_name
            return

# Delete operation
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    delete_record(id)
    return redirect(url_for('home'))


def delete_record(record_id):
    global data
    for record in data:
        if record['id'] == record_id:
            data.remove(record)
            return

# error handler
@app.errorhandler(404)
def not_found(error):
    return {"message": "Mention ID in the URL / invalid URL"}, 404
