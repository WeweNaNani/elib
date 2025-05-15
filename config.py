from flask import Flask, render_template, request
import sqlite3
import internetarchive
import requests

app = Flask(__name__)

def get_book_info(ia_id):
    try:
        item = internetarchive.get_item(ia_id)
        metadata = item.metadata
        downloadable_files = []
        for file in metadata.get("files", []):
            if file.get('name'):
                file_format = file['name'].split('.')[-1]
                download_link = f"https://archive.org/download/{ia_id}/{file['name']}"
                downloadable_files.append({
                    "format": file_format,
                    "url": download_link
                })
        preview_link = f"https://archive.org/details/{ia_id}/mode/1up"
        return downloadable_files, preview_link
    except Exception as e:
        print(f"Error fetching book info: {e}")
        return None, None

def init_db():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        author TEXT,
        isbn TEXT UNIQUE,
        olid TEXT UNIQUE,
        publish_year INTEGER,
        language TEXT,
        cover_id TEXT,
        genres TEXT,
        preview TEXT,
        description TEXT,
        subjects TEXT,
        pages INTEGER,
        publishers TEXT
    )''')
    conn.commit()
    conn.close()

def search_and_store_books(query):
    init_db()
    conn = sqlite3.connect('books.db', check_same_thread=False)
    c = conn.cursor()
    response = requests.get(f"https://openlibrary.org/search.json?q={query.replace(' ', '+')}")
    data = response.json()
    books = []

    for doc in data['docs'][:10]:
        title = doc.get('title', 'Unknown')
        author = ', '.join(doc.get('author_name', [])) if doc.get('author_name') else 'Unknown'
        isbn = doc.get('isbn', [None])[0]
        olid = doc.get('edition_key', [None])[0]
        publish_year = doc.get('first_publish_year', None)
        language = ', '.join(doc.get('language', [])) if doc.get('language') else None
        ia = doc.get('ia', [None])[0]
        cover_id = doc.get('cover_i', None)
        genres = ', '.join(doc.get('subject', [])) if doc.get('subject') else None
        preview = doc.get('first_sentence') or doc.get('subtitle') or None
        if isinstance(preview, dict):
            preview = preview.get('value')

        downloadable_files, preview_link = get_book_info(ia)

        book_data = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'olid': olid,
            'publish_year': publish_year,
            'language': language,
            'cover_id': cover_id,
            'genres': genres,
            'preview': preview,
            'description': None,
            'subjects': None,
            'pages': None,
            'publishers': None,
            'downloadable_files': downloadable_files,
            'preview_link': preview_link
        }

        books.append(book_data)

    conn.commit()
    conn.close()
    return books

@app.route('/', methods=['GET', 'POST'])
def index():
    books = []
    if request.method == 'POST':
        query = request.form['query']
        books = search_and_store_books(query)
    return render_template('index.html', books=books)

@app.route('/buy/<olid>')
def buy(olid):
    return f"""
    <h2>Thanks for your interest!</h2>
    <p>Download access for <strong>{olid}</strong> will be available after purchase.</p>
    <a href="/">Go back to search</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
