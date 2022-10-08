from csv import reader

def import_csv_file(file: str):
  terrain = []
  fullpath = f'./assets/csv/{file}'
  with open(fullpath) as file:
    data = reader(file, delimiter=',')
    for row in data:
      terrain.append(list(row))

  return terrain
