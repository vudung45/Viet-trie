from typing import List, Iterable, Generator
import itertools
import os.path
import re

def decapitalize(word):
    """
        won't decapitalize the first character if the word is in all CAPS
    """
    return word[:1].lower() + word[1:] if not word.isupper() else word

def simplify(sentence):
    """
        remove spaces in the front and decapitalize the first word
    """
    tokens = sentence.split(" ")
    i = 0

    while i < len(tokens) and tokens[i] == "":
        i += 1
    tokens = tokens[i:]
    if not tokens:
        return ""
    return " ".join([decapitalize(tokens[0])] + tokens[1:])


class VietTrie:
  def __init__(self) -> None:
    self.next = {}
    self.is_word = False


  # this function is created for efficiency purposes
  # Used for efficient sliding window approach to extract all words in a sentence
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

  def extract_words(self, original: str) -> List[str]:
    sentences = [simplify(sentence) for sentence in re.split('[!.?,]+', original)]
    words = []
    for sentence in sentences:
      tokens = [token for token in sentence.split(" ") if token != ""]
      if not tokens:
        continue
        
      i = 0
      # construct a sliding window iterator every iteration
      while i < len(tokens):
        # skip names and title
        tmp = i
        while tmp < len(tokens) and tokens[tmp][0].isupper():
          tmp += 1
        if tmp != i:
          words.append(" ".join(tokens[i:tmp]))
        i = tmp
        if i == len(tokens):
          break

        # extract words from dictionary
        word_gen = itertools.islice(tokens , i, len(tokens)) # sliding window iterator
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
    tokens = word.lower().split(" ")
    tmp = self
    for token in tokens:
      if token not in tmp.next:
        tmp.next[token] = self.__class__() # a hack to make VietTrie singleton :)
      tmp = tmp.next[token]
    tmp.is_word = True

words = []
with open(os.path.join(os.path.dirname(__file__), "words.txt"), "r") as f:
  words = f.read().split("\n")

# a hack to make VietTrie singleton :)
VietTrie = VietTrie()

for word in words:
  VietTrie.add_word(word)



if __name__ == "__main__":
  print(f"VietTrie.has_word(đàn bà) --> {VietTrie.has_word('đàn bà')}")
  print(f"VietTrie.has_word(đàn ông) --> {VietTrie.has_word('đàn ông')}")
  print(f"VietTrie.has_word(english) --> {VietTrie.has_word('english')}")
  print(f"VietTrie.has_word(việt nam) --> {VietTrie.has_word('việt nam')}")
  print(f"Extract words from this sentence: thiên nhiên Việt Nam rất là hùng vĩ -> {VietTrie.extract_words('thiên nhiên Việt Nam rất là hùng vĩ')}")
  print(f"Extract words from this sentence: mày lúc nào cũng í a í ới nhức hết cả đầu -> {VietTrie.extract_words('mày lúc nào cũng í a í ới nhức hết cả đầu')}")
  print(f"Extract words from this sentence: chạy chậm ì à ì ạch -> {VietTrie.extract_words('chạy chậm ì à ì ạch')}")
  print(f"Extract words from this sentence: tôi tên là Hoàng Dũng -> {VietTrie.extract_words('tôi tên là Hoàng Dũng')}")
  print(f"Extract words from this sentence: Tôi tên là Hoàng Dũng -> {VietTrie.extract_words('Tôi tên là Hoàng Dũng')}")
  print(f"Extract words from this sentence: HSBC là ngân hàng -> {VietTrie.extract_words('HSBC là ngân hàng')}")











