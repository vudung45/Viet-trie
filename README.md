# Viet-trie
Scrape all vietnamese words from VDict.com and construct a trie datastructure to store all of those words

# Test:
```python
  print(f"VietTrie.has_word(đàn bà) --> {VietTrie.has_word('đàn bà')}")
  print(f"VietTrie.has_word(đàn bà) --> {VietTrie.has_word('đàn ông')}")
  print(f"VietTrie.has_word(english) --> {VietTrie.has_word('english')}")
  print(f"VietTrie.has_word(việt nam) --> {VietTrie.has_word('việt nam')}")
  print(f"Extract words from this sentence: thiên nhiên việt nam rất là hùng vĩ -> {VietTrie.extract_words('thiên nhiên việt nam rất là hùng vĩ')}")
```

```
VietTrie.has_word(đàn bà) --> True
VietTrie.has_word(đàn bà) --> True
VietTrie.has_word(english) --> False
VietTrie.has_word(việt nam) --> True
Extract words from this sentence: thiên nhiên việt nam rất là hùng vĩ -> ['thiên nhiên', 'việt nam', 'rất', 'là', 'hùng vĩ']
```