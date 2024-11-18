from flask import Flask, send_from_directory, redirect, session
from pathlib import Path
import secrets

app = Flask(__name__, static_folder='website', static_url_path='/static')
app.secret_key = secrets.token_urlsafe(64)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = True

@app.route('/')
def server_html():
    session['last_page'] = '/'
    return send_from_directory('website', 'index.html')

@app.route('/<url>')
def custom_url(url):
    file = f'website/{url}'
    if not file.endswith('.html'):
        return redirect(session.get('last_page', '/'))
    file = Path(file)
    if not file.is_file():
        return redirect(session.get('last_page', '/'))
    session['last_page'] = f'/{url}'
    return send_from_directory('website', url)

if __name__ == '__main__':
    app.run('0.0.0.0', port=80)
