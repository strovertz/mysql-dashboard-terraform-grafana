import csv

def tsv_to_csv(input_file, output_file, encoding):
    with open(input_file, 'r', encoding=encoding) as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        with open(output_file, 'w', newline='', encoding=encoding) as csvfile:
            writer = csv.writer(csvfile)
            for row in reader:
                writer.writerow(row)

input_file = 'titles.csv'
output_file = 'output.csv'
tsv_to_csv(input_file, output_file, 'utf-8')
