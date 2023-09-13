from replit import audio
import os, time

print()
def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    input()
while True:
  os.system('clear')
  print('🎵 MyPOD Music Player')
  print()
  time.sleep(2)
  print('Press 1 to Play')
  time.sleep(2)
  print('Press 2 to Exit')
  time.sleep(2)
  print()
  print('Press anything else to see the menu again.')            
  askUser = input('> ')
  if askUser == '1':
    play()
  elif askUser == '2':
    break
  else:
    continue
  # check whether you should call the play() subroutine depending on user's input