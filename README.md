# CSCI2910Lab4
This is a coding Lab using web APIs for CSCI 2910.

## Process Log
- The API doc states how to used/call the API:<br>
`with AnimeFLV() as api:`<br>
- The search method `def search(self, query: str = None, page: int = None) -> List[AnimeInfo]:`<br>
Returns an array, however I don't fully understand what it returns.<br>
It is said to return `elements` in this line: `return self._process_anime_list_info(elements)`<br>
However, I think it is simply an array of items type `AnimeInfo` which is another class, <br>
the `search` method is within `AnimeFLV` class.<br>
- I tried to validate the user input for search, however, the method already return completed matches and incomplete ones<br>
it just doesn't return anything if a word is mispelled.
- Then, I used a for loop to iterate over the list `elements`.
- Exception handling, the next code segment will be inside a exception statement.
- Since the user knows the search results, it can pick one result by typing the index.<br>
I am validating the input here as I want to prevent the user from typing a non-integer and therefore call for an exception.
- Finally, I am using the `get_anime_info` method from the API to get and then display the anime info.

