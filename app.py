#!/usr/bin/env python3
import os

from flask import Flask, render_template

app = Flask(__name__)

PUBLIC_PAGES = [
    {"path": "/", "name": "Home"},
    {"path": "/catalog", "name": "Catalog"},
    {"path": "/support", "name": "Support"},
]


@app.route("/")
def index():
    return render_template("index.html", pages=PUBLIC_PAGES)


@app.route("/catalog")
def catalog():
    return render_template("page.html", title="Catalog", message="No products are currently listed.")


@app.route("/support")
def support():
    return render_template("page.html", title="Support", message="Support desk is currently offline.")


@app.route("/admin")
def admin_panel():
    return (
        "Exposed Admin Panel\n"
        "Status: public endpoint discovered\n"
        "Secret: LAB-012-FFUF"
    )


if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5012"))
    print(f"Open http://{host}:{port}")
    app.run(host=host, port=port, debug=False)
