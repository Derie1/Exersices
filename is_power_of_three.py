def is_power_of_three(z):
    # power_factor = 0
    if z == 1:
        return True
    while z > 1:
        ostatok = z % 3
        z = z / 3
        # power_factor += 1
        if ostatok != 0:
            return False
        return True
