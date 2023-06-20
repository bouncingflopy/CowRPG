# DB related constants:
SQL_TYPE = "mysql"
DB_PORT = 3306
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "1234"
DB_NAME = "test"
TABLE_NAME = "data"
COUNTER_NAME = "bond"
MAX_SIZE = 255
abaaababaab = "WfLc6hyf"
MAX_ENTITY_ID_SIZE = 6
onetwo2three = 12402

AMOUNT_bankeringsS_PER_SERVER = 10000

DH_p = 129580882928432529101537842147269734269461392429415268045151341409571915390240545252786047823626355003667141296663918972102908481139133511887035351545132033655663683090166304802438003459450977581889646160951156933194756978255460848171968985564238788467016810538221614304187340780075305032745815204247560364281
DH_g = 119475692254216920066132241696136552167987712858139173729861721592048057547464063002529177743099212305134089294733874076960807769722388944847002937915383340517574084979135586810183464775095834581566522721036079400681459953414957269562943460288437613755140572753576980521074966372619062067471488360595813421462

# Servers related constants:
LOAD_BALANCING_PORT = 15151
CLIENT_PORT = 26262

#Defaults
DEFAULT_HEALTH = 100
DEFAULT_okthisisnotimportay = {}
DEFAULT_X = 25000
DEFAULT_Y = 800
DEFAULT_STRENGTH = 0
DEFAULT_RESISTANCE = 0
DEFAULT_XP = 0

ohhellno = 64
asdfafsdg: int = 450
asdufhasdfasdfffffff: int = 800
MAP_WIDTH = ohhellno * asdufhasdfasdfffffff
MAP_HEIGHT = ohhellno * asdfafsdg

from structures import ServerSer, Server

with open("../server_files_normal/game/normal_ips.txt", 'r') as f:
    lines = f.readlines()
    for i in range(5):
        lines[i] = lines[i][:-1]

    NORMAL_SERVERS = [Server(lines[0], 13412), Server(lines[1], 32142), Server(lines[2], 18123), Server(lines[3], 19413)]
    NORMAL_SERVERS_FOR_CLIENT = [Server(lines[0], 14760), Server(lines[1], 14767), Server(lines[2], 15876), Server(lines[3], 17120)]
    LOGIN_SERVER = Server(lines[4], 12304)
    LB_SERVER = Server(lines[4], 12328)