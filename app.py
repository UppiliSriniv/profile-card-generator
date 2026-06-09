from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    role = request.form['role']
    bio = request.form['bio']
    skills = request.form['skills']
    image = request.form['image']

    return render_template(
        'index.html',
        generated=True,
        name=name,
        role=role,
        bio=bio,
        skills=skills,
        image=image
    )

if __name__ == '__main__':
    app.run(debug=True)