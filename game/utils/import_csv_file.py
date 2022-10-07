from csv import reader

def import_csv_file(path: str):
  terrain = []
  with open(path) as file:
    data = reader(file, delimiter=',')
    for row in data:
      terrain.append(list(row))

  return terrain
