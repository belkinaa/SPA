from ast import literal_eval
import pymysql, json
from werkzeug.utils import redirect

from config import setConfig_sliderweb
from table_class.classes_api import Unnamed_api
from table_class.dbTable import get_class_Table_for_DB

pymysql.install_as_MySQLdb()
from flask import Flask, render_template, url_for, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

testApp = Flask(__name__)

testApp = setConfig_sliderweb(nameApp=testApp)
db = SQLAlchemy(testApp, engine_options={"pool_pre_ping": True})
testApp.secret_key = b'%@#@_5#y2L"$4$#g#@F4Q8z\n\xec]/'

db.init_app(testApp)

dbUnnamed = get_class_Table_for_DB(db)

db.create_all()

# --------------------------
# -- | Главная страница | --
# --------------------  ------
import random


@testApp.route('/')
def index():
    obj_Unnamed_api = Unnamed_api(db=db,
                                  dbUnnamed=dbUnnamed)

    first_data = obj_Unnamed_api.getRows(dbClass=obj_Unnamed_api.dbUnnamed, ID=1)
    if first_data is None:
        lst_data_name = ['Алексей', 'Петр', 'Вася', 'Никифор', 'Федор', 'Антон']
        for i in range(9):
            random_name = random.choices(lst_data_name)
            obj_Unnamed_api.new_write(name=random_name, amount=random.randint(10, 200),
                                      distanse=abs(random.random() * 100 - random.random() * 100))
    alldataUnnamed = obj_Unnamed_api.get_all()
    print('alldataUnnamed->', alldataUnnamed)
    print('type->', type(alldataUnnamed))

    jsonStr = json.dumps(alldataUnnamed,  sort_keys=True, default=str)
    print('jsonStr: ', jsonStr)

    return render_template("index.html",
                           title='Single Page Application',
                           alldataUnnamed=alldataUnnamed,
                           lst_json=jsonStr)
