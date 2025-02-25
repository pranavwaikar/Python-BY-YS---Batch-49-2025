flMassOfObjectOneInKgs_pw_3 = float(input('Enter mass of object 1 in kgs:'))
flMassOfObjectTwoInKgs_pw_3 = float(input('Enter mass of object 2 in kgs:'))
flDistanceBetweenObjectsInMeters_pw_3 = float(input('Enter distance between objects in meters:'))
flUniversalConstantOfGravitation_pw_3 = 6.67 * (10 ** -11)
flForceOfGravitationInNewton_pw_3 = (flUniversalConstantOfGravitation_pw_3 * flMassOfObjectOneInKgs_pw_3 *
                                 flMassOfObjectTwoInKgs_pw_3) / (flDistanceBetweenObjectsInMeters_pw_3 ** 2)
print("Gravitational Force:", flForceOfGravitationInNewton_pw_3, 'Newton')


