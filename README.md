# CSCI2910Lab4
This is a coding Lab using web APIs for CSCI 2910.

## Process Log
- The API doc states how to used/call the API:<br>
`with AnimeFLV() as api:`<br>
- The search method `def search(self, query: str = None, page: int = None) -> List[AnimeInfo]:`<br>
Returns an array, however I don't fully understand what it returns.<br>
It is said to return `elements` in this line: `return self._process_anime_list_info(elements)`<br>
However, I think it is simply an array of items type `AnimeInfo` which is a class.<br>


