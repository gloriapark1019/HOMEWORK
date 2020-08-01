from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('homework2.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
# 클라이언트 데이터 받기
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    order = {'name': name_receive, 'count': count_receive, 'address': address_receive, 'phone': phone_receive}

# mongoDB에 넣기
    db.order.insert_one(order)
    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 여길 채워나가세요!
# mongoDB에서 id 값 제외한 데이터 조회하기
    result = list(db.order.find({}, {'_id': 0}))
# order라는 키 값으로 정보 보내주기
    return jsonify({'result': 'success', 'orders': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)