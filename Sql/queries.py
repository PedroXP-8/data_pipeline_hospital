import sqlite3 
import pandas as pd

conn = sqlite3.connect('Database/hospital.db')

# 1: count of all insurance providers
def query_insurance_providers():

    query1 = """ 
    select insurance_provider, count(*) as count
    from patients group by insurance_provider
    order by count desc;
    """
    df_1 = pd.read_sql_query(query1, conn)

    print("Count of all insurance providers:")
    print(df_1)


# 2: patients over than 50 years old
def query_patients_over_50():

    query2 = """
    select name, age, gender, email from patients
    where age >= 50
    order by age desc;
    """

    df_2 = pd.read_sql_query(query2, conn)
    print("\nPatients over 50 years old:")
    print(df_2)


# 3: general informations about patients
def query_general_information():

    query3 = """
    select name as "patient name", age,
    reason_for_visit, appointment_date,
     name as "doctor name", cost as "treatment cost" 
    from patients p
    join appointments a 
        on p.IDpatient = a.ID_patient
    join doctors d
        on a.IDdoctor = d.IDdoctor
    join treatments t
        on a.IDappointment = t.ID_appointment
    order by appointment_date desc;
    """

    df_3 = pd.read_sql_query(query3, conn)
    print("\nGeneral information about patients:")
    print(df_3)


# 4: count of appointments per doctor
def query_appointments_per_doctor():

    query4 = """
    select name as "doctor name", specialization,
    hospital_branch, count(*) as "number of appointments"
    from doctors d
    join appointments a
        on d.IDdoctor = a.ID_doctor
    group by name, specialization, hospital_branch
    order by "number of appointments" desc;
    """ 

    df_4 = pd.read_sql_query(query4, conn)
    print("\nCount of appointments per doctor:")
    print(df_4)