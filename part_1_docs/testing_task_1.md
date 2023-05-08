### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  # constructor method missing 


  def check_for_ace(self, card):
    if card.value = 1:
      # == sign needed instead of just one =
      return True
    else
    # colon (:) missing after else statement
      return False
   

  dif highest_card(self, card1 card2):
  # typo in defining function (def not dif) and comma (,) needed between paramenters card1 and card2
  if card1.value > card2.value:
    return card
    # card1 should be returned
  else:
    return card2
  


def cards_total(self, cards):
  total
  # initial value is missing (total = 0)
  for card in cards:
    total += card.value
    return "You have a total of" + total
  # total needs to be a string to allow concatenation ---> str(total)
  
```
