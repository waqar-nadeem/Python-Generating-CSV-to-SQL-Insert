import csv

def csv_to_sql(input_file, table_name, output_file):
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        columns = reader.fieldnames
        with open(output_file, 'w', encoding='utf-8') as sqlfile:
            for row in reader:
                values = []
                for col in columns:
                    val = row[col]
                    if val is None or val == '':
                        values.append('NULL')
                    else:
                        val = val.replace("'", "''")
                        values.append(f"'{val}'")
                columns_str = ", ".join(columns)
                values_str = ", ".join(values)
                sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});\n"
                sqlfile.write(sql)

csv_to_sql('input.csv', 'your_table_name', 'output.sql')
