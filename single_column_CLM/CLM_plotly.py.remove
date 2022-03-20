## load PFCLM output and make plots / do anaylsis

from parflow.tools.fs import get_absolute_path
from parflowio.pyParflowio import PFData
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

# intialize data and time arrays
data    = np.zeros([8,8760])  # an array where we store the PF output as columns
time    = np.zeros([8760])    # time array, we will probably want to swap with a date
forcing = np.zeros([8,8760])  # array to load in the meterological forcing

# load forcing file as numpy array, note should fix so count is 1-8760 instead of 0-8759
# variables are:
# 0 DSWR: Downward Visible or Short-Wave radiation [W/m2].
# 1 DLWR: Downward Infa-Red or Long-Wave radiation [W/m2]
# 2 APCP: Precipitation rate [mm/s]
# 3 Temp: Air temperature [K]
# 4 UGRD: West-to-East or U-component of wind [m/s] 
# 5 VGRD: South-to-North or V-component of wind [m/s]
# 6 Press: Atmospheric Pressure [pa]
# 7 SPFH: Water-vapor specific humidity [kg/kg]
#
ffname = 'forcing/narr_1hr.txt'
forcing = np.loadtxt(ffname,max_rows=8760)
print(forcing[2,0:10])
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
    data[1,icount] = data_arr[0,0,0]  #net latent heat flux (Wm-2)
    data[2,icount] = data_arr[4,0,0]  #net veg. evaporation and transpiration and soil evaporation (mms-1)
    data[3,icount] = data_arr[10,0,0] #SWE (mm)
    data[5,icount] = data_arr[2,0,0]  #net sensible heat flux (Wm-2)
    data[6,icount] = data_arr[3,0,0]  #net sensible heat flux (Wm-2)
    base = "output/PFCLM_SC.out.press.{:05d}.pfb"
    filename = base.format(icount)
    data_obj = PFData(filename)
    data_obj.loadHeader()
    data_obj.loadData()
    data_arr = data_obj.getDataAsArray()
    data_obj.close()
    data[4,icount] = (np.sqrt(slope)/mannings) * np.maximum(data_arr[19,0,0],0.0)**(5.0/3.0)
    time[icount] = icount


# Plot LH Flux, SWE and Runoff
#fig, ax = plt.subplots()
#ax2 = ax.twinx()
#ax.plot(time[1:8760],data[1,1:8760], color='g')
#ax.plot(time[1:8760],data[3,1:8760], color='b')
#ax2.plot(time[1:8760],data[4,1:8760], color='r')
#ax.set_xlabel('Time, WY [hr]')
#ax.set_ylabel('LH Flux, SWE')
#ax2.set_ylabel('Runoff [m/h]')
#plt.show()

# Initialize figure with subplots

fig = make_subplots(rows=2, cols=2,column_widths=[0.5, 0.5],row_heights=[0.3, 0.7],horizontal_spacing=0.1, vertical_spacing=0.1,specs=[[{"type": "scatter","rowspan": 2}, {"type": "scattergeo"}],[None, {"type": "scatter","l":0,"r":0, "t":0, "b":0}]],subplot_titles=("P, ET, R","Site Location","LH, SH, G for Single Column Simulation"))
#fig = go.Figure()
fig.add_trace(go.Scatter(x=time[1:8760], y=(data[2,1:8760]*3.6), name='ET [m/h]', line=dict(color='red', width=1)), 1, 1)
fig.add_trace(go.Scatter(x=time[1:8760], y=(forcing[1:8760,2]*3.6), name='precip [m/h]',line=dict(color='green', width=1)),1,1)
fig.append_trace(go.Scatter(x=time[1:8760], y=data[4,1:8760], name = 'Runoff [m/h]',line=dict(color='blue', width=1)),1,1)
fig.update_xaxes(title_text='Time [h] WY', row=1,col=1)
fig.update_yaxes(title_text='Water Flux [m/h]', row=1,col=1)

# domain location, should read in from metadata
lat = (34.9604,) 
lon = (-97.9789,)

fig.add_trace(go.Scattergeo(lon=lon, lat=lat,name='Site Location',
    mode = 'markers', marker=dict(color='black')),1,2)
fig.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="RebeccaPurple",
    showland=True, landcolor="LightGray",
    showocean=True, oceancolor="LightBlue",
    showlakes=True, lakecolor="Blue",
    showrivers=True, rivercolor="Blue")
#fitbounds="locations")
fig.update_layout(geo_scope='usa')  #,margin={"r":0,"t":0,"l":0,"b":0})

#LH, SH, G plot
#
fig.add_trace(go.Scatter(x=time[1:8760], y=data[1,1:8760], name='LH [W/m2]',
                         line=dict(color='red', width=1)),2,2)
fig.append_trace(go.Scatter(x=time[1:8760], y=data[5,1:8760], name = 'SH [W/m2]',
                         line=dict(color='blue', width=1)),2,2)
fig.append_trace(go.Scatter(x=time[1:8760], y=data[6,1:8760], name='G [W/m2]',
                         line=dict(color='green', width=1) 
),2,2)

fig.update_xaxes(title_text='Time [h] WY',row=2, col=2)
fig.update_yaxes(title_text='Energy Flux [W/m2]', row=2, col=2)

# Set theme, margin, and annotation in layout
fig.update_layout(
    width=1000,
    height=500)
#    margin=dict(
#        l=10,
#        r=10,
#        b=10,
#        t=30,
#        pad=0
#    ))
pio.write_html(fig, file='clm_sc.html')
