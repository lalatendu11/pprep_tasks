# importing  csv
import csv
# read csv file to a list of dictionaries
with open('students.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    data1 = [row for row in csv_reader]
# print(data1)

import oracledb


# Establish a connection
connection = oracledb.connect(
    user="lalatendu",
    password="lalatendu",
    dsn="LAPTOP-LOJK968K:1521/XE"
)

# Create a cursor
cursor = connection.cursor()

# Execute a query
query = "SELECT * FROM student"
cursor.execute(query)

# Fetch data and convert to a list of dictionaries
columns = [col[0] for col in cursor.description]
data2= [dict(zip(columns, row)) for row in cursor.fetchall()]

# Close cursor and connection
cursor.close()
connection.close()

# Print the result
# print(data2)

# Merging Dictionary-lists with duplicate value
def merge(data1, data2, key):
    result_set = set()
    merged_list = []

    for d in data1 + data2:
        if d[key] not in result_set:
            result_set.add(d[key])
            merged_list.append(d)

    return merged_list



merged_list = merge(data1, data2, key='SNAME')
print(merged_list)

# for item in merged_list:
#     print(item)


