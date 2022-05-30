import pokemon_script_1_stat as tothp
import pokemon_script_1_stat as totatk
import pokemon_script_1_stat as totdef
import pokemon_script_1_stat as totsatk
import pokemon_script_1_stat as totsdef
import pokemon_script_1_stat as totspd
import pokemon_script_2_ev as evatk
import pokemon_script_2_ev as evdef
import pokemon_script_2_ev as evsatk
import pokemon_script_2_ev as evsdef
import pokemon_script_2_ev as evspd

# Nature Library
nature_list = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish", "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"]


print("1. Stat Calculator \n2. EV Calculator")
ch = int(input("Select Mode: "))
match ch:
        
    case 1:
        print("1. Pokemon's HP \n2. Pokemon's Other Stat")
        statch = input(("Select the Function that will be used: "))
        while statch != "1" and statch != "2":
            print("Invalid input, Try again!")
            statch = input(("Select the Function that will be used: "))


        if statch == "1":
            level = int(input("\nLEVEL: "))
            while level > 100:
                print("Maxium value is 100 only")
                level = input(input("LEVEL: "))
            hp = int(input("HP: "))

            iv = int(input("IV: "))
            while iv > 31:
                print("Given value is between 0 - 31 only")
                iv = int(input("IV: "))

            ev = int(input("EV: "))
            while ev > 255:
                print("Given value is between 0 - 255 only")
                ev = int(input("EV: "))

            print("\n")
            print("HP =", tothp.PokemonSTAT.tothpReturnWithParams(hp,iv,ev,level), end='\n\n')
            print("\nSystem Terminated")


        elif statch == "2":
            poke = input("\nEnter your Pokemon Name: ")
            level = int(input("Enter your Pokemon Level: "))
            # NATURE
            nature = input("Nature: ")
            while nature not in nature_list:
                print("\nIncorrect Pokemon Nature, Try again")
                nature = input("Nature: ")
            # ATK
            baseatk = int(input("\nATK: "))
            iv_atk = int(input("IV: "))
            while iv_atk > 31:
                print("IV value should be between 0 and 31 only.")
                iv_atk = int(input("IV: "))
            
            ev_atk = int(input("EV: "))
            while ev_atk > 255:
                print("EV value should be between 0 and 255 only.")
                ev_atk = int(input("EV: "))
            # DEF
            basedef = int(input("\nDEF: "))
            iv_def = int(input("IV: "))
            while iv_def > 31:
                print("IV value should be between 0 and 31 only.")
                iv_def = int(input("IV: "))
            
            ev_def = int(input("EV: "))
            while ev_def > 255:
                print("EV value should be between 0 and 255 only.")
                ev_def = int(input("EV: "))
            # SP ATK
            basesatk = int(input("\nSP. ATK: "))
            iv_satk = int(input("IV: "))
            while iv_satk > 31:
                print("IV value should be between 0 and 31 only.")
                iv_satk = int(input("IV: "))
            
            ev_satk = int(input("EV: "))
            while ev_satk > 255:
                print("EV value should be between 0 and 255 only.")
                ev_satk = int(input("EV: "))
            # SP DEF
            basesdef = int(input("\nSP. DEF: "))
            iv_sdef = int(input("IV: "))
            while iv_atk > 31:
                print("IV value should be between 0 and 31 only.")
                iv_sdef = int(input("IV: "))
            
            ev_sdef = int(input("EV: "))
            while ev_sdef > 255:
                print("EV value should be between 0 and 255 only.")
                ev_sdef = int(input("EV: "))
            # SPD
            basespd = int(input("\nSPD: "))
            iv_spd = int(input("IV: "))
            while iv_spd > 31:
                print("IV value should be between 0 and 31 only.")
                iv_spd = int(input("IV: "))
            
            ev_spd = int(input("EV: "))
            while ev_spd > 255:
                print("EV value should be between 0 and 255 only.")
                ev_spd = int(input("EV: "))

            
            print("\n")
            print("Pokemon", poke, "a Lvl.", level, "with", nature, "nature, Overall Stats:")
            # Total
            print("\nATK =", totatk.PokemonSTAT.totatkReturnWithParams(level,baseatk,iv_atk,ev_atk,nature), end='\n\n')
            print("DEF =", totdef.PokemonSTAT.totdefReturnWithParams(level,basedef,iv_def,ev_def,nature), end='\n\n')
            print("SP. ATK =", totsatk.PokemonSTAT.totsatkReturnWithParams(level,basesatk,iv_satk,ev_satk,nature), end='\n\n')
            print("SP. DEF =", totsdef.PokemonSTAT.totsdefReturnWithParams(level,basesdef,iv_sdef,ev_sdef,nature), end='\n\n')
            print("SPD =", totspd.PokemonSTAT.totspdReturnWithParams(level,basespd,iv_spd,ev_spd,nature), end='\n\n')
            print("\nSystem Terminated")
    
    case 2:
        print("\n")
        base = int(input("ACTUAL STAT: "))
        stat = int(input("INCREASE STAT: "))
        level = int(input("TARGET LEVEL: "))
        while level > 100:
            print("Maxium value is 100 only")
            level = input(input("TARGET LEVEL: "))
        nature = input("NATURE: ")
        while nature not in nature_list:
            print("\nIncorrect Pokemon Nature, Try again")
            nature = input("NATURE: ")
        iv = int(input("IV: "))
        ev = int(input("EV: "))
        
        # Total
        print("\nEFFORT VALUES NEEDED IN:")
        print("\nATK is =", evatk.PokemonEV.evatkReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("DEF is =", evdef.PokemonEV.evdefReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("SP ATK is =", evsatk.PokemonEV.evsatkReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("SP DEF is =", evsdef.PokemonEV.evsdefReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("SPD is =", evspd.PokemonEV.evspdReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("\nSystem Terminated")

    case default:
        print("Invalid Input, System Terminated.")




