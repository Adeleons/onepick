from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient

client = MongoClient('mongodb+srv://kimseyoung:onepick@cluster0.osxlygm.mongodb.net/?retryWrites=true&w=majority')
db = client.onepick
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/lunch", methods=['GET'])
def lunch_post():
   city_receive = request.form.get('city')
   category_receive = request.form.get('category')

   lunch_list = list(db.lunch.find({'city': {'$in': [city_receive]}}, {'category': {'$in': [category_receive]}}))

   for d in lunch_list:
       return render_template('index.html', s_restaurant=d['restaurant'], s_represent=d['represent'],
                              s_food=d['food'])


if __name__ == '__main__':
    app.run('0.0.0.0', port=5100, debug=True)