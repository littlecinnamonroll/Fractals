import numpy as np
import matplotlib.pyplot as plt
from hilbert import decode, encode
from PIL import Image
import math
#============================== Uploading the image
im = Image.open('roomie.jpg') # Can be many different formats.
pix = im.load()
imwidth,imheight = im.size
#print(pix[0,0])  # Get the RGBA Value of the a pixel of an image

#============================== Getting the curve
squaresize = 8 #side of the square in bits
bits = 2*squaresize-1
array = np.array(list(range(1,(2**(bits+1)))))
# Turn an ndarray of Hilber integers into locations.
# first no. is the number of dimensions, second is the number of bits per dimension
#print(array)
locs = decode(array, 2, bits)
points = list(locs)
#print(points)
xpoints = [points[k][0] for k in range(len(points))]
ypoints = [points[k][1] for k in range(len(points))]
#scale the coordinates so we get the entire image in colour
#also adjust so final image isn't upside down
xpix = [imwidth-1-math.floor(xpoints[k]*imwidth/(2**squaresize)) for k in range(len(xpoints))]
ypix = [imheight-1-math.floor(ypoints[k]*imheight/(2**squaresize)) for k in range(len(ypoints))]
#print(ypix)

#print(locs)
plt.figure()
#plt.plot(range(len(array)), list(locs))
for k in range(len(points)-1):
    plt.plot(xpoints[k:k+2],ypoints[k:k+2],color=[ int(pix[xpix[k],ypix[k]][m])/255 for m in range(3)], linewidth=0.8)
    #print("done")
plt.show()
#==============================
