from .base import Output

try:
 import speechd
except:
 raise RuntimeError("Cannot find speechd. Please install python-speechd")

class Speechdisp(Output):
 """Speech output supporting Speech Dispatcher on Linux
    Note this requires python-speechd to be installed
 """
 name = "Linux Speech-Dispatcher"
 def __init__(self):
  self.client = speech.SSIPClient('AccessibleOutput2')
  self.client.set_output_motule('espeak-ng')
  self.client.set_punctuation(speech.PunctuationMode.NONE)

 def is_active(self):
  try:
   import speechd
  except:
   return False
  return True

 def speak(self, text, interrupt = 0):
  if interrupt:
   self.silence()
  self.client.speak(text)
 def silence(self):
  self.client.stop()

output_class = Speechdisp
