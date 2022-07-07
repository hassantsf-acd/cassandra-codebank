from cassandra.cluster import Cluster
import pandas as pd
from util import convert_string_to_list, convert_string_bigint

df = pd.read_csv('data.csv')

cluster = Cluster(['127.0.0.1'])

session = cluster.connect()

session.set_keyspace('codebank')

prepared_stmt = session.prepare(
    "INSERT INTO problems_by_tag(id, title, type, difficulty, company, submits, solved, tag, time_step) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
for idx, row in df.iterrows():
    if row['tags'] == "[]":
        session.execute(prepared_stmt, [str(row['id']), str(row['title']), str(row['type']), int(row['difficulty']), str(row['company']),
                                        int(row['submits']), int(row['solved']), 'NO_TAG', convert_string_bigint(row['time_step'])])
    else:
        for tag in convert_string_to_list(row['tags']):
            session.execute(prepared_stmt, [str(row['id']), str(row['title']), str(row['type']), int(row['difficulty']), str(row['company']),
                                            int(row['submits']), int(row['solved']), tag, convert_string_bigint(row['time_step'])])