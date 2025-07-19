from flask import Flask, render_template

app = Flask(__name__)

news_data = {
    "sports": [
        {"title": "India Wins Cricket Final", "summary": "India clinched the title after a thrilling match."},
        {"title": "Olympics 2024 Highlights", "summary": "India bags 10 medals in athletics."}
    ],
    "technology": [
        {"title": "New AI Tool Launched", "summary": "A revolutionary AI tool is changing industries."},
        {"title": "Quantum Computing Breakthrough", "summary": "Researchers achieve stable qubit states."}
    ],
    "health": [
        {"title": "New Vaccine Approved", "summary": "The new vaccine promises faster immunity."},
        {"title": "Fitness Trends 2025", "summary": "Virtual workouts are dominating routines."}
    ]
}

@app.route('/')
def home():
    return render_template("home.html", categories=news_data.keys())

@app.route('/news/<category>')
def show_news(category):
    articles = news_data.get(category, [])
    return render_template("news.html", category=category, articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
