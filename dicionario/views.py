import unicodedata
from django.shortcuts import render

def gregoport(request):
    raw_data = """
    το αβγό = ovo
    αγαπάω, -ώ = amar
    η αγάπη = o amor
    αγαπημένος, -η, -ο = favorito
    αγαπητός, -ή, -ό = querido
    η αγγελία = propaganda
    η Αγγελική = Angélica
    ο Άγγελος = Angelo
    η Αγγλία = Inglaterra
    αγγλική γλώσσα = inglês (língua)
    αγγλικά = inglês (língua)
    αγγλικός, -ή, -ό = inglês
    Άγγλος, -ίδα = (pessoa) inglês(a)
    το αγγούρι = pepino
    άγιος, -ια, -ία, -ο = santo
    η αγκαλιά = abraço
    η αγκινάρα = alcachofra
    το αγκίστρι = anzol
    η άγκυρα = âncora
    ο άγνωστος = o estranho
    η άγνωστη = a estranha
    άγνωστος, -η, -ο = estranho
    η αγορά = mercado
    αγοράζω = comprar
    το αγόρι = menino
    το άγχος = estresse, ansiedade, preocupação
    ο αγώνας = partida, jogo
    η άδεια = dia de licença do trabalho
    αδειάζω = esvaziar
    αδελφή = irmã
    αδελφός = irmão
    αδερφή = irmã
    αδερφός = irmão
    η αδυναμία = fraqueza
    αδυνατίζω = emagrecer
    αδύνατος, -η, -ο = magro
    το αέριο = gás
    το αεροδρόμιο = aeroporto
    το αεροπλάνο = avião
    η Αθανασία = Athanassia
    η Αθηνά = Athina
    ο αθλητής = o atleta
    η αθλήτρια = a atleta 
    ο αθλητισμός = esporte
    το Αιγαίο (πέλαγος) = o Mar Egeu
    η Αίγινα = Aegina
    η Αίγυπτος = Egito
    Αιγύπτιος, -ια = (pessoa) egípcio(a)
    αιγυπτιακός, -ή, -ό = egípcio
    αιγυπτιακή γλώσσα = egípcia (língua)
    αιγυπτιακά = egípcia (língua)
    η Αιθιοπία = Etiópia
    """

    def shave_marks(txt):
        norm_txt = unicodedata.normalize('NFD', txt)
        shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
        return unicodedata.normalize('NFC', shaved)
    
    data = "var data = ["
    for line in raw_data.splitlines():
        line = line.strip()
        if len(line) > 0:
            data += '"{}",\n'.format(line)

    data += "];"

    
    shaved = "var shaved = ["
    for line in raw_data.splitlines():
        line = line.strip()
        if len(line) > 0:
            shaved += '"{}",\n'.format(shave_marks(line))

    shaved += "];"
    
    return render(request, 'dicionario/gregoport.html', {'data': data, 'shaved': shaved})
