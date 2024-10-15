from animeflv import AnimeFLV
with AnimeFLV() as api:
  elements = api.search(input('Write the anime name: '))