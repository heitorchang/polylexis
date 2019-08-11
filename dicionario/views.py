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
    Άγγλος, -ίδα = inglês (pessoa)
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
    Αιγύπτιος, -ια = egípcio (pessoa)
    αιγυπτιακός, -ή, -ό = egípcio
    αιγυπτιακή γλώσσα = egípcia (língua)
    αιγυπτιακά = egípcia (língua)
    η Αιθιοπία = Etiópia
    το αίμα = sangue
    η Αιμιλία = Emilia
    αισθάνομαι = sentir
    η Αϊτή = Haiti
    η αίτηση = inscrição, ficha de inscrição
    η αιτία = causa, razão
    Άιφελ (Πύργος) = Torre Eiffel
    ακολουθώ = seguir
    ακόμη (quantitativo) = ainda, mais
    ακόμη (temporal) = ainda
    το ακορτεόν = acordião
    ακούω = escutar, ouvir
    ακριβός, -ή, -ό = caro
    ακριβώς = exatamente
    (στισ 10) ακριβώς! = às dez em ponto!
    η ακρόαση = audição
    η ακτή = praia
    το αλάτι = sal
    η Αλβανία = Albania
    αλβανική γλώσσα = albanês (língua)
    αλβανικά = albanês (língua)
    αλβανικός, -ή, -ό = albanês
    Αλβανός, -ή/-ίδα = albanês (pessoa)
    η Αλεξάνδρα = Alexandra
    η Αλεξάνδρεια = Alexandria
    η Αλεξανδρούπολη = Alexandroupoli
    ο Αλέξης = Alex
    η Αλεξία = Alexia
    το αλεύρι = farinha
    η αλήθεια = verdade
    η Αλίκι = Alice
    αλλά = mas
    η αλλαγή = mudança
    αλλάζω = mudar
    αλλιώς = diferentemente
    άλλος, -η, -ο = outro, diverso
    το άλογο = cavalo
    το αλφάβητο = alfabeto
    αμερικανικός, -ή, -ό = americano
    Αμερικανός, -ίδα americano (pessoa)
    Αμερική (ΗΠΑ) = Estados Unidos da América
    αμέσως = imediatamente
    το αμπέλι = vinhedo
    το Άμστερνταμ = Amsterdã
    αν = se
    ανάβω = acender, iluminar
    η ανάγκη = necessidade
    αναγνωρίζω = reconhecer
    η ανάγνωση = leitura
    ανακατεύω = misturar
    η ανάληψη = saque
    ανάμεσα = entre
    αναπνέω = respirar
    ο αναπτήρας = isqueiro
    η ανάσα = respiro
    η Αναστασία = Anastasia
    αναφέρω = referir, mencionar
    η Ανδριανούπολη = Andrianoupoli
    ανεβαίνω = subir, escalar
    ανεξάρτητος, -η, -ο = independente
    άνεργος, -η, -ο = desempregado
    ο Ανέστης = Anestis
    το άνθος = flor
    ο άνθρωπος = homem, ser humano
    ανθρώπινος, -η, -ο = humano
    η Άννα = Anna
    ανοίγω = abrir
    η άνοιξη = primavera
    ανοιχτά = aberto
    ο ανταγωνισμός = competição, torneio
    η Αντιγόνη = Antigone
    αντίθετος, -η, -ο = oposto, contrário
    αντικαθιστώ = trocar
    το αντικείμενο = objeto
    το αντίο = adeus
    αντιστοιχίζω = corresponder
    αντίστοιχος, -η, -ο = correspondente, equivalente
    το αντίτυπο = cópia
    ο άντρας = homem
    ο Αντρέας = André
    αντρικός, -ή, -ό = masculino
    ο Αντώνης = Antônio
    ο Αόριστος = passado (tempo verbal)
    η απάντηση = resposta
    απαντώ = responder
    απαραίτητος, -η, -ο = necessário
    απέναντι = de frente
    απευθύνομαι = dirigir-se a, endereçar
    απλά = simplesmente
    απλός, -ή, -ό = simples
    από = de, desde
    το απόγευμα = a tarde
    ο αποδέκτης = destinatário
    η αποδοχή = aceitação
    η απόσταση = distância
    το αποτέλεσμα = resultado
    η απόφαση = decisão
    αποφασίζω = decidir
    """

    def shave_marks(txt):
        norm_txt = unicodedata.normalize('NFD', txt)
        shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
        return unicodedata.normalize('NFC', shaved).lower()
    
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
            shaved += '"{} {}",\n'.format(shave_marks(line), line)

    shaved += "];"
    
    return render(request, 'dicionario/gregoport.html', {'data': data, 'shaved': shaved})
