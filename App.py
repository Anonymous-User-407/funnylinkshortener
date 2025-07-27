from flask import Flask, redirect, render_template, request
import random
import time

app = Flask(__name__)

# Simulating a link shortening database (you'd usually use a real database)
links_db = {
    'abcd1234': 'https://www.example.com',  # Example shortened link
    'xyz9876': 'https://www.anotherexample.com'
}

# Simple route for shortening links (for testing)
@app.route('/shorten', methods=['GET', 'POST'])
def shorten():
    if request.method == 'POST':
        long_url = request.form['long_url']
        # Simulating link shortening (in reality, you'd hash it or use a DB)
        short_code = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
        links_db[short_code] = long_url
        return f'Your shortened link is: <a href="/redirect/{short_code}">/{short_code}</a>'
    return render_template('shorten.html')

# Interstitial page before redirect
@app.route('/redirect/<short_code>')
def redirect_to_link(short_code):
    if short_code not in links_db:
        return 'Link not found!', 404
    
    long_url = links_db[short_code]
    return render_template('interstitial.html', long_url=long_url)

# Redirect the user after the delay
@app.route('/proceed/<short_code>')
def proceed(short_code):
    if short_code not in links_db:
        return 'Link not found!', 404
    
    long_url = links_db[short_code]
    return redirect(long_url)

if __name__ == '__main__':
    app.run(debug=True)