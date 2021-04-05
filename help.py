import time

class hilfen():


    def horloge(self):
        tim = time.time()
        deltaT = tim - 1617507553.7372708

        annee = 365.24 * 24 * 3600
        jour = 24 * 3600
        heure = 3600
        min = 60
        sec = 1

        a = deltaT // annee
        j = deltaT // jour - deltaT // annee * jour
        h = deltaT // heure - deltaT // jour * heure
        m = deltaT // min - deltaT // heure * min
        s = deltaT // sec - deltaT // min * min

        s += 17
        m += 39
        h += 5
        j += 95
        a += 2021


        if s >= 60:
            m += s // 60
            s -= 60 * (s // 60)
        if m >= 60:
            h += m // 60
            m -= 60 * (m // 60)
        if h >= 60:
            j += h // 24
            h -= 60 * (h // 60)
        if j >= 24:
            a += j // 365
            j -= 24 * (h // 24)

        mo = 0
        listMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ab = 0
        ii = 0
        for i in listMonth:
            ab += i
            if j <= ab:
                mo = ii
                break
            ii += 1

        j = listMonth[ii] - (ab - j)
        liste = [j, h, m, s]
        for i in range(len(liste)):
            if liste[i] < 10:
                liste[i] = f"0{int(liste[i])}"
            else:
                liste[i] = int(liste[i])


        month = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
        return f"{liste[0]} {month[mo]} {int(a)} à {liste[1]} : {liste[2]} et {liste[3]} sec"
