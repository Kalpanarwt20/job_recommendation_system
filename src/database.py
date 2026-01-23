# import mysql.connector

# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="ansu.kalpana1412",
#         database="job_recommender"
#     )

# def save_resume_data(resume_text, summary, gaps, roadmap, keywords):
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     query = """
#     INSERT INTO resume_analysis 
#     (resume_text, summary, skill_gaps, roadmap, keywords)
#     VALUES (%s, %s, %s, %s, %s)
#     """

#     cursor.execute(query, (resume_text, summary, gaps, roadmap, keywords))
#     conn.commit()

#     cursor.close()
#     conn.close()
# def fetch_all_resumes():
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)

#     query = "SELECT * FROM resume_analysis"
#     cursor.execute(query)

#     results = cursor.fetchall()

#     cursor.close()
#     conn.close()

#     return results
# def fetch_resume_by_id(resume_id):
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)

#     query = "SELECT * FROM resume_analysis WHERE id = %s"
#     cursor.execute(query, (resume_id,))

#     result = cursor.fetchone()

#     cursor.close()
#     conn.close()

#     return result
# def delete_resume_by_id(resume_id):
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     query = "DELETE FROM resume_analysis WHERE id = %s"
#     cursor.execute(query, (resume_id,))

#     conn.commit()

#     cursor.close()
#     conn.close()
# def update_resume_keywords(resume_id, keywords):
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     query = "UPDATE resume_analysis SET keywords = %s WHERE id = %s"
#     cursor.execute(query, (keywords, resume_id))

#     conn.commit()

#     cursor.close()
#     conn.close()        
# def update_resume_analysis(resume_id, summary, gaps, roadmap):
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     query = """
#     UPDATE resume_analysis 
#     SET summary = %s, skill_gaps = %s, roadmap = %s 
#     WHERE id = %s
#     """
#     cursor.execute(query, (summary, gaps, roadmap, resume_id))

#     conn.commit()

#     cursor.close()
#     conn.close()


import mysql.connector
import os

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        port=os.getenv("MYSQLPORT")
    )




# ---------------- DB CONNECTION ----------------
# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="ansu.kalpana1412",
#         database="job_recommender"
#     )


# ---------------- SAVE RESUME (UPDATED) ----------------
def save_resume_data(name, email, phone, resume_text, summary, gaps, roadmap, keywords):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO resume_analysis
    (name, email, phone, resume_text, summary, skill_gaps, roadmap, keywords)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (name, email, phone, resume_text, summary, gaps, roadmap, keywords)
    )

    conn.commit()
    cursor.close()
    conn.close()


# ---------------- FETCH ALL RESUMES ----------------
def fetch_all_resumes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM resume_analysis"
    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results


# ---------------- FETCH RESUME BY ID ----------------
def fetch_resume_by_id(resume_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM resume_analysis WHERE id = %s"
    cursor.execute(query, (resume_id,))

    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result


# ---------------- DELETE RESUME ----------------
def delete_resume_by_id(resume_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM resume_analysis WHERE id = %s"
    cursor.execute(query, (resume_id,))

    conn.commit()
    cursor.close()
    conn.close()


# ---------------- UPDATE KEYWORDS ----------------
def update_resume_keywords(resume_id, keywords):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE resume_analysis SET keywords = %s WHERE id = %s"
    cursor.execute(query, (keywords, resume_id))

    conn.commit()
    cursor.close()
    conn.close()


# ---------------- UPDATE ANALYSIS ----------------
def update_resume_analysis(resume_id, summary, gaps, roadmap):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    UPDATE resume_analysis
    SET summary = %s, skill_gaps = %s, roadmap = %s
    WHERE id = %s
    """
    cursor.execute(query, (summary, gaps, roadmap, resume_id))

    conn.commit()
    cursor.close()
    conn.close()
