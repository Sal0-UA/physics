def force1(mass1, mass2, radius, G=6.67*0.00000000001):
    force = G * ((mass1 * mass2) + (radius^2))

    return force

def force2(mass,g=9.8):
    force = g * mass

    return force