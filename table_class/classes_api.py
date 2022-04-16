import time
from datetime import datetime

class OperationDB():
    def __init__(self, DB):
        self.db = DB

    # Получение строки из таблицы по ID
    def getRows(self, dbClass, ID):
        return dbClass.query.filter_by(id=int(ID)).first()

    def get_all(self, dbClass):
        return dbClass.query.all()

    # Получение нового ID
    def get_newId(self, dbName):
        cashRows = dbName.query.order_by(dbName.id.desc()).first()
        if cashRows is None:
            return 1
        else:
            return cashRows.id + 1

    # Новая запись в БД (INSERT)
    def write_rows_DB(self, newRowsCash):
        self.db.session.add(newRowsCash)
        self.db.session.commit()
        self.db.session.close()

    # Обновление записей в БД (UPDATE)
    def update_op_table(self, dbTab, idRows, field_lst, data_list):
        print('field_lst |==>', field_lst)
        print('data_list |==>', data_list)
        cash = self.db.session.query(dbTab).filter_by(
        id = int(idRows)).first()
        if cash is None:
            print('Нет такой строки!')
            for name, value in zip(field_lst, data_list):
                print('name=>', name, '|->|', 'value=>', value, )
                setattr(cash, name, value)
                self.db.session.commit()
                self.db.session.close()


class Unnamed_api(OperationDB):
    def __init__(self, db, dbUnnamed):
        super().__init__(DB=db)
        self.dbUnnamed = dbUnnamed

    def getUser(self, ID):
        return self.getRows(dbClass=self.dbUnnamed, ID=ID)

    def get_all(self):
        super().get_all(dbClass=self.dbUnnamed)
        cash = []
        for rows in self.dbUnnamed.query.all():
            cash.append({
                'id': rows.id,
                'name': rows.name,
                'date': rows.date,
                'amount': rows.amount,
                'distanse': rows.distanse
            })
        return cash

    def new_write(self, name, amount, distanse):
        self.idUser = self.get_newId(dbName=self.dbUnnamed)
        self.write_rows_DB(newRowsCash=self.dbUnnamed(id=self.idUser,
                                                      date=datetime.fromtimestamp(time.time()),
                                                      name=name,
                                                      amount=amount,
                                                      distanse=distanse))
