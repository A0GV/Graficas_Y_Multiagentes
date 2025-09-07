# Enhanced car-following logic

def find_leader_ahead(cars, car):
    # Logic to find the leader car ahead of the current car
    for other_car in cars:
        if other_car.position > car.position:
            return other_car
    return None


def calculate_safe_velocity(leader, current_car):
    # Logic to calculate a safe velocity based on the leader's speed
    safe_velocity = leader.velocity - (leader.position - current_car.position) / 2
    return max(safe_velocity, 0)


# Existing car movement logic
for car in cars:
    leader = find_leader_ahead(cars, car)
    if leader:
        safe_velocity = calculate_safe_velocity(leader, car)
        car.velocity = safe_velocity
        car.position += round(car.velocity)  # Ensure movement is to integer position
    else:
        # Logic for when there is no leader ahead
        car.position += round(car.velocity)  # Ensure movement is to integer position
