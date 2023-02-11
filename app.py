import random
from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient

client = MongoClient('mongodb+srv://kimseyoung:onepick@cluster0.osxlygm.mongodb.net/?retryWrites=true&w=majority')
db = client.onepick
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main_page.html')


@app.route("/lunch", methods=["GET"])
def web_lunch_get():
    lunch_list = list(db.lunch.find({}, {'_id': False}))
    return jsonify({"lunchs": lunch_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5100, debug=True)



# from flask import Flask, render_template, request, jsonify
# import random

# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://kimseyoung:onepick@cluster0.fzbyzfc.mongodb.net/Cluster0?retryWrites=true&w=majority')
# db = client.onepick
# app = Flask(__name__)

# @app.route('/')
# def home():
#    return render_template('main_page.html')

# @app.route('/lunch', methods=['POST'])
# def web_lunch_get():
#    city_receive = request.form.get('city_receive')
#    category_receive = request.form.get('category_receive')
#    represent_receive = request.form.get('represent_receive')
#    restaurant_receive = request.form.get('restaurant_receive')

#    doc = {
#       "city" : city_receive,
#       "category" : category_receive,
#       "represent" : represent_receive,
#       "restaurant" : restaurant_receive
      
#    }

   
#    # db.gangnam.find({'city': {'$in': [city_receive]}},{'class': {'$in': [class_receive]}} )
#    for d in db.lunch.find({'city': {'$in': [city_receive]}},{'category': {'$in': [category_receive]}}):
#    # for d in db.lunch.find(doc({'city': {'$in': [city_receive]}},{'category': {'$in': [category_receive]}})):
#       print(d['restaurant'], d['represent'], d['food'])

#    return render_template('real_menu_result.html', s_restaurant = d['restaurant'], s_represent = d['represent'], s_food = d['food'])


# # @app.route("/gangnam", methods=["GET"])
# # def web_gangnam_get():
#     # comment_list = list(db.homework.find({},{'_id':False}))
#     # choice = random.choice(comment_list)
#     # return jsonify({'comments': choice})


# if __name__ == '__main__':
#    app.run('0.0.0.0',port=5100,debug=True)