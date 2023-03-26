import pygmt

# Creating a 3-D perspective image
#from https://www.pygmt.org/latest/tutorials/advanced/3d_perspective_image.html

"""
--------note--------
（1）对于国内用户，建议直接使用中科大LUG提供的国内镜像。修改方式为
gmt set GMT_DATA_SERVER https://mirrors.ustc.edu.cn/gmtdata
然后将生成的 gmt.conf 文件复制到GMT用户目录 ~/.gmt (Linux/macOS) 或 C:\\Users\\XXX\\.gmt（Windows）下*
（2）GMT_AUTO_DOWNLOAD 是否允许自动从GMT服务器（由 GMT_DATA_SERVER 控制）下载数据文件到用户目录 ~/.gmt 下。可以取 on 或者 off 
当前版本默认为off，需手动配置为on
源自：https://docs.gmt-china.org/latest/utilities/gdal/
--------note--------
"""

#  Load sample earth relief data
hn_grid = pygmt.datasets.load_earth_relief(resolution="01s", region=[117.10, 117.18, 32.70, 32.78])

fig = pygmt.Figure()

# Sets the view azimuth as -135 degrees, and the view elevation as 30
perspective = [-135, 30]

# Sets a Mercator projection on a 15-centimeter figure
projection = 'M15c'

fig.grdview(
    grid=hn_grid,
    perspective=perspective,
    # Sets the x- and y-axis labels, and annotates the west, south, and east
    frame=["xag", "yag", "WSnE", "zaf+lElevation"],
    projection=projection,
    # Sets the height of the three-dimensional relief at 2.5 centimeters
    zsize="2.5c",
    # Set the surftype to "surface"
    surftype="s",
    # Set the CPT to "geo"
    cmap="geo",
    # drapegrid = [117.14, 32.74],
    plane="ggrey",
    # Set the contour pen thickness to "0.1p"
    contourpen="0.1p",
)

fig.plot(x=117.14, y=32.74, style="a1c", fill="red", pen="white", perspective=perspective, projection = projection)
fig.basemap(
        perspective=True,
        rose="JCL+w5c+l+o2c/0c")

fig.text(perspective=perspective, projection = projection, x=117.14, y=32.74 - 0.003, text="HCEO", font="14p,Helvetica-Bold,black")

fig.colorbar(perspective=perspective, frame=["a50", "x+lElevation", "y+lm"])
fig.savefig('./3D_perspective_image_result.png', dpi = 600)