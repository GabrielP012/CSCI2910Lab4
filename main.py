from animeflv import AnimeFLV
with AnimeFLV() as api:
  elements = api.search(input('Write the anime name: '))
  for i, element in enumerate(elements):
    print(f'{i}, {element.title}')
    