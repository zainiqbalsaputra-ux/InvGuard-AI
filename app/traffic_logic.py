def check_violation(vehicle_position, roi):
    """
    Check if vehicle inside restricted area
    """

    if vehicle_position in roi:
        return True

    return False