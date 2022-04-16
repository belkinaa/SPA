def setConfig_sliderweb(nameApp):
    nameApp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/spa_db'
    nameApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return nameApp
