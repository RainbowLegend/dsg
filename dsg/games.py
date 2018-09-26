from errors import *

class Games:

    def __init__(self, **kwargs):
        pass

    list_of = ['Instinct', 'TheJourney', 'WallpaperMaker']

    class Instinct:
        dl_link = 'http://www.mediafire.com/file/kf462h2hp25ggye/InstinctTechDemo.zip'
        price = 59.99
        premium_price = 79.99
        os_support = ['Windows', 'OSX']
        description = "'Instinct' is a first-person survival game where your only options are to explore or\n"
        "to die. You are on an island full of mysterious shrines and mechs - lots and lots of\n"
        "huge mechs that are not happy to see you. Gather materials to obtain a weapon and upgrade\n"
        "them by completing objectives in the shrines. Defeat enough monstrosities to use their\n"
        "materials to get away from the island. But be warned! It is very unsafe to seek shelter\n"
        "and stay in one place, so sleeping is out of the question. Encounter oil drops\n"
        "(yes you can drink oil) to keep yourself awake before your energy runs out. If you fail\n"
        "to find enough oil and finally pass out, the mechs will find and annihilate you. Survive this\n"
        "strange, mechanical setting and beat awesome boss battles!"

    class WallpaperMarker:
        year = '2019'
        price = 0.99
        dl_link = 'None, WIP'
        os_support = ['iOS']
        description = "Wallpaper Maker 2019 is a revolutionary wallpaper creator tool for your tablets, phones\n"
        "and computers! It uses revolutionary far-field technology to closely emulate nature's true look\n"
        "synthetically."

    class TheJourney:
        dl_link = 'https://1shotgame.ga/journeyv028'
        price = None
        os_support = ['Windows']
        version = '0.2.8'
