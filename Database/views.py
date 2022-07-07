from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])

session = cluster.connect()

session.set_keyspace('codebank')

session.execute("""
    CREATE MATERIALIZED VIEW sorted_diff_on_tags AS
        SELECT * FROM problems_by_tag
        WHERE tag IS NOT NULL AND difficulty IS NOT NULL AND id IS NOT NULL
        PRIMARY KEY ((tag), difficulty, id);
""")

session.execute("""
    CREATE MATERIALIZED VIEW sorted_submits_on_tags AS
        SELECT * FROM problems_by_tag
        WHERE tag IS NOT NULL AND submits IS NOT NULL AND id IS NOT NULL
        PRIMARY KEY ((tag), submits, id);
""")

session.execute("""
    CREATE MATERIALIZED VIEW sorted_solved_on_tags AS
        SELECT * FROM problems_by_tag
        WHERE tag IS NOT NULL AND solved IS NOT NULL AND id IS NOT NULL
        PRIMARY KEY ((tag), solved, id);
""")


session.execute("""
    CREATE MATERIALIZED VIEW part_by_company AS
        SELECT * FROM problems_by_tag
        WHERE tag IS NOT NULL AND company IS NOT NULL AND id IS NOT NULL
        PRIMARY KEY ((company), tag, id);
""")