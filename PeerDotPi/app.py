from flask import Flask, render_template, request
from search import search_for_letters

app = Flask(__name__)

@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))
    title = 'Here are your results:'
    return render_template ('results.html', the_phrase=phrase, the_letters=letters, the_results=results, the_title=title)

@app.route('/')
@app.route('/entry')
def entry():
    return render_template('entry.html', the_title='Welcome to Search4Letters on the web!')

if __name__ == "__main__":
    app.run(debug=True)