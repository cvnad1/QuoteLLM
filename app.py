from flask import Flask, render_template, request
import cohere

app = Flask(__name__)

co = cohere.Client("API_KEY_HERE")

@app.route('/', methods=['GET', 'POST'])
def page():
    is_output = False
    outputtext = ""
    if request.method == "POST":
        is_output = True
        outputtext = request.form['inputtext']
        response = co.generate(prompt=outputtext, model='b6dde340-864b-4a01-bd76-b66cb6de2fad-ft', max_tokens=300, temperature=0.75, p=0.5)
        outputtext = response.generations[0].text
    return render_template('index.html', output=outputtext, is_output=is_output)


if __name__ == '__main__':
    app.run(debug=True)