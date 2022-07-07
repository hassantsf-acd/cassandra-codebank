from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])

session = cluster.connect()

session.set_keyspace('codebank')

# Query 1


async def view_problems_by_tag(tag):
    return session.execute(f"SELECT * FROM problems_by_tag WHERE tag = '{tag}'")


def view_problems_by_tag_sort_on_diff(tag):
    return session.execute(f"SELECT * FROM sorted_diff_on_tags WHERE tag = '{tag}'")


def view_problems_by_tag_sort_on_submits(tag):
    return session.execute(f"SELECT * FROM sorted_submits_on_tags WHERE tag = '{tag}'")


def view_problems_by_tag_sort_on_solved(tag):
    return session.execute(f"SELECT * FROM sorted_solved_on_tags WHERE tag = '{tag}'")


# Query 2
def view_submits_between(start, end):
    return session.execute(f"SELECT * FROM problems_by_tag WHERE submits > {start} AND submits < {end} ALLOW FILTERING;")


def view_submits_between_sort_on_diff(start, end):
    return session.execute(f"SELECT * FROM sorted_diff_on_tags WHERE submits > {start} AND submits < {end} ALLOW FILTERING;")


def view_submits_between_sort_on_submits(start, end):
    return session.execute(f"SELECT * FROM sorted_submits_on_tags WHERE submits > {start} AND submits < {end} ALLOW FILTERING;")


def view_submits_between_sort_on_solved(start, end):
    return session.execute(f"SELECT * FROM sorted_solved_on_tags WHERE submits > {start} AND submits < {end} ALLOW FILTERING;")

# Query 3


def view_difficulty_between(start, end):
    return session.execute(f"SELECT * FROM problems_by_tag WHERE difficulty > {start} AND difficulty < {end} ALLOW FILTERING;")


def view_difficulty_between_sort_on_diff(start, end):
    return session.execute(f"SELECT * FROM sorted_diff_on_tags WHERE difficulty > {start} AND difficulty < {end} ALLOW FILTERING;")


def view_difficulty_between_sort_on_submits(start, end):
    return session.execute(f"SELECT * FROM sorted_submits_on_tags WHERE difficulty > {start} AND difficulty < {end} ALLOW FILTERING;")


def view_difficulty_between_sort_on_solved(start, end):
    return session.execute(f"SELECT * FROM sorted_solved_on_tags WHERE difficulty > {start} AND difficulty < {end} ALLOW FILTERING;")

# Query 4


def view_diff_tag(tag, difficulty):
    return session.execute(f"SELECT * FROM problems_by_tag WHERE tag = '{tag}' AND difficulty = {difficulty}  ALLOW FILTERING;")


def view_diff_tag_sort_on_submits(tag, difficulty):
    return session.execute(f"SELECT * FROM sorted_submits_on_tags WHERE tag = '{tag}' AND difficulty = {difficulty}  ALLOW FILTERING;")


def view_diff_tag_sort_on_solved(tag, difficulty):
    return session.execute(f"SELECT * FROM sorted_solved_on_tags WHERE tag = '{tag}' AND difficulty = {difficulty}  ALLOW FILTERING;")

# Query 5


def view_diff_tag_min_max_avg(tag, difficulty):
    return session.execute(f"SELECT MIN(submits), MAX(submits), AVG(submits) FROM problems_by_tag WHERE tag = '{tag}' AND difficulty = {difficulty}  ALLOW FILTERING;")

# Query 6


def view_solve_ratio_problems_by_tag(tag):
    return session.execute(f"SELECT CAST(solved AS DECIMAL) / submits, tag FROM problems_by_tag WHERE tag = '{tag}'")

# Query 7


def view_solve_ratio_problems_by_tag_company(tag, company):
    return session.execute(f"SELECT id, tag, title, CAST(solved AS DECIMAL) / submits FROM problems_by_tag WHERE tag = '{tag}' AND company = '{company}' ALLOW FILTERING;")

def view_solve_ratio_problems_by_tag_company_all_tags(company):
    return session.execute(f"SELECT id, tag, title, CAST(solved AS DECIMAL) / submits FROM problems_by_tag WHERE company = '{company}' ALLOW FILTERING;")

# Query 8


def view_tags_of_company(company):
    return session.execute(f"SELECT DISTINCT tag, company FROM company_tags WHERE company = '{company}' ALLOW FILTERING;")

# Query 9


def change_difficulty(id, new_difficulty):
    for row in session.execute(f"SELECT * FROM problems_by_tag WHERE id = '{id}' ALLOW FILTERING;"):
        session.execute(
            f"UPDATE problems_by_tag SET difficulty = {new_difficulty} WHERE tag = '{row.tag}' AND id = '{id}';")


# Query 10
def change_diff_company_tag(company, tags, new_difficulty):
    tags_string = ''

    for tag in tags:
        tags_string += (f"'{tag}',")

    tags_string = tags_string[:len(tags_string) - 1]

    for row in session.execute(f"SELECT id FROM problems_by_tag WHERE company = '{company}' AND tag IN ({tags_string}) ALLOW FILTERING;"):
        session.execute(
        f"UPDATE problems_by_tag SET difficulty = {new_difficulty} WHERE id = '{row.id}' AND tag IN ({tags_string});")


# Query 11
def delete_company_problems(company):
    for row in session.execute(f"SELECT * FROM problems_by_tag WHERE company = '{company}' ALLOW FILTERING;"):
        session.execute(
            f"DELETE FROM problems_by_tag WHERE tag = '{row.tag}'AND id = '{row.id}'")


# Query 15
def view_min_max_diff_on_tags(tag):
    return session.execute(f"SELECT MIN(difficulty), MAX(difficulty) FROM problems_by_tag WHERE tag = '{tag}';")

# Query 19


def view_problems_by_tag_of_company(tag, companies):
    company_string = ''

    for company in companies:
        company_string += (f"'{company}',")

    company_string = company_string[:len(company_string) - 1]
    return session.execute(f"SELECT * FROM problems_by_tag WHERE tag = '{tag}' AND company IN ({company_string}) ALLOW FILTERING;")

# Query 18


def sort_tags_on_average():
    session.execute("""CREATE TABLE IF NOT EXISTS sort_tag_on_average(
                        id int,
                        avg_diff float,
                        tag text,
                        PRIMARY KEY((id), avg_diff, tag));
    """)
    for row in session.execute("SELECT DISTINCT tag from problems_by_tag;"):
        avg_diff = session.execute(
            f"SELECT AVG(difficulty) FROM problems_by_tag WHERE tag = '{row.tag}'").one().system_avg_difficulty

        session.execute(
            f"INSERT INTO sort_tag_on_average(id, avg_diff, tag) VALUES({1}, {avg_diff}, '{row.tag}');")

    results = session.execute("SELECT tag, avg_diff FROM sort_tag_on_average;")

    session.execute("DROP TABLE sort_tag_on_average;")

    return results


# Query 17
def sort_companies_on_average():
    session.execute("""CREATE TABLE IF NOT EXISTS sort_company_on_average(
                        id int,
                        avg_diff float,
                        company text,
                        PRIMARY KEY((id), avg_diff, company));
    """)
    for row in session.execute("SELECT DISTINCT company from part_by_company;"):
        avg_diff = session.execute(
            f"SELECT AVG(difficulty) FROM part_by_company WHERE company = '{row.company}'").one().system_avg_difficulty

        session.execute(
            f"INSERT INTO sort_company_on_average(id, avg_diff, company) VALUES({1}, {avg_diff}, '{row.company}');")

    results = session.execute(
        "SELECT company, avg_diff FROM sort_company_on_average;")

    session.execute("DROP TABLE sort_company_on_average;")

    return results

# Query 18


def sort_tags_on_solve_ratio():
    session.execute("""CREATE TABLE IF NOT EXISTS sort_tag_on_solve_ratio(
                        id int,
                        solve_ratio float,
                        tag text,
                        PRIMARY KEY((id), solve_ratio, tag));
    """)
    for row in session.execute("SELECT DISTINCT tag from problems_by_tag;"):
        ratio = session.execute(
            f"SELECT CAST(solved AS DECIMAL) / submits FROM problems_by_tag WHERE tag = '{row.tag}'").one().cast_solved_as_decimal____submits

        session.execute(
            f"INSERT INTO sort_tag_on_solve_ratio(id, solve_ratio, tag) VALUES({1}, {ratio}, '{row.tag}');")

    results = session.execute(
        "SELECT tag, solve_ratio FROM sort_tag_on_solve_ratio;")

    session.execute("DROP TABLE sort_tag_on_solve_ratio;")

    return results
