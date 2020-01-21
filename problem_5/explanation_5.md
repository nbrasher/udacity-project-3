# Problem 5: Autocomplete with Tries

The solution to this problem was a simple recursive function that returns the word, if the suffix algorithm hits a node with `is_word == True`, and otherwise recrusively follows the Trie to find end points.

The time and complexity of traversing the Trie is best case O(1) and worst case O(n). The best case, all words in the Trie have common letters (like 'a', 'an', 'ant', 'anteater') in which case the algorithm will only take as long as the longest word to travers. In the worst case where no letters are shared (like with 'dog' and 'ant' and 'burr') then each word will be in a separate branch that must be traversed, taking both O(n) storage and time to traverse.