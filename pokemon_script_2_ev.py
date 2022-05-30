class PokemonEV():
    def evatkReturnWithParams(base,stat,level,nature,iv,ev):
        D_temp = ( ( 2 * base * iv + ( ev / 4 ) ) * level / 100)
        if D_temp > 510:
            D = 510
        else:
            D = D_temp
        if nature == "Lonely" or nature == "Adamant" or nature == "Naughty" or nature == "Brave":
            tempatk = ( ( ( ( stat / 1.1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        elif nature == "Bold" or nature == "Modest" or nature == "Calm" or nature == "Timid":
            tempatk = ( ( ( ( stat / 0.9 ) - ( D ) ) * 400 / level ) / 4 ) * 4
        
        else:
            tempatk = ( ( ( ( stat / 1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        evatk = "{:.2f}".format(tempatk)

        return evatk

    def evdefReturnWithParams(base,stat,level,nature,iv,ev):
        D_temp = ( ( 2 * base * iv + ( ev / 4 ) ) * level / 100)
        if D_temp > 510:
            D = 510
        else:
            D = D_temp
        if nature == "Bold" or nature == "Impish" or nature == "Lax" or nature == "Relaxed":
            tempdef = ( ( ( ( stat / 1.1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        elif nature == "Lonely" or nature == "Mild" or nature == "Gentle" or nature == "Hasty":
            tempdef = ( ( ( ( stat / 0.9 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        else:
            tempdef = ( ( ( ( stat / 1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        evdef = "{:.2f}".format(tempdef)

        return evdef

    def evsatkReturnWithParams(base,stat,level,nature,iv,ev):
        D_temp = ( ( 2 * base * iv + ( ev / 4 ) ) * level / 100)
        if D_temp > 510:
            D = 510
        else:
            D = D_temp
        if nature == "Modest" or nature == "Mild" or nature == "Rash" or nature == "Quiet":
            tempsatk = ( ( ( ( stat / 1.1 ) - ( D ) ) * 400 / level ) / 4 ) * 4   

        elif nature == "Adamant" or nature == "Impish" or nature == "Careful" or nature == "Jolly":
            tempsatk = ( ( ( ( stat / 0.9 ) - ( D ) ) * 400 / level ) / 4 ) * 4
        
        else:
            tempsatk = ( ( ( ( stat / 1 ) - ( D ) ) * 400 / level ) / 4 ) * 4
        
        evsatk = "{:.2f}".format(tempsatk)

        return evsatk

    def evsdefReturnWithParams(base,stat,level,nature,iv,ev):
        D_temp = ( ( 2 * base * iv + ( ev / 4 ) ) * level / 100)
        if D_temp > 510:
            D = 510
        else:
            D = D_temp
        if nature == "Calm" or nature == "Gentle" or nature == "Careful" or nature == "Sassy":
            tempsdef = ( ( ( ( stat / 1.1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        elif nature == "Naughty" or nature == "Lax" or nature == "Rash" or nature == "Naive":
            tempsdef = ( ( ( ( stat / 0.9 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        else:
            tempsdef = ( ( ( ( stat / 1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        evsdef = "{:.2f}".format(tempsdef)

        return evsdef

    def evspdReturnWithParams(base,stat,level,nature,iv,ev):
        D_temp = ( ( 2 * base * iv + ( ev / 4 ) ) * level / 100)
        if D_temp > 510:
            D = 510
        else:
            D = D_temp
        if nature == "Timid" or nature == "Hasty" or nature == "Jolly" or nature == "Naive":
            tempspd = ( ( ( ( stat / 1.1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        elif nature == "Brave" or nature == "Relaxed" or nature == "Quiet" or nature == "Sassy":
            tempspd = ( ( ( ( stat / 0.9 ) - ( D ) ) * 400 / level ) / 4 ) * 4
        
        else:
            tempspd = ( ( ( ( stat / 1 ) - ( D ) ) * 400 / level ) / 4 ) * 4
        
        evspd = "{:.2f}".format(tempspd)
        
        return evspd


