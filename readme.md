# Have Fun!!!
### [中国地图、白化](https://github.com/fhhan/eg/blob/master/cartopy_makeout.py)
```python
# maskout 中国地图
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
 ```   

---
![图片](https://github.com/fhhan/eg/blob/master/China🇨🇳.png)

### [绘制箭头](https://github.com/fhhan/eg/blob/master/my_quiver.py)
