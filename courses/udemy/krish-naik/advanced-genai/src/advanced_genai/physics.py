def calculate_advanced_gravity(mass: float, constant: float = 9.81) -> float:
    \"\"\"
    Calculates the downward force of gravity with an adjustable constant.

    Args:
        mass (float): The mass of the object in kilograms.
        constant (float): The gravitational constant to use (default 9.81).

    Returns:
        float: The force in Newtons.
    \"\"\"
    return mass * constant
