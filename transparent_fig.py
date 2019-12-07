import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
from matplotlib.path import Path
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.io.shapereader import Reader
import matplotlib as mpl
from cartopy.mpl.patch import geos_to_path
from shapely.geometry import Point, Polygon
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter


shp = Reader('/Users/fhan/Downloads/china_shp/country/country1.shp')
f1 = xr.open_dataset('/Users/fhan/Downloads/ERA-20C-yearmean-1926~1970.nc')
u1 = f1['uv10']
lat = u1.coords['latitude']
lon = u1.coords['longitude']

u1_avg = u1.mean(dim='time')
lev = np.linspace(0,5,101)
#lev = np.arange(0,4.5,0.25)

fig = plt.figure(figsize=(9,6),dpi=600)

proj = ccrs.PlateCarree() #可利投影,适用于等经纬度格点资料，地图上画两点连起来是直线

#proj =ccrs.Geodetic() #大地投影 地图上两点直线是大圆
proj1 = ccrs.LambertConformal(central_longitude=105, central_latitude=90,standard_parallels=(25, 45))#,false_easting=400000, false_northing=400000)#

ax = fig.add_subplot(111,projection=proj1)    #只需要在此设置地图的投影方式
region = [70,140,15,60]
ax.set_extent(region,crs = proj)
#ax.set_position([0,0,1,1])

#经纬度刻度线方法一
# ax.set_xticks(np.arange(70,130+10,20),crs = proj)
# ax.set_yticks(np.arange(15,60+5,10),crs=proj)
# lon_formatter = LongitudeFormatter(zero_direction_label=True)
# lat_formatter = LatitudeFormatter()
# ax.xaxis.set_major_formatter(lon_formatter)
# ax.yaxis.set_major_formatter(lat_formatter)
# ax.tick_params(labelsize=15)       # NOTE: 不是fontsize， 是labelsize

# to get the effect of having just the states without a map "background"
# turn off the outline and background patches
ax.background_patch.set_visible(False)   #设置图片背景为不可见
ax.outline_patch.set_visible(False)      #设置图片外面的outline方框


#ax.contourf中的transform 代表数据的投影方式
contourf = ax.contourf(lon,lat,u1_avg,lev,cmap='Blues',transform=proj,extend='both')

countries = shp.records()
cn_multipoly, = [country.geometry for country in countries
                 if country.attributes['CNTRY_NAME'] == 'China']  # 选择地图属性下'NAME'属性里名字是'China'的一条多边形

paths = []
for i in range(len(cn_multipoly)):
    cn_geom, = geos_to_path(cn_multipoly.geoms[i])
    paths.append(cn_geom)

path = Path.make_compound_path(*paths)
for collection in contourf.collections:
    collection.set_clip_path(path, proj._as_mpl_transform(ax))

# 白化等值线上的刻度标签
# contour = ax.contour(lon,lat,u1_avg,lev,cmap='Blues',transform=proj,extend='both')
# cn_label = plt.clabel(contour,inline=1,fontsize=10,fmt="%.fr")
# if cn_label:
#     clip_map_shapely = Polygon(path.vertices)
#     for text_object in cn_label:
#         if not clip_map_shapely.contains(Point(text_object.get_position())):
#             text_object.set_visible(False)

ax.add_geometries(cn_multipoly, crs=proj, edgecolor='black', linewidths=1, facecolor='none', zorder=10, alpha=0.8)

#设置地图网格线
# ax.gridlines(color="black", linestyle="--")
# ax.gridlines(color='gray', linestyle = 'dotted', xlocs = np.arange(70,140+20,20), ylocs = np.arange(15,65+10,10))

#设置 colorbar
# fig.colorbar(contourf, format='%.1f',shrink=0.8,ax=ax)

#设置子图，南海区域
# sub_ax = fig.add_axes([0.60, 0.20, 0.17, 0.2],projection=proj)
# # Add ocean, land, rivers and lakes
# # Set figure extent
# sub_ax.set_extent([105, 125, 0, 25],crs=proj)
# sub_ax.add_geometries(shp.geometries(),crs=proj,edgecolor='black', linewidths=1,facecolor='none',zorder=10,alpha=0.8)

#设置图片透明度
alpha = 0
fig.patch.set_alpha(alpha)
ax.patch.set_alpha(alpha)
fig.savefig('transparent.png',bbox_inches = 'tight',transparent=True) #transparent 透明
