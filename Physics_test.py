train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
 
# Write your code below: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  print(c_temp)
  return c_temp
f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = (c_temp) * (9/5) + 32
  print(f_temp)
  return f_temp
c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  train_force = mass * acceleration
  return train_force
  print(train_force)
  print("The GE train supplies {} Newtons of force".format(train_force))
train_force = get_force(train_mass, train_acceleration)
def get_energy(mass, c = 3*10*8):
  return mass * (c*c)
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies {} Joules.".format(bomb_energy))

def get_work(mass, acceleration, distance):
  return get_force(train_mass, train_acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does {0} Jules of work over {1} meters.".format(train_work, train_distance))
