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
    αγγλική γλώσσα = inglês (idioma)
    αγγλικά = inglês (idioma)
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
    αιγυπτιακή γλώσσα = egípcia (idioma)
    αιγυπτιακά = egípcia (idioma)
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
    αλβανική γλώσσα = albanês (idioma)
    αλβανικά = albanês (idioma)
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
    αποφεύγω = evitar
    ο/η απόφοιτος/-η = graduado, diplomado
    ο Απρίλιος = abril
    η (Σαουδική) Αραβία = Arábia Saudita
    ο αρακάς =ervilha
    αργά = tarde
    αργώ = estar tarde 
    (μου) αρέσει = gostar
    το άρθρο = artigo
    ο αριθμός = número
    αριστερά = na esquerda
    αριστερός, -ή, -ό = esquerdo
    άριστος, -η, -ο = o melhor, excelente
    αρκετός, -ή, -ό = suficiente
    η Αρκτική = Ártico
    αρκώ = ser suficiente
    η Αρμενία = Armênia
    αρμενική γλώσσα = armênio (idioma)
    αρμενικά = armênio (idioma)
    αρμενικός, -ή, -ό = armênio
    Αρμένιος, -ια = armênio (pessoa)
    αρνούμαι = recusar, dizer não
    αρρωσταίνω = ficar doente
    η αρρώστια = doença
    άρρωστος, -η, -ο = doente
    αρσενικός, -ή, -ό = masculino
    η αρχή = começo, início
    αρχίζω = começar
    το ασανσέρ = elevador
    ο/η ασθενής = o/a paciente
    η Ασία = Ásia
    η άσκηση = exercício
    η ασπιρίνη = aspirina
    άσπρος, -η, -ο = branco
    η αστυνομία = polícia
    ο/η αστυνομικός = policial
    άσχημα = mal
    άσχημος = feio
    η ασχολία = profissão
    η ατζέντα = agenda
    το άτομο = pessoa
    το ατύχημα = acidente
    ο Αύγουστος = agosto
    αυθόρμητος, -η, -ο = espontâneo
    η αυλή = pátio
    η αϋπνία = insônia
    το αύριο = amanhã
    η Αυστραλία = Austrália
    Αυστραλός, -ίδα = australiano (pessoa)
    αυστραλιανός, -ή, -ό = australiano
    η Αυστρία = Áustria
    Αυστριακός, -ή = austríaco (pessoa)
    αυστριακός, -ή, -ό = austríaco
    το αυτί = orelha
    το αυτοκίνητο = carro
    αυτός, -ή, -ό (para pessoas) = ele, ela
    αυτός, -ή, -ό (não para pessoas) = este
    το αφεντικό = chefe
    αφήνω = deixar
    η αφίσα = pôster
    αφού = depois
    αφρικανικός, -ή, -ό = africano
    Αφρικανός, -ή = africano (pessoa)
    η Αφρική = África
    ο Απόστολος = Apostolos
    ο Αποστόλης = Apostolos
    το Αργοστόλι = Argostoli
    βάζω = pôr
    το βάζο = vaso
    βαθιά = profundamente
    ο βαθμός = grau
    βαθύς, -ιά, -ύ = profundo
    η βαλίτσα = mala
    ο βάλτος = pântano
    το βαπόρι = navio a vapor
    βαριά = pesadamente
    βαρύς, -ιά, -ύ = pesado
    το βάρος = peso
    η βάση = base
    βασικός, -ή, -ό = básico
    ο Βασίλης = Vassilis
    η Βασιλική = Vassiliki
    η βασιλόπιτα = bolo de ano novo
    η Βάσω = Vasso
    βάφω = pintar
    βγάζω = tirar
    βγαίνω = sair
    η βδομάδα/εβδομάδα = semana
    βέβαια = claro, certamente
    το Βέλγιο = Bélgica
    βελγικός, -ή, -ό = belga
    Βέλγος, -ίδα = belga (pessoa)
    το Βελιγράδι = Belgrado
    βελούδινος, -η, -ο = veludo
    η Βενεζουέλα = Venezuela
    το βενζινάδικο = posto de gasolina
    το βερίκοκο = damasco
    το Βερολίνο = Berlim
    το βήμα = passo
    ο βήχας = tosse
    βήχω = tossir
    το βιβλίο = livro
    το βιβλιάριο = livreto
    η βιβλιοθήκη = biblioteca
    η Βιέννη = Viena
    το βιολί = violino
    η βιτρίνα = vitrine
    βλέπω = ver, olhar
    βοηθάω, -ώ = ajudar
    η βοήθεια = ajuda
    βοηθητικός, -ή, -ό = prestativo, auxiliar
    το βόλεϊ = vôlei
    η βόλτα = caminhada
    η Βουλγαρία = Bulgária
    βουλγαρικός, -ή, -ό = búlgaro
    βουλγαρική γλώσσα = búlgaro (idioma)
    βουλγαρικά = búlgaro (idioma)
    Βούλγαρος, -α = búlgaro (pessoa)
    το βουνό = montanha
    το βούτυρο = manteiga 
    η βραδιά = noite
    το βραδινό (φαγητό) = jantar
    το βράδυ = noite
    η Βραζιλία = Brasil
    βραζιλιανικός, -ή, -ό = brasileiro
    βραζιλιανική γλώσσα = brasileiro (idioma)
    βραζιλιανικά = brasileiro (idioma)
    Βραζιλιάνος, -α = brasileiro (pessoa)
    η Βρετανία = Grã-Bretanha
    βρέχω = molhar
    βρίσκω = achar
    η βροχή = chuva
    οι Βρυξέλλες = Bruxelas
    η βρύση = torneira
    ο γάιδαρος = asno
    το γαϊδούρι = asno
    το γάλα = leite
    γαλανός, -ή, -ό = azul
    η Γαλλία = França
    γαλλικός, -ή, -ό = francês
    γαλλική γλώσσα = francês (idioma)
    γαλλικά = francês (idioma)
    ο γάμος (cerimônia) = casamento
    ο γάμος (instituição) = matrimônio
    το γάντι = luva
    το γαριδάκι = salgadinho
    το γαρίφαλο = cravo (flor)
    η γάτα = gato
    Γεια! = Oi! Olá!
    ο γείτονας = vizinho
    η γειτονιά = vizinhança
    γελάω, -ώ = rir
    γελαστός, -ή, -ό = rindo
    γεμίζω = encher
    τα γενέθλια = aniversário
    γενικά = geralmente
    γεννάω, -ώ = dar à luz
    η γέννηση = nascimento
    η Γερμανία = Alemanha
    γερμανική γλώσσα = alemão (idioma)
    γερμανικά = alemão (idioma)
    γερμανικός, -ή, -ό = alemão
    Γερμανός, -ίδα = alemão (pessoa)
    γερός, -ή, -ό = saudável
    ο γέρος = idoso
    το γεύμα = refeição
    το γήπεδο = campo (esportivo)
    για = para
    η γιαγιά = avó 
    ο Γιάννης = João
    το γιαούρτι = iogurte
    γιαπωνέζικη γλώσσα = japonês (idioma)
    γιαπωνέζικα = japonês (idioma)
    Γιαπωνέζος, -α = japonês (pessoa)
    το γιασεμί = jasmim
    γιατί (interrogativo) = por que
    γιατί (causativo) = porque
    ο/η γιατρός = médico
    γίνομαι = tornar
    η γιορτή = festa, celebração
    ο γιος = filho
    ο Γιώργος = Jorge
    γκρι = cinza
    η γκρίνια = resmungo
    το γλύκο = doce
    γλυκός, -ιά, -ό = doce
    η γλώσσα = idioma
    η γλώσσα (parte do corpo) = língua
    γλώσσα μητρική = língua materna
    η γνώμη = opinião
    γνωρίζω = saber
    η γνώση = conhecimento
    γνωστός, -ή, -ό = conhecido
    οι γονείς = pais
    το γουρούνι = porco
    η γραβάτα = gravata
    το γράμμα = letra
    ο/η γραμματέας = secretário
    η γραμματική = gramática
    το γραμματοκιβώτιο = caixa de correio
    το γραμματόσημο = selo
    η γραμμή = linha
    γραπτός, -ή, -ό = escrito
    το γραφείο (quarto) = escritório
    το γραφείο (móvel) = escrivaninha
    γράφω = escrever
    η γραφή = escrita
    γρήγορος, -η, -ο = rápido
    γρήγορα = rapidamente
    ο Γρηγόρης = Gregório
    τα γυαλιά = óculos
    το Γυμνάσιο = colégio
    το γυμναστήριο = academia
    γυμναστής, -τρια = professor de educação física
    η γυμναστική = ginástica
    η γυναίκα = mulher
    γυναικείος, -α, -ο = feminino
    γυρίζω = voltar
    γυρνάω = voltar
    ο γύρος = gyros
    η γωνία = esquina
    δανέζικη γλώσσα = dinamarquês (idioma)
    δανέζικα = dinamarquês (idioma)
    δανέζικος, -η, -ο = dinamarquês
    η Δανία = Dinamarca
    Δανός, -ή (-έζα) = dinamarquês (pessoa)
    δάσκαλος, -α = professor
    το δάσος = floresta
    η δάφνη = louro
    δείχνω = mostrar
    δέκα = dez
    δεκαεννιά = dezenove
    δεκαέξι = dezesseis
    δεκαεπτά = dezessete
    δεκαοκτώ = dezoito
    δεκαπέντε = quinze
    δεκατέσσερις, δεκατέσσερα = quatorze
    δέκατος = décimo
    δεκατρείς, δεκατρία = treze
    ο Δεκέμβριος = dezembro
    το δελφίνι = golfinho
    το δέμα = pacote
    το δέντρο = árvore
    δεξιά = direita
    η Δευτέρα = segunda-feira
    δεύτερος, -η, -ο = segundo
    η Δήμητρα = Dimitra
    ο Δημήτρης = Dimitris
    τα δημητριακά = cereal
    δημιουργώ = criar
    η δημοκρατία = democracia
    δημόσιος, -α, -ο = público
    ο/η δημοσιογράφος = jornalista
    το Δημοτικό σχολείο = escola primária
    διαβάζω = ler
    το διαβατήριο = passaporte
    το διάγραμμα = diagrama
    διαγράφω = apagar
    διαγώνια = diagonalmente
    το διαγώνισμα = exame, prova
    το διαδίκτυο = internet
    η διαδρομή = caminho, rota
    διαθέσιμος, -η, -ο = disponível
    οι διακοπές = férias
    διακόσιοι, -ες, -α = duzentos
    διακρίνω = distinguir
    διαλέγω = escolher
    ο διάλογος = diálogo
    η διαμονή = acomodação
    το διαμέρισμα = apartamento 
    η διάρκεια = duração
    διαρκώς = constantemente
    διασκεδάζω = divertir-se
    η διατροφή = nutrição
    η διαφήμιση = propaganda
    η διαφορά = diferença
    διαφορετικός, -ή, -ό = diferente
    διαφορετικά = diferentemente
    τα δίδακτρα = taxas escolares
    διδάσκω = ensinar
    η διδασκαλία = ensino
    διεθνής, -ής, -ές = internacional
    η διεύθυνση = endereço
    διευθυντής, -ντρια (em geral) = gerente, diretor
    διευθυντής, -ντρια (na escola) = diretor
    δικός, -ή, -ό / δικοί, -ές, -ά μου = meu
    δικός, -ή, -ό / δικοί, -ές, -ά σου = seu
    δικός, -ή, -ό / δικοί, -ές, -ά του = dele
    δικός, -ή, -ό / δικοί, -ές, -ά της = dela
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
