
'''
        if testingStatus == 1:
            gaugesweep(rpmState, 50)
            gaugesweep(egtState, 19)
            gaugesweep(coolantState, 19)
            gaugesweep(boostState, 19)
            gaugesweep(oilPressureState, 19)
        else:
            continue'''

'''
        rpmState += direction # always move, in whichever direction

        # figure out if you need to change direction
        # Note that these ifs simply won't trigger until it's time to
        # change.
        if rpmState == 50:
            direction = -1
        elif rpmState == 0:
            direction = 1
    #elif
     #       direction = 0'''


#        egtState += direction
#        if egtState == 19:
#            direction = -1
#        elif egtState == 1:
#            direction = 1
#        if rpmState < 19:
#            rpmState += 1
#        else:
#            rpmState = 0

'''
        if egtState < 19:
            egtState += 1
        else:
            egtState = 0


        if boostState < 19:
            boostState += 1
        else:
            boostState = 0

        if coolantState < 19:
            coolantState += 1
        else:
            coolantState = 0

        if oilPressureState < 19:
            oilPressureState += 1
        else:
            oilPressureState = 0

        if speedTen < 9:
#            pygame.time.wait(500)
            speedTen += 1
        else:
            speedTen = 0

        if speedOne < 9:
            speedOne += 1
        else:
            speedOne = 0

        if fuelState >= 70:
            fuelState -= 1'''


   # rpmState = 50

   # if testingStatus == 1:
   #     if rpmState > 50:
    #    rpmState -= 1

#    if testingStatus == 1:
#        if rpmState < 50:
#            rpmState += 1
#        elif rpmState > 0:
#            rpmState = 0



   # rpmState = 0
    #    if rpmState > 50: rpmState = 0
    #        if rpmState == 50:
    #           rpmState == 0


def testing_status(sweepcount):
    global rpm_status
    global direction
    rpm_sweep = 0
    rpm_status = rpm_sweep
    rpm_sweep += direction
    sweepcount = sweepcount
    if rpm_sweep == 50:
        rpm_sweep -= 1
        direction = -1
        sweepcount = +1
    elif rpm_sweep == 0:
        rpm_sweep += 1
        direction = 1
#    pygame.display.update()