import requests
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation
import datetime

url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={}&key={}"
key = "*INSERT API KEY HERE*"
fig = plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
xar = []
yar = []


def get_subs_count(channel_id):
    r_url = url.format(channel_id, key)
    req = requests.get(r_url).json()
    subs_count = req['items'][0]["statistics"]["subscriberCount"]
    print(channel_id, " :", subs_count)
    return int(subs_count)


def animate(i):
    pdp = get_subs_count("pewdiepie")
    xar.append(int(i))
    yar.append(int(pdp))
    if len(xar) > 5:
        xar.remove(xar[0])
        yar.remove(yar[0])
    ax1.clear()
    ax1.ticklabel_format(useOffset=False)
    ax1.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax1.plot(xar, yar, '-o')
    ax2.clear()
    ax2.ticklabel_format(useOffset=False)
    ax2.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax2.plot(xar, yar, '-o')
    plt.ylabel('Pewdiepie Sub Count')
    plt.xlabel('Time(Seconds)')
    print(yar)
    print(xar)


ani = animation.FuncAnimation(fig, animate, interval=1000)
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
