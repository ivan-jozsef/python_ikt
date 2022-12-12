from fri_a import *
from fri_e import *
from fri_m import *
from mon_a import *
from mon_e import *
from mon_m import *
from sat_a import *
from sat_e import *
from sat_m import *
from sun_a import *
from sun_e import *
from sun_m import *
from thu_a import *
from thu_e import *
from thu_m import *
from tue_a import *
from tue_e import *
from tue_m import *
from wed_a import *
from wed_e import *
from wed_m import *

def fri_napi():
    global fnapi_ossz
    fnapi_ossz = fa + fe + fm
    print("###############################")
    print(f'Péntek napi összes bevétel: {fnapi_ossz} Ft.')
    print("###############################")
fri_napi()

def mon_napi():
    global mnapi_ossz
    mnapi_ossz = ma + me + mm
    print("###############################")
    print(f'Hétfő napi összes bevétel: {mnapi_ossz} Ft.')
    print("###############################")
mon_napi()

def sat_napi():
    global snapi_ossz
    snapi_ossz = sa + se + sm
    print("###############################")
    print(f'Szombat napi összes bevétel: {snapi_ossz} Ft.')
    print("###############################")
sat_napi()

def sun_napi():
    global sunapi_ossz
    sunapi_ossz = sua + sue + sunm
    print("###############################")
    print(f'Vasárnap napi összes bevétel: {sunapi_ossz} Ft.')
    print("###############################")
sun_napi()

def thu_napi():
    global tnapi_ossz
    tnapi_ossz = ta + te + tm
    print("###############################")
    print(f'Csütörtök napi összes bevétel: {tnapi_ossz} Ft.')
    print("###############################")
thu_napi()

def tue_napi():
    global tunapi_ossz
    tunapi_ossz = tua + tue + tum
    print("###############################")
    print(f'Kedd napi összes bevétel: {tunapi_ossz} Ft.')
    print("###############################")
tue_napi()

def wed_napi():
    global wnapi_ossz
    wnapi_ossz = wa + we + wm
    print("###############################")
    print(f'Szerda napi összes bevétel: {wnapi_ossz} Ft.')
    print("###############################")
wed_napi()

def hetiossz():
    heti_ossz = fnapi_ossz + mnapi_ossz + snapi_ossz + sunapi_ossz + tnapi_ossz + tunapi_ossz + wnapi_ossz
    print(f'A heti összbevétel : {heti_ossz} Ft.')
hetiossz()
