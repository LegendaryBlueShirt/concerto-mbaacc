from kivy.config import Config
import configparser
import os
import sys
from kivy.resources import resource_add_path
if hasattr(sys, '_MEIPASS'):
    resource_add_path(os.path.join(sys._MEIPASS))
os.environ["KIVY_AUDIO"] = "sdl2"
# Kivy app configs
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'multisamples', 0)
Config.set('kivy', 'desktop', 1)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('kivy', 'window_icon', 'concertoicon.ico')
Config.set(
    "kivy",
    "default_font",
    [
        "Roboto",
        'data/fonts/Roboto-Regular.ttf', 
        'data/fonts/Roboto-Italic.ttf',
        'data/fonts/Roboto-Bold.ttf', 
        'data/fonts/Roboto-BoldItalic.ttf'
    ],
)
Config.write()

if getattr(sys,'frozen', False): #frozen exe
    PATH = os.path.dirname(sys.argv[0])
else: #not frozen
    PATH = os.path.dirname(os.path.abspath(__file__))

try:
    # load caster .ini
    with open(PATH + '\cccaster\config.ini', 'r') as f:
        config_string = '[settings]\n' + f.read()
    caster_config = configparser.ConfigParser()
    caster_config.read_string(config_string)
except:
    caster_config = None

if os.path.exists(PATH + '\concerto.ini'):
    with open(PATH + '\concerto.ini') as f:
        config_string = f.read()
else:
    with open(PATH + '\concerto.ini', 'w') as f:
        f.write('[settings]\n')
        f.write('netplay_port = 0\n')
        f.write('mute_alerts = 0\n')
        f.write('mute_bgm = 0\n')
        f.close()
    with open(PATH + '\concerto.ini','r') as f:
        config_string = f.read()
app_config = configparser.ConfigParser()
app_config.read_string(config_string)

LOBBYURL = "https://concerto-mbaacc.herokuapp.com/l"
VERSIONURL = "https://concerto-mbaacc.herokuapp.com/v"
CURRENT_VERSION = '7-5-2021'