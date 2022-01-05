import streamlit as st
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from parflow.tools.fs import get_absolute_path
from parflowio.pyParflowio import PFData
import matplotlib.pyplot as plt
from streamlit.elements import color_picker

base_dir = get_absolute_path(".")
N=60
time    = np.zeros([N+1])    # time array, we will probably want to swap with a date
outflow = np.zeros([N+1])  # array to load in the meterological forcing
sat = np.zeros([N+1,300,20])

for icount in range(0, N):
        base = (base_dir+"/dunne_over/Dunne.out.satur.{:05d}.pfb")
        filename = base.format(icount)
        data_obj = PFData(filename)
        data_obj.loadHeader()
        data_obj.loadData()
        data_arr = data_obj.getDataAsArray()
        data_obj.close()
        sat[icount,:,:] = np.where(data_arr[:,0,:]<=0.0, 0.0, data_arr[:,0,:])
        #sat[icount,:,:] = data_arr.reshape(300,20)
        #print(data_arr[4,0,10])
        #print(sat[icount,4,10])
        
        # base = (base_dir+"/output/PFCLM_SC.out.press.{:05d}.pfb")
        # filename = base.format(icount)
        # data_obj = PFData(filename)
        # data_obj.loadHeader()
        # data_obj.loadData()
        # data_arr = data_obj.getDataAsArray()
        # data_obj.close()
        # data[4,icount] = (np.sqrt(slope)/mannings) * np.maximum(data_arr[19,0,0],0.0)**(5.0/3.0)
        # time[icount] = icount
#sat = np.where(sat<=0.0, 0.0, sat)

fig, ax = plt.subplots()

for i in range(N):
    ax.cla()
    ax.imshow(sat[i,:,:],vmin=0.1, vmax=1.0,origin='lower',aspect=0.015,cmap='viridis_r')  #,extent=[0,100,0,1])
    ax.set_title("frame {}".format(i))
    plt.pause(0.01)

fig = go.Figure(
    data=[go.Heatmap(z=sat[0],zmin=0.1,zmax=1.0)],
    layout=go.Layout(
        title="Time 0",
        title_x=0.1,
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None]),
                    dict(label="Pause",
                         method="animate",
                         args=[None,
                               {"frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                                "transition": {"duration": 0}}],
                         )])]
    ),
    frames=[go.Frame(data=[go.Heatmap(z=sat[i],zmin=0.1,zmax=1.0)],
                     layout=go.Layout(title_text=f"Timestep {i+1}")) 
            for i in range(1, N)]
)
fig.show()
#st.plotly_chart(fig)