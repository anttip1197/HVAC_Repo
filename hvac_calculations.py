def heating_power(flow_rate, temp_diff):
    """
    Calculate heating power in watts.
    
    Parameters:
    flow_rate : float : flow rate in cubic meters per second
    temp_diff : float : temperature difference in degrees Celsius
    
    Returns:
    float : heating power in watts
    """
    specific_heat = 4184  # specific heat of water in J/(kg*K)
    density_water = 1000  # kg/m^3
    power = flow_rate * density_water * specific_heat * temp_diff
    return power


def cooling_power(flow_rate, temp_diff):
    """
    Estimate cooling power in watts.
    
    Parameters:
    flow_rate : float : flow rate in cubic meters per second
    temp_diff : float : temperature difference in degrees Celsius
    
    Returns:
    float : cooling power in watts
    """
    # Assume similar calculations as heating, but negative temp_diff for cooling
    return heating_power(flow_rate, -temp_diff)


def pressure_drop(length, diameter, flow_rate, viscosity):
    """
    Calculate pressure drop in pipes using the Darcy-Weisbach equation.
    
    Parameters:
    length : float : length of the pipe in meters
    diameter : float : diameter of the pipe in meters
    flow_rate : float : flow rate in cubic meters per second
    viscosity : float : dynamic viscosity of the fluid in Pa.s
    
    Returns:
    float : pressure drop in Pascals
    """
    # Calculate the Reynolds number
    area = 3.14159 * (diameter / 2) ** 2
    velocity = flow_rate / area
    density = 1000  # Assume density of water in kg/m^3
    reynolds_number = (density * velocity * diameter) / viscosity
    # Calculate friction factor using the Darcy-Weisbach equation
    if reynolds_number < 2000:
        # Laminar flow
        friction_factor = 64 / reynolds_number
    else:
        # Turbulent flow Poiseuille approximation
        friction_factor = 0.3164 / (reynolds_number ** 0.25)
    pressure_drop = friction_factor * (length / diameter) * (density * velocity ** 2) / 2
    return pressure_drop
