import requests
import urllib.request
import os.path

def main():
    #Ways to speed up:
    # - Async for each instances
    # - Faster Downloads for images
    #uwu.st??? getting 404 
    instances = ["mastodon.gamedev.place","mastodon.art","social.tchncs.de",
                 "lgbtq.cool","witches.live","laserdisc.party",
                 "fedi.lynnesbian.space","cybre.space","efdn.club",
                 "lamp.institute","radical.town","jorts.horse",
                 "mastodon.social","knzk.me","octodon.social",
                "deadinsi.de"]
    instances.sort()
    setup(instances)
    try:
        for name in instances:
            print("-----!"+name+"!-----")
            fetch(name)
    except Exception as e:
        print("Instance Error")
        print(e)

def fetch(name):
    r = requests.get('https://%s/api/v1/custom_emojis'% name, allow_redirects=True)
    path = "emoji/%s/" % name
    try: 
        for emoji in r.json():
            try:
                if os.path.isfile(path+emoji['shortcode']+".png"):
                    pass
                else:
                    print(emoji['shortcode'] + " found!")
                    emojiimage = requests.get(emoji['static_url'],allow_redirects=True)
                    open(path + emoji['shortcode']+".png",'wb').write(emojiimage.content)
            except Exception as e:
                print("Did not get: " + emoji['url'])
                print(e)
                pass
    except Exception as e:
        print(e)

def setup(instances): 
    if (os.path.isdir("emoji/")):
        pass   
    else:
        os.mkdir("emoji/")

    for name in instances:
        if (os.path.isdir("emoji/%s/"%name)):
            pass
        else: os.mkdir("emoji/%s/"%name)
 
if __name__ == '__main__':
    main()