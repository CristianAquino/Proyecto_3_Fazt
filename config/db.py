from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/storedb")

meta = MetaData()

conn = engine.connect()