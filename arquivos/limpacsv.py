import csv

def format_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)

        formatted_data = []
        for row in reader:
            formatted_row = []
            for item in row:
              
                if item.startswith('[') and item.endswith(']'):
                    item = item[1:-1]
                item = item.replace("'", "")

                
                item = item.strip()

                formatted_row.append(item)

            formatted_data.append(formatted_row)

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(formatted_data)

    print("Arquivo CSV formatado com sucesso!")

input_file = '/tmp/titles.csv'
output_file = '/tmp/person_formatted.csv'
format_csv(input_file, output_file)
