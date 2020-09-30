## load PFCLM output and make plots / do anaylsis

from parflow.tools.fs import get_absolute_path
from parflowio.pyParflowio import PFData
import matplotlib.pyplot as plt
import numpy as np

# intialize data and time arrays
data    = np.zeros([8,8760])
time    = np.zeros([8760])

# reading the CLM file PFCLM_SC.out.clm_output.<file number>.C.pfb
# variables are by layer:
# 0  total latent heat flux (Wm-2)
# 1  total upward LW radiation (Wm-2)
# 2  total sensible heat flux (Wm-2)
# 3  ground heat flux (Wm-2)
# 4  net veg. evaporation and transpiration and soil evaporation (mms-1)
# 5  ground evaporation (mms-1)
# 6  soil evaporation (mms-1)
# 7  vegetation evaporation (canopy) and transpiration (mms-1)
# 8  transpiration (mms-1)
# 9  infiltration flux (mms-1)
# 10 SWE (mm)
# 11 ground temperature (K)
# 12 irrigation flux
# 13 - 24 Soil temperature by layer (K)

slope    = 0.05
mannings = 2.e-6

# loop over a year of files (8760 hours) and load in the CLM output
# then map specific variables to the data array which holds things for analysis
# and plotting
for icount in range(1, 8760):
    base = "output/PFCLM_SC.out.clm_output.{:05d}.C.pfb"
    filename = base.format(icount)
    data_obj = PFData(filename)
    data_obj.loadHeader()
    data_obj.loadData()
    data_arr = data_obj.getDataAsArray()
    data_obj.close()
    data[1,icount] = data_arr[0,0,0]  #total (really, it is net) latent heat flux (Wm-2)
    data[2,icount] = data_arr[4,0,0]  #net veg. evaporation and transpiration and soil evaporation (mms-1)
    data[3,icount] = data_arr[10,0,0] #SWE (mm)
    base = "output/PFCLM_SC.out.press.{:05d}.pfb"
    filename = base.format(icount)
    data_obj = PFData(filename)
    data_obj.loadHeader()
    data_obj.loadData()
    data_arr = data_obj.getDataAsArray()
    data_obj.close()
    data[4,icount] = (np.sqrt(slope)/mannings) * np.maximum(data_arr[19,0,0],0.0)**(5.0/3.0)
    time[icount] = icount

fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.plot(time[1:8760],data[1,1:8760], color='g')
ax.plot(time[1:8760],data[3,1:8760], color='b')
ax2.plot(time[1:8760],data[4,1:8760], color='r')

ax.set_xlabel('Time, WY [hr]')
ax.set_ylabel('LH Flux, SWE')
ax2.set_ylabel('Runoff [m/h]')
plt.show()
