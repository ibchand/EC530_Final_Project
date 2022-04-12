import csv
import json

trees = []

with open('Trees.csv', newline='') as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=',',)

  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      print(f'Column names are {", ".join(row)}')
      line_count += 1
    else:
      if line_count % 128 == 0:
        trees.append({"lat": float(row[0]), "long": float(row[1])})
        line_count += 1
      else:
        line_count += 1
    
output_file = open("Trees.json", "w")

json.dump(trees, output_file, indent = 2)
  
output_file.close()