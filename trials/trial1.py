import os

def find_html_file():
    files = [f for f in os.listdir(os.getcwd()) if f.endswith(".html")]
    
    if not files:
        raise FileNotFoundError("No HTML file found in project root.")

    if "index.html" in files:
        return "index.html"

    return files[0]
