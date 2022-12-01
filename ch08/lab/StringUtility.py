class StringUtility: #Create the class
  
  def __init__(self, string):
    self.string = string 
    
    
  def __str__(self):
    return self.string

  '''
  This method returns self.string
  Returns self.string
  '''
  

  def vowels(self):
    count=0
    char = ''
    for char in self.string:
       if char in 'aeiouAEIOU':
        count += 1
    if count < 5:
      return str(count)
    else:
      return("many")

  '''
This method says that if any charcter in string is a vowel, return the      number of vowels in that string.
Returns number of vowels in strin.
  '''
    
  
  def bothEnds(self):
    if len(self.string) > 2:
      return self.string[0:2] + self.string[-2:]
    else:
        return('')

  """
This method returns string made of first 2 and last 2 characters of given original string. If string length is less than or equal to 2, it returns an empty string.
Returns string of first 2 and last 2 characters of the given string.
"""
  
  def fixStart(self):
    if len(self.string) > 1: 
      self.modstring = self.string
      char = self.string[0] 
      self.modstring = self.modstring.replace(char, '*') 
      self.modstring = char + self.modstring[1:] #Leave first character unchanged
      return self.modstring
    else:
      return self.string 
    
  """
This method leaves the first character of string unchanged. If that first letter is later repeated, that repeated character is replaced with a *. If length is less than or equal to 1, it returns original string.
Returns a string where all repeated characters of first character is replaced by a *.
"""

  def asciiSum(self):
    total = 0
    for char in self.string:
      total += ord(char)
    return total

  """
This method returns an interger that is the sum of all ascii values in the string.
Returns sum of ascii values in string.
"""

  def cipher(self):
    modstring = ""  # Shifted string
    for char in self.string:
      if char.islower():
        modstring = modstring + ((chr((ord(char) + (len(self.string)) - 97)% 
 26 + 97)))  # Lowercase
      elif char.isupper():
        modstring = modstring + ((chr((ord(char) + (len(self.string)) - 65)% 26 + 65)))  # Uppercase
      else:
        modstring = modstring + char  # Non-letters
    return(modstring)

"""
This method encrypts the string by incrementing the letters by length of string. Characters that are not numbers remain unchanged.
Returns encrypted string.
"""

