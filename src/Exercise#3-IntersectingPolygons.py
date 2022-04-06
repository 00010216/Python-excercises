"""
This solution doesn't apply for Polygons with ring cases, in that case
the holes coordinates should be specified when creating a polygon
like this gm.Polygon(exterior coordinate,[interior coordinate or holes])
and uncomment the verification of a valid polygon
"""
import numpy as np
from shapely import geometry as gm
import random as rdm

#How many polygons intersect with each polygon
#Each polygon area
def comparepolygons(polygons_array):
    index = -1               #polygons index in the array
    polygons_intersected = 0 #how many polygons a polygon intersects
    iterations = 0           #to control if each polygon was compared with all the other polygons

    for i in polygons_array:
        index += 1
        polygon_a = gm.Polygon(i)

        """if not polygon_a.is_valid:
            print("(Polygon:"+"     "+str(index) + ")")
            print("Is not a valid polygon")
            continue
        """
        for j in polygons_array:
            if(np.array_equal(i,j)): #condition to not verify intersections with itself 
                continue
            iterations += 1 
            polygon_b = gm.Polygon(j)

            """if not polygon_b.is_valid: 
                continue
            """
            if(polygon_a.intersects(polygon_b)):
                polygons_intersected += 1
            if(iterations == (len(polygons_array)-1)): 
                print("(Polygon:"+"     "+ str(index)+")")
                print("Area:",polygon_a.area)
                print("Intersects:", polygons_intersected)
                polygons_intersected = 0 
                iterations = 0 

#Main code  
polygons = np.random.randint(0,200,(10,rdm.randint(3,6),2))
comparepolygons(polygons)