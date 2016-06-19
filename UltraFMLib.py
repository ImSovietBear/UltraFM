#!/usr/bin/python

from subprocess import call

#This is the library for controlling the pifm program with python.
#This was made by Elijah Reeds for use in pifm, but feel free to use it along with your own programs, as well as modify it.
#You can even delete this comment if you want, but I prefer it not be deleted!

isPlaying = false

frequency = 0.0

def play_sound(filename):
   if(!isPlaying):
      call(["./pifm", filename, frequency])
      isPlaying = true
      return
   else:
      print("A sound is already playing! Stop it using stop_sound before trying to play another!")
      return

def stop_sound():
   if(isPlaying):
      call(["killall", ./pifm])
      isPlaying = false
      return
   else:
      print("You must play a sound to stop it!")
      return

def changeFreq(freq):
   frequency = freq
