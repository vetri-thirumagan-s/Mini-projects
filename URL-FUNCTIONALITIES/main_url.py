import pyshorteners as pyshort
import pyperclip

def shortening(url):

  #  Creates a URL shortener object
  short_url = pyshort.Shortener()

  # Provides access to shortening
  return short_url.tinyurl.short(url)

def expanding(url):

  #  Creates a URL shortener object
  long_url = pyshort.Shortener()

  # Provides access to expanding
  return long_url.tinyurl.expand(url)       



def copy(text_to_be_copied):
    return pyperclip.copy(text_to_be_copied)