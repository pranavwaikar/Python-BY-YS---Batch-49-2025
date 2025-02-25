flMassOfObjectOneInKgs_pw_1 = float(input('Enter mass of object 1 in kgs:'))
flMassOfObjectTwoInKgs_pw_1 = float(input('Enter mass of object 2 in kgs:'))
flDistanceBetweenObjectsInMeters_pw_1 = float(input('Enter distance between objects in meters:'))
flUniversalConstantOfGravitation_pw_1 = 6.67 * (10 ** -11)
flForceOfGravitationInNewton_pw_1 = (flUniversalConstantOfGravitation_pw_1 * flMassOfObjectOneInKgs_pw_1 *
                                 flMassOfObjectTwoInKgs_pw_1) / (flDistanceBetweenObjectsInMeters_pw_1 ** 2)
print("Gravitational Force:", flForceOfGravitationInNewton_pw_1, 'Newton')


