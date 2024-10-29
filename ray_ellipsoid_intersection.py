# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# Finds the intersection point between a ray and the Earth Reference ellipsoid, if it exists
# Parameters:
# d_l_x: x-component of origin-referenced ray direction
# d_l_y: y-component of origin-referenced ray direction
# d_l_z: z-component of origin-referenced ray direction
# c_l_x: x-component offset of ray origin
# c_l_y: y-component offset of ray origin
# c_l_z: z-component offset of ray origin
# Output:
# Produces the x,y, and z components of the intersection point
#
# Written by Celia Sterthous
# Other contributors: None
#
# See the LICENSE file for the license.
# import Python modules
import math 
import sys # argv
# "constants"
R_E_KM = 6378.137
E_E = 0.081819221456
# helper functions
## function description
# def calc_something(param1, param2):

# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
 print(\
 'Usage: '\
 'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
 )
 exit()
# write script below this line
## quadratic coefficients
A = d_l_x**2.0+d_l_y**2.0+(d_l_z**2/(1-E_E**2))
B = 2.0*(d_l_x*c_l_x+d_l_y*c_l_y+d_l_z*(c_l_z/(1-E_E**2)))
C = c_l_x**2+c_l_y**2+(c_l_z**2/(1-E_E**2))-R_E_KM**2
discriminant = B**2-4*A*C
if discriminant>=0:
   d=(-B-math.sqrt(discriminant))/(2*A)
if d<0:
   d=(-B+math.sqrt(discriminant))/(2*A)

## intersection point calculation
d_l = [d_l_x, d_l_y, d_l_z]
c_l = [c_l_x, c_l_y, c_l_z]
intersection_point = [c_l[0]+d*d_l[0], c_l[1]+d*d_l[1], c_l[2]+d*d_l[2],]
## Print results
print(intersection_point[0])  # x-component of intersection point
print(intersection_point[1])  # y-component of intersection point
print(intersection_point[2])  # z-component of intersection point