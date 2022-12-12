import sys
from fri_a import *
from fri_e import *
from fri_m import *
from napi_heti import fri_napi
from mon_a import *
from mon_e import *
from mon_m import *
from napi_heti import mon_napi
from sat_a import *
from sat_e import *
from sat_m import *
from napi_heti import sat_napi
from sun_a import *
from sun_e import *
from sun_m import *
from napi_heti import sun_napi
from thu_a import *
from thu_e import *
from thu_m import *
from napi_heti import thu_napi
from tue_a import *
from tue_e import *
from tue_m import *
from napi_heti import tue_napi
from wed_a import *
from wed_e import *
from wed_m import *
from napi_heti import wed_napi
from napi_heti import hetiossz


def alap():
        frid_m()
        frid_e()
        frid_a()
        fri_napi()
        mon_a()
        mon_e()
        mon_m()
        mon_napi()
        sat_a()
        sat_e()
        sat_m()
        sat_napi()
        sun_a()
        sun_e()
        sun_m()
        sun_napi()
        thu_a()
        thu_e()
        thu_m()
        thu_napi()
        tue_a()
        tue_e()
        tue_m()
        tue_napi()
        wed_a()
        wed_e()
        wed_m()
        wed_napi()
        hetiossz()



with open('bevetel.txt', 'w', encoding="utf-8") as sys.stdout:
    alap()

