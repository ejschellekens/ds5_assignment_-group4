def readRecord() -> list:
    """Reads the CSV file and transfers it to an array
    
    :returns:
     list: all records in the CSV file.
    """
    file_path = input("Enter the path to the CSV file: ")
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            records.append(row)
    
    return records

def calculateAverage(records : list):
    """Calculates the average grade
    
    :param records: records of all students
    """
    total = sum(float(record['Grade']) for record in records)
    average = total / len(records)

    print(f"Average Grade: {average}")
    print("--------------------")

def filterGrade(records : list):
    """Filters grade above 80
    
     :param records: records of all students
    """
    filtered_records = [record for record in records if float(record['Grade']) >= 80.0]

    print("Student Report")
    print("--------------")
    for record in filtered_records:
        print(f"Name: {record['Name']}")
        print(f"Grade: {record['Grade']}")
        print("--------------------")