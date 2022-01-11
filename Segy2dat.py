import numpy as np
import xarray as xr
from segysak import open_seisnc, segy
import pathlib

segy_path = pathlib.Path("C:\\Users\\Administrator\\cig-cnooc\\cnooc\\data\\prediction\\kerry.sgy")     #设置一下sgy的存储地址
segy.get_segy_texthead(segy_path)

from segysak.segy import segy_loader, well_known_byte_locs
testdata = segy_loader(segy_path, iline=9, xline=21, cdpx=73, cdpy=77, vert_domain="TWT")
testdata

testdata['data'].shape
seismic=testdata['data'].values
seismic.shape
seismic.dtype
seismic.tofile("C:\\Users\\Administrator\\cig-cnooc\\cnooc\\data\\prediction\\seis.dat")     #存储dat的地址
