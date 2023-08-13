import time
import sys
from tkinter import *

# Setup

root = Tk()
T = Text(root, height=2, width=30)
T.pack()

with open('IMPORTANT.txt', 'r') as myfile:
    name=myfile.readline()
    desc=myfile.readline()
    create=myfile.readline()
    game=myfile.readline()

data = name
data = data.replace('\n', '')
name = data
data = desc
data = data.replace('\n', '')
desc = data
data = create
data = data.replace('\n', '')
create = data
data = game
data = data.replace('\n', '')
game = data

create = 'Made By: ' + create

# Start    
print(name)
print(desc)
print(create)
print(game)

if name == ('') or desc == ('') or create == ('') or game == (''):
    print('Data not found')
    sys.exit()

root = Tk()
T = Text(root, height=3, width=50)
T.pack()
T.insert(END, name + '\n' + desc + '\n' + create)
mainloop()

time.sleep(2)

try:
    root.destroy()
except:
    print('Window already destroyed')
    
exec(open(game).read())
sys.exit
