import requests
import os.path
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation
import random
import optparse
from pygame import mixer

my_path = os.path.abspath(os.path.dirname(__file__))
parser = optparse.OptionParser()
url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={}&key={}"
key = "AIzaSyBFshWcaYNFxlVysaVJ4yVNPITI1aOPhNE"
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink',
          'tab:gray', 'tab:olive', 'tab:cyan']

fig = plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
xar = []
yar = []
x2ar = []
y2ar = []


def get_subs_count(channel_id):
    r_url = url.format(channel_id, key)
    req = requests.get(r_url).json()
    subs_count = req['items'][0]["statistics"]["subscriberCount"]
    return int(subs_count)


def playBL():
    path = my_path + "/res/bitch-lasagna.ogg"
    mixer.init()
    mixer.music.load(path)
    mixer.music.play(-1)


def animate(i):
    pdp = get_subs_count("pewdiepie")
    tseries = get_subs_count("tseries")
    i = i + 3
    xar.append(int(i))
    x2ar.append(int(i))
    yar.append(int(pdp))
    y2ar.append(int(tseries))
    if len(xar) > 10:
        xar.remove(xar[0])
        yar.remove(yar[0])
        x2ar.remove(x2ar[0])
        y2ar.remove(y2ar[0])
    ax1.clear()
    ax1.set_title("PewDiePie")
    ax1.ticklabel_format(useOffset=False)
    ax1.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax1.plot(xar, yar, '-ob')
    ax2.clear()
    ax2.set_title("T-Series")
    ax2.ticklabel_format(useOffset=False)
    ax2.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax2.plot(x2ar, y2ar, '-ob')
    ax1.set_ylabel('Pewdiepie Sub Count')
    ax2.set_ylabel('T-Series Sub Count')
    plt.xlabel('Time(Seconds)')
    fig.canvas.set_window_title('Pewdiepie vs T-Series')
    if memesEnabled == 'True': updateOnRender()


def updateOnRender():
    ax1.set_facecolor(random.choice(colors))
    ax2.set_facecolor(random.choice(colors))
    fig.set_facecolor(random.choice(colors))


parser.add_option('-m', '--memes',
                  action="store", dest="memes",
                  help="wanna enable memes? if so send me as True", default="")
options, args = parser.parse_args()
memesEnabled = options.memes
if memesEnabled == 'True': playBL()
ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()
