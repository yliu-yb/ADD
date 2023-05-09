import xarray as xr
import os

os.chdir("D:\code\zhou")

ds_day = xr.open_dataset("data/g4.timeAvgMap.MOD11C3_006_LST_Day_CMG.20000101-20200229.180W_81S_180E_81N (1).nc")
ds_night = xr.open_dataset("data/g4.timeAvgMap.MOD11C3_006_LST_Night_CMG.20000101-20200229.180W_81S_180E_81N (1).nc")

ds_day['MOD11C3_006_LST_Day_CMG'] = ds_day.MOD11C3_006_LST_Day_CMG - 273.15
ds_day['MOD11C3_006_LST_Night_CMG'] = ds_night.MOD11C3_006_LST_Night_CMG - 273.15
ds_day['MOD11C3_006_LST_Day_Night_CMG'] = (ds_day.MOD11C3_006_LST_Day_CMG + ds_day.MOD11C3_006_LST_Night_CMG) * 0.5
ds_day.to_netcdf("./data/g4.timeAvgMap.MOD11C3_006_LST_Day_Night_CMG.20000101-20200229.180W_81S_180E_81N.nc")