import requests
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation

url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={}&key={}"
key = "AIzaSyA4fROr5xofbdddjAoO5wZtrrQuVIP1wKA"
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
    print(channel_id, " :", subs_count)
    return int(subs_count)


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
    ax1.plot(xar, yar, '-o')
    ax2.clear()
    ax2.set_title("T-Series")
    ax2.ticklabel_format(useOffset=False)
    ax2.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax2.plot(x2ar, y2ar, '-or')
    ax1.set_ylabel('Pewdiepie Sub Count')
    ax2.set_ylabel('T-Series Sub Count')
    plt.xlabel('Time(Seconds)')
    print(yar)
    print(xar)


ani = animation.FuncAnimation(fig, animate, interval=3000)
plt.show()

# while True:
#     pdp_count = get_subs_count("pewdiepie")
#     tsrs_count = get_subs_count("tseries")
#     print("Sub Gap :", pdp_count - tsrs_count)
#     time.sleep(4)

# pdpURL = "https://socialblade.com/youtube/user/pewdiepie/realtime"
# tsrsURL = "https://socialblade.com/youtube/user/tseries/realtime"
#
#
# def get_subs_count(url, channel_name):
#     req = requests.get(url)
#     soup = bs(req.text, 'html.parser')
#     count = soup.findAll('p', id='rawCount')[0].string
#     print(channel_name + ': ' + count)
#
#
# while True:
#     get_subs_count(pdpURL, 'PewDiePie')
#     get_subs_count(tsrsURL, 'T-S*ries')
#     time.sleep(20)
