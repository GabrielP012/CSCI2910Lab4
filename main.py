from animeflv import AnimeFLV
with AnimeFLV() as api:
  elements = api.search(input('Write the anime name: '))
  for i, element in enumerate(elements):
    print(f'{i}, {element.title}')
  try:
    input_selection = (input('select option: '))
    while not input_selection.isdigit():
      input_selection = (input('Invalid Number.  Select option: '))
    selection = int(input_selection)
    info = api.get_anime_info(elements[selection].id)
    info.episodes.reverse()
  except Exception as e:
    print(e)