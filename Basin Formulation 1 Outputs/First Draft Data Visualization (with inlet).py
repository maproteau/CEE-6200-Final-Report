# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 18:57:53 2025

@author: maryp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime 

# %%

##### Calibration Versus Observed

obsQ= pd.read_csv(r"C:\Users\maryp\Box\(1) Cornell\CEE 6200\Project\Daily Discharge TL1-2 FINAL.csv")
print(obsQ.dtypes)

# %%

calQ= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Original Calibrated Exports\Channel_1_Daily_River-Flow.csv")
print(calQ.dtypes)

# %%

datesobs = obsQ["time"].tolist()
dayobsQ = [datetime.strptime(date, "%m/%d/%Y") for date in datesobs]

datescal = calQ["Date"].tolist()
daycalQ = [datetime.strptime(date, "%d/%m/%Y") for date in datescal]

tl1_q = obsQ["m3"].tolist()

cal_tl1_q = calQ["Value"].tolist()

# %%

fig, ax = plt.subplots()
plt.grid(linestyle = '--')
plt.plot(daycalQ, cal_tl1_q, label = "Calibrated Discharge", color = "tomato")
plt.plot(dayobsQ, tl1_q, label = "Observed Discharge", color ="midnightblue")
plt.title("Discharge")
plt.ylabel("Discharge (m^3/s)")
plt.xlabel("Day")
plt.legend()
ax.tick_params(axis='x', labelrotation=45)
plt.show()

# %%


obsN= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\Observed Data\NY-TL1 ORGN .csv")
print(obsN.dtypes)

# %%

calN= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Original Calibrated Exports\Channel_1_Daily_River-Organic-Nitrogen.csv")
print(calN.dtypes)

# %%

datesobsN = obsN["time"].tolist()
dayobsN = [datetime.strptime(date, "%m/%d/%Y") for date in datesobsN]

datescalN = calN["Date"].tolist()
daycalN = [datetime.strptime(date, "%d/%m/%Y") for date in datescalN]

tl1_N = obsN["orgn kg"].tolist()

cal_tl1_N = calN["Value"].tolist()

# %%

fig, ax = plt.subplots()
plt.grid(linestyle = '--')
plt.plot(daycalN, cal_tl1_N, label = "Nitrogen after Calibration", color = "goldenrod")
plt.scatter(dayobsN, tl1_N, label = "Observed Nitrogen", color ="darkgreen")
plt.title("Nitrogen")
plt.ylabel("Nitrogen (kg/day)")
plt.xlabel("Day")
plt.legend()
ax.tick_params(axis='x', labelrotation=45)
plt.show()

# %%

obsP= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\Observed Data\NY-TL1 SOLP.csv")
print(obsP.dtypes)


# %%

calP= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Original Calibrated Exports\Channel_1_Daily_River-Soluble-Phosphorus.csv")
print(calP.dtypes)

# %%

datesobsP = obsP["time"].tolist()
dayobsP = [datetime.strptime(date, "%m/%d/%Y") for date in datesobsP]

datescalP = calN["Date"].tolist()
daycalP = [datetime.strptime(date, "%d/%m/%Y") for date in datescalP]

tl1_P = obsP["solp kg"].tolist()

cal_tl1_P = calP["Value"].tolist()

# %%

fig, ax = plt.subplots()
plt.grid(linestyle = '--')
plt.plot(daycalP, cal_tl1_P, label = "Phosphorus after Calibration", color = "darkcyan")
plt.scatter(dayobsP, tl1_P, label = "Observed Phosphorus", color ="purple")
plt.title("Phosphorus")
plt.ylabel("Phosphorus (kg/day)")
plt.xlabel("Day")
plt.legend()
ax.tick_params(axis='x', labelrotation=45)
plt.show()


# %%

##### Interventions Discharge 

interQ= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Exports from InOut\Discharge All Interventions (with Inlet).csv")
print(interQ.dtypes)

# %%
datesinterQ = interQ["date"].tolist()
dayinterQ = [datetime.strptime(date, "%m/%d/%Y") for date in datesinterQ]

flo_og = interQ["og flo"].tolist()

flo_fs1 = interQ["fs1 flo"].tolist()

flo_fs2 = interQ["fs2 flo"].tolist()

flo_fs3 = interQ["fs3 flo"].tolist()

flo_gw1 = interQ["gw1 flo"].tolist()

flo_gw2 = interQ["gw2 flo"].tolist()

flo_gw3 = interQ["gw3 flo"].tolist()

# %%

fig, ax = plt.subplots()
plt.grid(linestyle = '--')
plt.plot(daycalQ, cal_tl1_q, label = "Calibrated Discharge", color = "tomato")
plt.plot(dayinterQ, flo_gw1, label = "GW1 Discharge", color = "peachpuff")
plt.plot(dayinterQ, flo_gw2, label = "GW2 Discharge", color = "sandybrown")
plt.plot(dayinterQ, flo_gw3, label = "GW3 Discharge", color = "peru")
plt.plot(dayinterQ, flo_fs1, label = "FS1 Discharge", color = "lightcoral")
plt.plot(dayinterQ, flo_fs2, label = "FS2 Discharge", color = "indianred")
plt.plot(dayinterQ, flo_fs3, label = "FS3 Discharge", color = "brown")
plt.title("Discharge by Intervention")
plt.ylabel("Discharge (m^3/sec)")
plt.xlabel("Date")
plt.legend()
ax.tick_params(axis='x', labelrotation=45)
plt.show()


# %%

#### Interventions Nitrogen 

interN= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Exports from InOut\ORGN All Interventions (with Inlet).csv")
print(interN.dtypes)

# %%
datesinterN = interN["date"].tolist()
dayinterN = [datetime.strptime(date, "%m/%d/%Y") for date in datesinterN]

orgn_og = interN["orgn og"].tolist()

orgn_fs1 = interN["orgn fs1"].tolist()

orgn_fs2 = interN["orgn fs2"].tolist()

orgn_fs3 = interN["orgn fs3"].tolist()

orgn_gw1 = interN["orgn gw1"].tolist()

orgn_gw2 = interN["orgn gw2"].tolist()

orgn_gw3 = interN["orgn gw3"].tolist()

# %%

fig, ax = plt.subplots()
plt.grid(linestyle = '--')
plt.plot(daycalN, cal_tl1_N, label = "Nitrogen after Calibration", color = "darkgoldenrod")
plt.plot(dayinterN, orgn_fs1, label = "FS1 Nitrogen", color = "lemonchiffon")
plt.plot(dayinterN, orgn_fs2, label = "FS2 Nitrogen", color = "gold")
plt.plot(dayinterN, orgn_fs3, label = "FS3 Nitrogen", color = "goldenrod")
plt.plot(dayinterN, orgn_gw1, label = "GW1 Nitrogen", color = "blanchedalmond")
plt.plot(dayinterN, orgn_gw2, label = "GW2 Nitrogen", color = "navajowhite")
plt.plot(dayinterN, orgn_gw3, label = "GW3 Nitrogen", color = "orange")
plt.title("Nitrogen by Intervention")
plt.ylabel("Organic Nitrogen (kg/day)")
plt.xlabel("Date")
plt.legend()
ax.tick_params(axis='x', labelrotation=45)
plt.show()


# %%
#### Interventions Phosphorus 

interP= pd.read_csv(r"C:\Users\maryp\Downloads\Data CEE Project\FINAL EXPORTS\Exports from InOut\SOLP All Interventions (with Inlet).csv")
print(interP.dtypes)

# %%
datesinterP = interP["date"].tolist()
dayinterP = [datetime.strptime(date, "%m/%d/%Y") for date in datesinterP]

solp_og = interP["sol og"].tolist()

solp_fs1 = interP["solp fs1"].tolist()

solp_fs2 = interP["solp fs2"].tolist()

solp_fs3 = interP["solp fs3"].tolist()

solp_gw1 = interP["solp gw1"].tolist()

solp_gw2 = interP["solp gw2"].tolist()

solp_gw3 = interP["solp gw3"].tolist()

# %%

fig, ax = plt.subplots()
plt.grid(linestyle = '--')
plt.plot(daycalP, cal_tl1_P, label = "Phosphorus after Calibration", color = "darkcyan")
plt.plot(dayinterP, solp_fs1, label = "FS1 Phosphorus", color = "paleturquoise")
plt.plot(dayinterP, solp_fs2, label = "FS2 Phosphorus", color = "turquoise")
plt.plot(dayinterP, solp_fs3, label = "FS3 Phosphorus", color = "lightseagreen")
plt.plot(dayinterP, solp_gw1, label = "GW1 Phosphorus", color = "honeydew")
plt.plot(dayinterP, solp_gw2, label = "GW2 Phosphorus", color = "aquamarine")
plt.plot(dayinterP, solp_gw3, label = "GW3 Phosphorus", color = "mediumaquamarine")
plt.title("Phosphoris by Intervention")
plt.ylabel("Soluble Phosphorus (kg/day)")
plt.xlabel("Date")
plt.legend()
ax.tick_params(axis='x', labelrotation=45)
plt.show()







