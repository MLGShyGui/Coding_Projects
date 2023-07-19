# This program finds the cheapest shipping method given the package weight. Premium shipping is not properly implimented yet.
weight = int(input("Please enter the weight of your package: "))

ground_cost = 0
drone_cost = 0
premium = 125
# Ground Shipping
if weight <= 2:
  ground_cost = (weight * 1.5) + 20
elif weight > 2 and weight <=6:
  ground_cost = (weight * 3) + 20
elif (weight > 6) and (weight <=10):
  ground_cost = (weight * 4) + 20
else:
  ground_cost = (weight * 4.75) + 20

# Drone Shipping
if weight <= 2:
  drone_cost = (weight * 4.5)
elif weight > 2 and weight <=6:
  drone_cost = (weight * 9)
elif (weight > 6) and (weight <=10):
  drone_cost = (weight * 12)
else:
  drone_cost = (weight * 14.25)

if drone_cost > ground_cost:
  print("Ground shipping is cheapest at ${:,.2f}".format(ground_cost))
elif ground_cost == drone_cost:
  print("Both Ground and Drone shipping cost ${:,.2f}".format(drone_cost))
else:
  print("Drone shipping is cheapest at ${:,.2f}".format(drone_cost))
