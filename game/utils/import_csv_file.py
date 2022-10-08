from csv import reader

def import_csv_file(file: str):
  terrain = []
  fullpath = f'./game/assets/csv/{file}'
  with open(fullpath) as csv_file:
    data = reader(csv_file, delimiter=',')
    for row in data:
      terrain.append(list(row))

  return terrain
