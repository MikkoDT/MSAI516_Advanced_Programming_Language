import rad_deg_converter as rdc
import numpy as np

angle1 = 90
angle2 = 1.571

angle1 = rdc.deg_to_rad(angle1)
angle2 = rdc.rad_to_deg(angle2)

print("angle1 = ",np.around(angle1,3))
print("angle2 = ",np.around(angle2,3))