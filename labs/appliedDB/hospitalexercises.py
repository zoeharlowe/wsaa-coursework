# hospitalexercises.py
# This file contains the exercises for the hospital database.
# Author: Zoe McNamara Harlowe

import pymysql

conn = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='hospital',
                             cursorclass=pymysql.cursors.DictCursor)

def display_menu():
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - Enter New Patient")
    print("2 - Find Patient by Name")

# 1. Enter new patient
def enter_patient():
    cursor = conn.cursor()

    # Get patient details

    # PPSN
    ppsn = input("Enter patient PPSN: ")
    # Check if PPSN already exists
    check_ppsn_sql = "SELECT * FROM patient_table WHERE ppsn = %s"

    with cursor:
        cursor.execute(check_ppsn_sql, (ppsn,))
        existing = cursor.fetchone()

    if existing:
        print("Existing PPSN entered.")
        return

    # First & Surname & Address
    first_name = input("Enter first name: ")
    surname = input("Enter surname: ")
    address = input("Enter address: ")

    # Doctor ID
    doctorID = int(input("Enter doctor ID: "))
    if doctorID != int(doctorID):
        print("Invalid input. Doctor ID must be an integer.")
        return
    # Check if Doctor ID exists
    check_doctor_sql = "SELECT * FROM doctor_table WHERE doctorID = %s"

    with cursor:
        cursor.execute(check_doctor_sql, (doctorID,))
        doctorID = cursor.fetchone()
        if not doctorID:
            print("Doctor ID does not exist.")
            return

    ins = "INSERT INTO patient_table (ppsn, first_name, surname, address, doctorID) VALUES (%s, %s, %s, %s, %s)"

    with cursor:
        try:
            rowsAffected = cursor.execute(ins, (ppsn, first_name, surname, address, doctorID))
            conn.commit()
            if (rowsAffected == 0):
                print("No patient added.")
        except Exception as e:
            print(f"Error occurred: {e}")

def enter_patient():
    cursor = conn.cursor()

    # 1. PPSN
    ppsn = input("Enter patient PPSN: ")

    # Check if PPSN already exists
    check_ppsn_sql = "SELECT * FROM patient_table WHERE ppsn = %s"
    cursor.execute(check_ppsn_sql, (ppsn,))
    if cursor.fetchone():
        print("Existing PPSN entered.")
        return

    # 2. First name, surname, address
    first_name = input("Enter first name: ")
    surname = input("Enter surname: ")
    address = input("Enter address: ")

    # 3. Doctor ID (validate integer)
    doctor_input = input("Enter doctor ID: ")
    if not doctor_input.isdigit():
        print("Invalid input. Doctor ID must be an integer.")
        return

    doctorid = int(doctor_input)

    # Check if doctor exists
    check_doctor_sql = "SELECT * FROM doctor_table WHERE doctorid = %s"
    cursor.execute(check_doctor_sql, (doctorid,))
    doctor_row = cursor.fetchone()

    if not doctor_row:
        print("Doctor ID does not exist.")
        return

    # 4. Insert patient
    insert_sql = """
        INSERT INTO patient_table (ppsn, first_name, surname, address, doctorid)
        VALUES (%s, %s, %s, %s, %s)
    """

    try:
        rowsAffected = cursor.execute(insert_sql, (ppsn, first_name, surname, address, doctorid))
        conn.commit()
        if rowsAffected == 0:
            print("No patient added.")
        else:
            print("Patient added successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


def find_patient():
    name = input("Enter patient name (or partial name): ")

    query = """
        SELECT p.ppsn, p.first_name, p.surname, d.name
        FROM patient_table p
        JOIN doctor_table d ON p.doctorid = d.doctorid
        WHERE p.first_name LIKE %s OR p.surname LIKE %s
    """

    cursor = conn.cursor()
    cursor.execute(query, ('%' + name + '%', '%' + name + '%'))
    patients = cursor.fetchall()

    if not patients:
        print("\nNo patients found.")
        return

    print("\nPatients found:")
    for p in patients:
        print(p['ppsn'], '|', p['first_name'], '|', p['surname'], '|', p['name'])



# Main function
def main():
	# Initialise array

	display_menu()
	
	while True:
		choice = input("Enter choice: ")
		
		if (choice == "1"):
			enter_patient()
			display_menu()
		elif (choice == "2"):
			find_patient()
			display_menu()
		else:
			display_menu()


if __name__ == "__main__":
    main()