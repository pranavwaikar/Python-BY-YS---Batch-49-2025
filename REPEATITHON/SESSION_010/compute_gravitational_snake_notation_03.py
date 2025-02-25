mass_of_object_1_in_kgs_pw_3 = float(input('Enter mass of object 1 in kgs:'))
mass_of_object_2_in_kgs_pw_3 = float(input('Enter mass of object 2 in kgs:'))
distance_between_objects_in_meters_pw_3 = float(input('Enter distance between objects in meters:'))
universal_constant_of_gravitation_pw_3 = 6.67 * 10 ** -11
gravitational_force_of_attraction_pw_3 = (universal_constant_of_gravitation_pw_3 * mass_of_object_1_in_kgs_pw_3 *
                                     mass_of_object_2_in_kgs_pw_3) / (distance_between_objects_in_meters_pw_3 ** 2)
print('Force of attracition:', gravitational_force_of_attraction_pw_3, 'Newton')
