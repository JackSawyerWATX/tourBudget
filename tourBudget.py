# TODO: Define the budget for the cultural tour
# TODO: Define the cost associated with each city visit
cultural_tour = 3600
tour_cost = {"Bejing": 800, "Manila": 700, "Seoul": 900, "New Dheli": 1000}

# TODO: Initialize the total amount spent and the list of chosen cities
total_spent = 0
cultural_cities = []

# TODO: Use a while loop to selectively add cities to the tour list based on the budget
# Inside the loop:
    # TODO: Retrieve a city and its associated cost
    # TODO: Check if adding this city would exceed your budget
        # TODO: If not, update the total spent and add the city to your list
while total_spent < cultural_tour and tour_cost:
    city, cost = tour_cost.popitem()
    if total_spent + cost <= cultural_tour:
        total_spent += cost
        cultural_cities.append(city)

# TODO: Print the list of cities chosen for the cultural tour
print("The cities selected for the local tour are:", cultural_cities)
