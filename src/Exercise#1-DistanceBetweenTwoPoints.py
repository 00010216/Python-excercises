import argparse
import math

#arg parse get arguments from command line
def parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('LAT1', type = float, help = "a float for the latitude 1 in degrees")
	parser.add_argument('LON1', type = float, help = "a float for the longitude 1 in degrees")
	parser.add_argument('LAT2', type = float, help = "a float for the latitude 2 in degrees")
	parser.add_argument('LON2', type = float, help = "a float for the longitude 2 in degrees")
	args = parser.parse_args()
	return (args)

#Returns the distance between the two points
def getDistance(lat1, lon1, lat2, lon2):

	#latitudes and longitudes difference
	lat_d = math.radians(lat2 - lat1)
	lon_d = math.radians(lon2 - lon1)

	#conversion to radians
	lat1 = math.radians(lat1)
	lat2 = math.radians(lat2)

	#Earth Radius (km)
	r = 6371.000 

	# haversine function
	h = ((math.sin((lat_d)/2))**2) + math.cos(lat1)*math.cos(lat2)*((math.sin((lon_d)/2))**2) 

	#Distance
	d = 2*r*math.asin(math.sqrt(h))

	return(d)

#Main code  
args = parser()
distance = getDistance(args.LAT1, args.LON1,args.LAT2, args.LON2)
print(distance)