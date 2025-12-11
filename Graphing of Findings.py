# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 15:20:54 2025

@author: maryp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime 


# %%
## FLOW

obs_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\Observed Data\NY-TL1 Daily Discharge Cut.csv")

obs_df.head()

dates = obs_df["time"].tolist()
day = [datetime.strptime(date, "%m/%d/%Y") for date in dates]

# %%

cal_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Flow.csv")

cal_df.head()

dates1 = cal_df["Date"].tolist()
daycal = [datetime.strptime(date, "%d/%m/%Y") for date in dates1]
# %%

fs1_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Flow_FS1.csv")

fs1_df.head()

datesfs = fs1_df["Date"].tolist()
dayfs = [datetime.strptime(date, "%d/%m/%Y") for date in datesfs]


# %%

fs2_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Flow_FS2.csv")

fs2_df.head()


# %%

fs3_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Flow_FS3.csv")

fs3_df.head()

# %%

gw1_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Flow_GW1.csv")

gw1_df.head()

datesgw = gw1_df["Date"].tolist()
daygw = [datetime.strptime(date, "%d/%m/%Y") for date in datesgw]

# %%

gw2_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Flow_GW2.csv")

gw2_df.head()

# %%

gw3_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Flow_GW3.csv")

gw3_df.head()

# %%

### VISUALIZE FLOW

fig, ax = plt.subplots()
#plt.grid(linestyle = '--')
plt.plot(day, obs_df["m3"], label = "observed", color = "blue")
plt.plot(daycal, cal_df["Value"], label = "modeled", color = "red")
plt.plot(dayfs, fs1_df["Value"], label = "FS1", color = "green")
plt.plot(dayfs, fs2_df["Value"], label = "FS2", color = "purple")
plt.plot(dayfs, fs3_df["Value"], label = "FS3", color = "yellow")
plt.plot(daygw, gw1_df["Value"], label = "GW1", color = "orange")
plt.plot(daygw, gw2_df["Value"], label = "GW2", color = "gray")
plt.plot(daygw, gw3_df["Value"], label = "GW3", color = "black")
#plt.title("Rainfall and Runoff 1977 - 1980")
#plt.xlabel("Date")
plt.legend()
#ax.xaxis.set_major_locator(ticker.MultipleLocator(base=182))
#ax.tick_params(axis='x', labelrotation=45)
plt.show()




# %%

### NITROGEN

obsN_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\Observed Data\NY-TL1 ORGN .csv")

obsN_df.head()

# %%

calN_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Organic-Nitrogen.csv")

calN_df.head()

# %%

fs1N_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Organic-Nitrogen_FS1.csv")

fs1N_df.head()

# %%

fs2N_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Organic-Nitrogen_FS2.csv")

fs2N_df.head()

# %%

fs3N_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Organic-Nitrogen_FS3.csv")

fs3N_df.head()

# %%

gw1N_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Organic-Nitrogen_GW1.csv")

gw1N_df.head()

# %%

gw2N_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Organic-Nitrogen_GW2.csv")

gw2N_df.head()

# %%

gw3N_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Organic-Nitrogen_GW3.csv")

gw3N_df.head()

# %%
### VISUALIZE NITROGEN

fig, ax = plt.subplots()
#plt.grid(linestyle = '--')
#plt.plot(day, obsN_df["orgn kg"], label = "observed", color = "blue")
plt.plot(dayfs, fs1N_df["Value"], label = "FS1", color = "green")
plt.plot(dayfs, fs2N_df["Value"], label = "FS2", color = "purple")
plt.plot(dayfs, fs3N_df["Value"], label = "FS3", color = "yellow")
plt.plot(daygw, gw1N_df["Value"], label = "GW1", color = "orange")
plt.plot(daygw, gw2N_df["Value"], label = "GW2", color = "gray")
plt.plot(daygw, gw3N_df["Value"], label = "GW3", color = "black")
plt.plot(daycal, calN_df["Value"], label = "modeled", color = "red")
#plt.title("Rainfall and Runoff 1977 - 1980")
#plt.xlabel("Date")
plt.legend()
#ax.xaxis.set_major_locator(ticker.MultipleLocator(base=182))
#ax.tick_params(axis='x', labelrotation=45)
plt.show()


# %%


#### PHOSPHORUS


obsP_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\Observed Data\NY-TL1 SOLP.csv")

obsP_df.head()

# %%

calP_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Soluble-Phosphorus.csv")

calP_df.head()

# %%

fs1P_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Soluble-Phosphorus_FS1.csv")

fs1P_df.head()

# %%

fs2P_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Soluble-Phosphorus_FS2.csv")

fs2P_df.head()

# %%

fs3P_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Soluble-Phosphorus_FS3.csv")

fs3P_df.head()

# %%

gw1P_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Soluble-Phosphorus_GW1.csv")

gw1P_df.head()

# %%

gw2P_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Soluble-Phosphorus_GW2.csv")

gw2P_df.head()

# %%

gw3P_df= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Channel_1_Daily_River-Soluble-Phosphorus_GW3.csv")

gw3P_df.head()


# %%
### VISUALIZE PHOSPHORUS

fig, ax = plt.subplots()
#plt.grid(linestyle = '--')
#plt.plot(day, obsN_df["solp kg"], label = "observed", color = "blue")
plt.plot(dayfs, fs1P_df["Value"], label = "FS1", color = "green")
plt.plot(dayfs, fs2P_df["Value"], label = "FS2", color = "purple")
plt.plot(dayfs, fs3P_df["Value"], label = "FS3", color = "yellow")
plt.plot(daygw, gw1P_df["Value"], label = "GW1", color = "orange")
plt.plot(daygw, gw2P_df["Value"], label = "GW2", color = "gray")
plt.plot(daygw, gw3P_df["Value"], label = "GW3", color = "black")
plt.plot(daycal, calP_df["Value"], label = "modeled", color = "red")
#plt.title("Rainfall and Runoff 1977 - 1980")
#plt.xlabel("Date")
plt.legend()
#ax.xaxis.set_major_locator(ticker.MultipleLocator(base=182))
#ax.tick_params(axis='x', labelrotation=45)
plt.show()






