import netCDF4 as NC
import datetime
import numpy

import draw

day_data = NC.Dataset("./data/g4.areaAvgTimeSeries.MOD11C3_006_LST_Day_CMG.20000101-20200131.99E_26N_107E_31N.nc")
day_time = day_data["time"]
day_lst = numpy.array(day_data["MOD11C3_006_LST_Day_CMG"]) - 273.15
day_date = [datetime.datetime.utcfromtimestamp(t) for t in day_time]

night_data = NC.Dataset("./data/g4.areaAvgTimeSeries.MOD11C3_006_LST_Night_CMG.20000101-20200131.99E_26N_107E_31N.nc")
night_time = night_data["time"]
night_lst = numpy.array(night_data["MOD11C3_006_LST_Night_CMG"]) - 273.15
night_date = [datetime.datetime.utcfromtimestamp(t) for t in night_time]

draw.DrawLine(day_date, day_lst, night_date, night_lst)

