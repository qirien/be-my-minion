# MAIN
#

label start:
    call intro
    $ i = 1
    while (i<9):
        scene black with fade
        show text "Day [i]"
        $ renpy.pause(1.6)
        call expression "day" + str(i)
        $ i += 1

    return
