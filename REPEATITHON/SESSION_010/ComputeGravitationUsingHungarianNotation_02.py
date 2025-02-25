flMassOfObjectOneInKgs_pw_2 = float(input('Enter mass of object 1 in kgs:'))
flMassOfObjectTwoInKgs_pw_2 = float(input('Enter mass of object 2 in kgs:'))
flDistanceBetweenObjectsInMeters_pw_2 = float(input('Enter distance between objects in meters:'))
flUniversalConstantOfGravitation_pw_2 = 6.67 * (10 ** -11)
flForceOfGravitationInNewton_pw_2 = (flUniversalConstantOfGravitation_pw_2 * flMassOfObjectOneInKgs_pw_2 *
                                 flMassOfObjectTwoInKgs_pw_2) / (flDistanceBetweenObjectsInMeters_pw_2 ** 2)
print("Gravitational Force:", flForceOfGravitationInNewton_pw_2, 'Newton')


