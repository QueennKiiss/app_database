from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.sql import select
from sqlalchemy.engine import reflection
import mysql.connector

engine = create_engine("mysql+mysqlconnector://mmaestro:Mmaestro-236@localhost/svf", echo=True)
metadata = MetaData()

# On way to get from engine
metadata.reflect(bind=engine)

# print(f"List of MySQL server tables: {metadata.sorted_tables}")
# print(metadata.tables)

sut_table = metadata.tables['SUT']

print(type(sut_table))

# with engine.connect() as conn:
# 	s = select(['SUT'])
# 	result = conn.execute(s)
# 	print(result)

	# result = conn.execute("select SUT_id from SUT")
	# for row in result:
	# 	print("username:", row['SUT_id'])
	# # print(conn.scalar(text("select 'hi'")))

