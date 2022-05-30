class PokemonSTAT():
    def tothpReturnWithParams(hp,iv,ev,level):
        temphp = ((2*hp+iv+(ev/4)*level) / 100) + level + 10
        if temphp > 510:
            temphp = 510

        else:
            temphp = temphp

        tothp = "{:.2f}".format(temphp)

        return tothp

    def totatkReturnWithParams(baseatk,iv_atk,ev_atk,level,nature):
        tempatk = ((2*baseatk+iv_atk+(ev_atk/4)*level)+5)

        if nature == "Lonely" or nature == "Adamant" or nature == "Naughty" or nature == "Brave":
            tempatk = tempatk * 1.1

        elif nature == "Bold" or nature == "Modest" or nature == "Calm" or nature == "Timid":
            tempatk = tempatk * 0.9

        if tempatk > 510:
            tempatk = 510

        totatk = "{:.2f}".format(tempatk)

        return totatk

    def totdefReturnWithParams(basedef,iv_def,ev_def,level,nature):
        tempdef = ((2*basedef+iv_def+(ev_def/4)*level)+5)

        if nature == "Bold" or nature == "Impish" or nature == "Lax" or nature == "Relaxed":
            tempdef = tempdef * 1.1

        elif nature == "Lonely" or nature == "Mild" or nature == "Gentle" or nature == "Hasty":
            tempdef = tempdef * 0.9

        if tempdef > 510:
            tempdef = 510

        totdef = "{:.2f}".format(tempdef)

        return totdef

    def totsatkReturnWithParams(basesatk,iv_satk,ev_satk,level,nature):
        tempsatk = ((2*basesatk+iv_satk+(ev_satk/4)*level)+5)

        if nature == "Modest" or nature == "Mild" or nature == "Rash" or nature == "Quiet":
            tempsatk = tempsatk * 1.1    

        elif nature == "Adamant" or nature == "Impish" or nature == "Careful" or nature == "Jolly":
            tempsatk = tempsatk * 0.9

        if tempsatk > 510:
            tempsatk = 510

        totsatk = "{:.2f}".format(tempsatk)

        return totsatk

    def totsdefReturnWithParams(basesdef,iv_sdef,ev_sdef,level,nature):
        tempsdef = ((2*basesdef+iv_sdef+(ev_sdef/4)*level)+5)

        if nature == "Calm" or nature == "Gentle" or nature == "Careful" or nature == "Sassy":
            tempsdef = tempsdef * 1.1

        elif nature == "Naughty" or nature == "Lax" or nature == "Rash" or nature == "Naive":
            tempsdef = tempsdef * 0.9

        if tempsdef > 510:
            tempsdef = 510

        totsdef = "{:.2f}".format(tempsdef)

        return totsdef

    def totspdReturnWithParams(basespd,iv_spd,ev_spd,level,nature):
        tempspd = ((2*basespd+iv_spd+(ev_spd/4)*level)+5)

        if nature == "Timid" or nature == "Hasty" or nature == "Jolly" or nature == "Naive":
            tempspd = tempspd * 1.1

        elif nature == "Brave" or nature == "Relaxed" or nature == "Quiet" or nature == "Sassy":
            tempspd = tempspd * 0.9
        
        if tempspd > 510:
            tempspd = 510

        totspd = "{:.2f}".format(tempspd)

        return totspd
        
    

