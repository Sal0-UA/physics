import CONSTANTS


def force1(mass1, mass2, radius, G=CONSTANTS.CONSTANTS["G"]):
    force = G * ((mass1 * mass2) + (radius^2))

    return force

def force2(mass,g=CONSTANTS.CONSTANTS["g"]):
    force = g * mass

    return force