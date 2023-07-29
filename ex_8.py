import pylab
from matplotlib import cm
import numpy


def makeData():
    x = numpy.arange(-10, 10, 0.1)
    y = numpy.arange(-10, 10, 0.1)
    xgrid, ygrid = numpy.meshgrid(x, y)
    zgrid = numpy.sin(xgrid) * numpy.sin(ygrid) / (xgrid * ygrid)
    return xgrid, ygrid, zgrid


x, y, z = makeData()

fig = pylab.figure()
axes = fig.add_subplot(projection='3d')
axes.plot_surface(x, y, z, rstride=5, cstride=1, cmap=cm.jet)
pylab.savefig('figure_with_legend_ex_8.png')
pylab.show()
