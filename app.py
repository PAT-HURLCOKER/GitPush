# Initialize all dependencies
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_mars

# Initialize Flask
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


# Initialize the HTML routes
# two routes established (index html and the py code to scrape
@app.route('/')

def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update
    (
        {},
        mars_data,
        upsert=True
    )

    return 'Scraping Successful!'


if __name__ == "__main__":

    app.run(debug=True)