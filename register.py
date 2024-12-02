from db import db

def register_user(fname, lname, age, email, password):
    conn, cursor = db()

    salt1 = 'sal;dkfgjhfasd;lkdjtha;skljdtghnas;ldktghjn'
    salt2 = 'sal;dktghasl;edkthas;ldjtkhbnsxscvsxlnfmvcaioewrut'


    query = """
    INSERT INTO users (fname, lname, age, email, password) 
    VALUES (%s, %s, %s, %s, %s);
    """
    cursor.execute(query)
    conn.commit()
    conn.close()

    return None

    

