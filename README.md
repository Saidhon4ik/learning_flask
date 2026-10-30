# Learning Flask

A small learning project for practicing Flask fundamentals, server-rendered HTML, and Jinja templates. The project is being built step by step as a foundation for a future data-focused web application.

## Tech stack

- Python 3.13+
- Flask
- `uv` for Python project and dependency management
- HTML templates rendered with Jinja

## Run locally

1. Clone the repository and open its folder in PowerShell.
2. Install the project dependencies:

   ```powershell
   uv sync
   ```

3. Start the development server:

   ```powershell
   uv run python main.py
   ```

4. Open `http://127.0.0.1:5000/` in a browser.

The app currently runs with Flask debug mode enabled for local development.

## Pages and routes

| URL | What it demonstrates |
|---|---|
| `/` | Renders the home page from `templates/home.html` |
| `/about` | Passes hobby and city values from Python into a template |
| `/hello/<name>` | Reads a text parameter from the URL |
| `/square/<int:n>` | Accepts an integer URL parameter and returns its square |
| `/books` | Passes a Python list to a template and renders it as a table |

## What this project practices

- Creating a Flask app and connecting routes to Python view functions.
- Returning simple responses and using URL parameters.
- Keeping HTML in the `templates/` folder and rendering it with `render_template`.
- Passing values and lists from Python to Jinja templates.
- Using Jinja output (`{{ ... }}`) and loops (`{% for ... %}`) to build HTML from data.
- Adding navigation links between pages.
- Creating a basic search form with a label, input, and submit button. The form currently submits to `/books`, but filtering is not implemented yet.
- Using Git to commit project milestones and publish them to GitHub.

## Project structure

```text
learning-flask/
├── main.py
├── templates/
│   ├── about.html
│   ├── books.html
│   └── home.html
├── pyproject.toml
├── uv.lock
└── README.md
```

## Learning roadmap

Next steps include reading form values in Flask, filtering the book list, and then learning how to connect a Flask app to PostgreSQL. Deployment (including Render) will be explored later, after the app is ready.
