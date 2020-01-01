from typing import List, Iterable, Generator
import itertools
class VietTrie:
  def __init__(self) -> None:
    self.next = {}
    self.is_word = False


  # this function is created for efficiency purposes
  # Used for efficient sliding window approach to attract all words
  # from a list of tokens from LEFT -> RIGHT
  def trail_depth(self, word_gen: Generator[str, None, None]) -> int:
    depth = 0
    max_depth = depth
    tmp = self
    for token in word_gen:
      if token not in tmp.next:
        return max_depth
      tmp = tmp.next[token]
      depth += 1
      max_depth = depth if tmp.is_word else max_depth

    return max_depth

  def extract_words(self, sentence: str) -> List[str]:
    tokens = sentence.split(" ")
    words = []
    i = 0
    while i < len(tokens):
      word_gen = itertools.islice(tokens , i, len(tokens))
      depth = max(1, self.trail_depth(word_gen))
      words.append(" ".join(tokens[i:i+depth]))
      i += depth
    return words


  def has_word(self, word: str) -> bool:
    tokens = word.split(" ")
    tmp = self
    for token in tokens:
      if token not in tmp.next:
        return False
      tmp = tmp.next[token]
    return tmp.is_word


  def add_word(self, word: str) -> None:
    tokens = word.split(" ")
    tmp = self
    for token in tokens:
      if token not in tmp.next:
        tmp.next[token] = self.__class__() # a hack to make VietTrie singleton :)
      tmp = tmp.next[token]

    tmp.is_word = True

words = []
with open("words.txt", "r") as f:
  words = f.read().split("\n")

# a hack to make VietTrie singleton :)
VietTrie = VietTrie()

for word in words:
  VietTrie.add_word(word)



if __name__ == "__main__":
  print(f"VietTrie.has_word(đàn bà) --> {VietTrie.has_word('đàn bà')}")
  print(f"VietTrie.has_word(đàn bà) --> {VietTrie.has_word('đàn ông')}")
  print(f"VietTrie.has_word(english) --> {VietTrie.has_word('english')}")
  print(f"VietTrie.has_word(việt nam) --> {VietTrie.has_word('việt nam')}")
  print(f"Extract words from this sentence: thiên nhiên việt nam rất là hùng vĩ -> {VietTrie.extract_words('thiên nhiên việt nam rất là hùng vĩ')}")
  print(f"Extract words from this sentence: mày lúc nào cũng í a í ới nhức hết cả đầu -> {VietTrie.extract_words('mày lúc nào cũng í a í ới nhức hết cả đầu')}")
  print(f"Extract words from this sentence: chạy chậm ì à ì ạch -> {VietTrie.extract_words('chạy chậm ì à ì ạch')}")










