from flask import Flask,jsonify,request
app = Flask(__name__)
tasks = [
    {
        'ID':1,
        'Title':'Get ready for golf practice',
        'Description':'Started at 9:00AM at a golf field',
        'Done':'True'
    },
    {
        'ID':2,
        'Title':'Eat lunch',
        'Description':'Ate lunch at home after golf practice',
        'Done':'True'
    }
]

@app.route('/displayname')
def displayname():
    return 'Yena'

@app.route('/displayschool')
def displayshcool():
    return 'LPP'

@app.route('/addtask',methods=['POST'])
def addtask():
    if not request.json:
        return jsonify({
            'Status':'Error',
            'Message':'Please enter details to add a new task'
        })
    t = {
        'ID':tasks[-1]['ID']+1,
        'Title':request.json['Title'],
        'Description':request.json['Description'],
        'Done':request.json['Done']
    }
    tasks.append(t)
    return jsonify({
        'Status' : 'Success',
        'Message' : 'The task has been successfully added'
    })

@app.route('/gettasks')
def gettasks():
    return jsonify({
        'data':tasks
    })

if(__name__ == '__main__'):
    app.run(debug=True)