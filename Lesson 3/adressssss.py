class Adress:

    def __init__(self, index, gorod, ulica, dom, kvartira):
        self.indexs = index
        self.gorods = gorod
        self.ulicas = ulica
        self.doms = dom
        self.vartiras = kvartira

class Mailing:

    to = Adress(67598, "dfasgf", "sdfgjf", 467, 6759)
    froms = Adress(3462545, "sfg", "sfg", 4, 3456)
    coast = 1230
    track = "udvhlsdns1dm" 

    def __init__(self, to, froms, coast, track):
        self.to = to
        self.froms = froms
        self.coast = coast
        self.track = track

        print("Отправление", track, "из", to, "в", froms, ". Стоимость", coast, "рублей." )
        