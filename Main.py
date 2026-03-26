import sys
sys.path.append('Pipeline')
sys.path.append('Sql')

import tables
import transform
import extract
import load
import queries

def main():

    # Extracting data
    extract_doctors = extract.extract_data("Data/Raw/doctors.csv")
    extract_patients = extract.extract_data("Data/Raw/patients.csv")
    extract_appointments = extract.extract_data("Data/Raw/appointments.csv")
    extract_treatments = extract.extract_data("Data/Raw/treatments.csv")
    extract_billings = extract.extract_data("Data/Raw/billing.csv")

    # Transforming data
    transform_doctors = transform.transform_doctors(extract_doctors)
    transform_patients = transform.transform_patients(extract_patients)
    transform_appointments = transform.transform_appointments(extract_appointments)
    transform_treatments = transform.transform_treatments(extract_treatments)
    transform_billings = transform.transform_billings(extract_billings)

    # creating tables
    tables.create_doctors_table()
    tables.create_patients_table()
    tables.create_appointments_table()
    tables.create_treatments_table()
    tables.create_billings_table()

    # loading data
    load.load_data(transform_doctors, transform_patients,
    transform_appointments, transform_treatments, transform_billings)

    # running queries
    queries.query_insurance_providers()
    queries.query_patients_over_50()
    queries.query_general_information()
    queries.query_appointments_per_doctor()
    
    print("All queries executed successfully.")

if __name__ == "__main__":
    main()


