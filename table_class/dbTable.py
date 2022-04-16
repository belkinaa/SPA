def get_class_Table_for_DB(_db):
    class Unnamed(_db.Model):
        __tablename__ = "users"
        id = _db.Column(_db.Integer, primary_key=True, autoincrement=True)
        date = _db.Column(_db.TIMESTAMP, unique=False, nullable=False)
        name = _db.Column(_db.String(50), unique=False, nullable=False)
        amount = _db.Column(_db.Integer, unique=False, nullable=False)
        distanse = _db.Column(_db.Float, unique=False, nullable=False)

        def __repr__(self):
            return f"table users : {self.id},{self.date},{self.name},{self.amount},{self.distanse}"

    def get_tab_classes(_db_):
        return Unnamed

    return get_tab_classes(_db_=_db)