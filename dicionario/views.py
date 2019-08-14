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
    (στισ 10) ακριβώς = às dez em ponto
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
    Γεια = Oi, οlá
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
    δικός, -ή, -ό / δικοί, -ές, -ά μας = nosso
    δικός, -ή, -ό / δικοί, -ές, -ά σας = seu
    δικός, -ή, -ό / δικοί, -ές, -ά τους = deles
    δίκαιος, -η, -ο = justo, legítimo
    ο/η δικηγόρος = advogado
    το δίκλινο (δωμάτιο) = quarto duplo
    δίνω = dar
    διορθώνω = corrigir
    δίπλα = ao lado
    διπλανός, -ή, -ό = perto
    διπλός, -ή, -ό = duplo
    διψάω, -ώ = estar com sede
    δοκιμάζω (em geral) = tentar
    δοκιμάζω (comida) = provar
    το Δουβλίνο = Dublim
    η δουλειά = trabalho
    δουλεύω = trabalhar
    ο Δούναβης = Danúbio
    η δραστηριότητα = atividade
    ο δρόμος = rua
    η δύναμη = força
    δυνατός, -ή, -ό = forte
    δυνατά = fortemente
    δύο = dois
    δυόμισι = dois e meio
    η Δύση = oeste
    η δύση = pôr-do-sol
    δύσκολος, -η, -ο = difícil
    δυστυχώς = infelizmente
    δώδεκα = doze
    το δωμάτιο = quarto
    το δώρο = presente
    δωρεάν = grátis
    έβδομος, -η, -ο = sétimo
    εβδομήντα = setenta
    εδώ = aqui
    η εικόνα = imagem, retrato
    είκοσι = vinte
    εικοσιένας/-μία/-ένα = vinte e um
    εκατό = cem
    εκεί = lá
    εκείνος, -η, -ο = aquele
    έκτος, -η, -ο = sexto
    η Ελλάδα = Grécia
    ο Έλληνας = grego (pessoa)
    η Ελληνίδα = grega (pessoa)
    ελληνική γλώσσα = grego (idioma)
    ελληνικά = grego (idioma)
    ελληνικός, -ή, -ό = grego
    ένας, μία, ένα = um, uma
    ένατος, -η, -ο = nono
    ενενήντα = noventa
    ο ενικός αριθμός = singular
    εννέα, εννιά = nove
    έντεκα = onze
    έξι = seis
    εξήντα = sessenta
    το επίθετο = adjetivo
    επιθυμώ = desejar
    επιλέγω = escolher
    η επιλογή = escolha
    το επίπεδο = nível
    επιπλέον = além disso
    το έπιπλο = mobília
    επίσης = também
    η επίσκεψη = visita
    η επιστήμη = ciência
    επιστρέφω = voltar
    το επιτραπέζιο παιχνίδι = jogo de tabuleiro
    επιτρέπεται = é permitido
    επιτρέπω = permitir
    η επιτυχία = sucesso
    επόμενος, -η, -ο = próximo
    η εποχή = época, estação
    το επώνυμο = sobrenome
    η εργασία = trabalho
    το εργαστήριο = oficina, laboratório
    η έρευνα = investigação
    έρχομαι = vir
    η ερώτηση = pergunta
    το εστιατόριο = restaurante
    εσύ, εσείς = você
    η ετικέτα = etiqueta
    ετοιμάζομαι = preparar-se
    ετοιμάζω = preparar
    έτοιμος, -η, -ο = pronto
    το έτος = ano
    ευγενικός, -ή, -ό = gentil
    η ευκαιρία = chance, oportunidade
    εύκολος, -η, -ο = fácil
    το ευρώ = euro
    ευρωπαïκός, -ή, -ό = europeu
    Ευρωπαίος, -α = europeu (pessoa)
    η Ευρώπη = Europa
    η ευτυχία = felicidade
    ευτυχισμένος, -η, -ο = feliz
    ευχάριστος, -η, -ο = agradável
    ευχαριστώ = agradecer
    Ευχαριστώ = Obrigado
    η ευχή = desejo
    ο/η έφηβος/-η = adolescente
    η εφημερίδα = jornal
    εφορία = fisco
    εφόσον = desde
    εφτά/επτά = sete
    εφτακόσιοι/επτακόσιοι, -ες, -α = setecentos
    έχω = ter
    το Ζαΐρ = Zaire
    η Ζάκυνθος = Zakynthos, Zante
    το ζαμπόν = presunto
    τα ζάρια = dados (jogo)
    η ζάχαρη = açúcar
    το ζαχαροπλαστείο = confeitaria
    η ζέστη = calor
    Κάνει ζέστη = Faz calor
    το ζευγάρι = par
    η (Νέα) Ζηλανδία = (Nova) Zelândia
    Ζηλανδός, -ή = neozelandês
    ζητάω, -ώ = perguntar
    η Ζυρίχη = Zurique
    ζω = viver
    ζωγραφίζω = pintar
    η ζωγραφική = pintura
    η ζωή = vida
    ζωντανός, -ή, -ό = vivo
    το ζώο = animal
    ο/η ηθοποιός = ator
    ηλεκτρικός, -ή, -ό = elétrico
    ηλεκτρονικός, -ή, -ό = eletrônico
    η ηλικία = idade
    ο ήλιος = sol
    η μέρα/ημέρα = dia
    το ημερολόγιο = calendário
    η ημερομηνία = data
    Ηρακλής = Hércules
    η ησυχία = calma, tranquilidade
    ήσυχος, -η, -ο = quieto
    ο ήχος = som
    θα = vou
    η θάλασσα = mar
    η θέα = vista
    θεατρικός, -ή, -ό = teátrico
    το θέατρο = teátro
    η θεία = tia
    ο θείος = tio
    θέλω = querer
    η θέρμανση = calefação
    θερμός, -ή, -ό = morno
    η θέση = posição
    η Θεσσαλονίκη = Thessaloniki
    θηλυκός, -ή, -ό = feminino
    το Θιβέτ = Tibete
    ο θόρυβος = ruído
    το θρανίο = mesa escolar
    θυμάμαι = lembrar
    ο Ιανουάριος = janeiro
    η Ιαπωνία = Japão
    ιαπωνικός, -ή, -ό = japonês
    η ιατρική = medicina
    ιδιαίτερος, -η, -ο = especial
    ίδιος, -α, -ο = o mesmo
    η ικανότητα = abilidade, capacidade
    το ίντερνετ = internet
    ο Ιούλιος = julho
    ο Ιούνιος = junho
    η Ιρλανδία = Irlanda
    ιρλανδική γλώσσα = irlandês (idioma)
    ιρλανδικά = irlandês (idioma)
    ιρλανδικός, -ή, -ό = irlandês
    Ιρλανδός, -ή = irlandês (pessoa)
    η Ισλανδία = Islândia
    ισλανδική γλώσσα = islandês (idioma)
    ισλανδικά = islandês (idioma)
    ισλανδικός, -ή, -ό = islandês
    Ισλανδός, -ή = islandês (pessoa)
    το ισόγειο = térreo
    η Ισπανία = Espanha
    ισπανική γλώσσα = espanhol (idioma)
    ισπανικά = espanhol (idioma)
    ισπανικός, -ή, -ό = espanhol
    Ισπανός, -ίδα = espanhol (pessoa)
    το Ισραήλ = Israel
    ισραηλινός, -ή, -ό = israelense
    Ισραηλινός, -ή = israelense (pessoa)
    η ιστορία = história
    ίσως = talvez
    η Ιταλία = Itália
    ιταλική γλώσσα = italiano (idioma)
    ιταλικά = italiano (idioma)
    ιταλικός, -ή, -ό = italiano
    Ιταλός, -ίδα = italiano (pessoa)
    καθαρίζω = limpar
    καθαρός, -ή, -ό = limpo
    κάθε = todo
    καθένας, καθεμία/καθεμιά, καθένα = todo, todo mundo
    κάθετα = verticalmente, do outro lado
    ο/η καθηγητής/-τρια = professor
    καθόλου = nenhum, de jeito nenhum 
    κάθομαι = sentar
    ο καθρέφτης = espelho
    η καθυστέρηση = atraso
    καθώς = enquanto
    και = e
    καινούριος, -ια, -ιο = novo
    ο καιρός = tempo (atmosférico)
    Τι καιρό κάνει; = Que tempo faz?
    κακός, -ή, -ό = ruim
    καλημέρα = bom dia
    καληνύχτα = boa noite
    καλησπέρα = boa tarde
    το καλοκαίρι = verão
    το καλοριφέρ = radiador
    καλός, -ή, -ό = bom
    η κάλτσα = meia
    καλύπτω = cobrir
    καλύτερος, -η, -ο = melhor
    καλώ = chamar, convidar
    καλωσορίζω = dar boas-vindas
    το κάμπιγκ = acampamento
    ο Καναδάς = Canadá
    καναδικός, -ή, -ό = canadense
    Καναδός, -ή = canadense (pessoa)
    ο καναπές = sofá
    κανένας, καμία/καμιά, κανένα = nenhum, ninguém
    ο κανόνας = regra
    κάνω = fazer
    το καπέλο = chapéu
    κάποιος, -α, -ο (substantivo) = alguém
    κάποιος, -α, -ο (adjetivo) = algum, um
    το καράβι = barco
    η καρδιά = coração
    η καρέκλα = cadeira
    το καρότο = cenoura
    το καρπούζι = melancia
    η κάρτα = cartão
    το κασέρι = queijo amarelo
    η κασετίνα = estojo (para lápis)
    το κασκόλ = cachecol
    η κατάθεση = depósito
    καταλαβαίνω = entender
    ο κατάλογος = catálogo
    η κατασκήνωση = acampamento
    η κατάσταση = situação
    κατεβαίνω = descer, diminuir
    η κατεύθυνση = direção
    κάτι = algo
    η κατοικία = residência
    ο/η κάτοικος = residente, habitante
    η κατσίκα = cabra
    κάτω = embaixo
    κάτω από = debaixo
    ο καφές = café
    η καφετέρια = cafeteria
    το κείμενο = texto
    το κενό = lacuna
    κεντρικός, -ή, -ό = central
    το κέντρο = centro
    το κεράσι = cereja
    κερδίζω = ganhar
    η Κέρκυρα = Corfu
    κεφαλαίο γράμμα = letra maiúscula
    το κεφάλι = cabeça
    ο κήπος = jardim
    η κιθάρα = violão
    το κιλό = quilo
    η Κίνα = China
    Κινέζος, -α = chinês (pessoa)
    κινεζική γλώσσα = chinês (idioma)
    κινεζικά = chinês (idioma)
    κινεζικός, -ή, -ό = chinês
    ο κινηματογράφος = cinema
    το κινητό τηλέφωνο = celular
    κίτρινος, -η, -ο = amarelo
    το κλειδί = chave
    κλείνω = fechar, desligar
    το κλίμα = clima
    κόβω = cortar
    η κοιλιά = barriga
    κοιμάμαι = dormir
    κόκκινος, -η, -ο = vermelho
    ο κόκορας = galo
    κολλάω = colar, grudar
    το κολοκυθάκι = abobrinha
    η κολόνα = coluna
    κολυμπάω, -ώ = nadar
    το κολύμπι = natação
    το κομμάτι = pedaço
    το κομμωτήριο = salão de cabeleireiro
    ο/η κομμωτής/-τρια = cabeleireiro
    κοντά = perto
    κοντός, -ή, -ό = curto, baixo
    η κοπέλα = menina
    η Κορέα = Coreia
    Κορεάτης, -ισσα = coreano (pessoa)
    κορεατικός, -ή, -ό = coreano
    κορεατική γλώσσα = coreano (idioma)
    κορεάτικα = coreano (idioma)
    η κόρη = filha
    το κορίτσι = menina
    η κορνίζα = moldura
    το κορόιδο = otário
    ο κόσμος = gente, mundo
    το κοστούμι = terno
    το/η κοτόπουλο/κότα = frango
    η κουβέρτα = cobertor
    το κουδούνι = sino
    η κουζίνα = cozinha
    η κούκλα = boneca
    το κουνέλι = coelho
    το κουτί = caixa
    το κρανίο = crânio
    το κρασί = vinho
    κρατάω, -ώ = segurar
    το κρέας = carne
    το κρεβάτι = cama
    το κρεμμύδι = cebola
    το κρεοπωλείο = açougue
    ο κρεοπώλης = açougueiro
    Κρήτη = Creta
    (Τι) κρίμα = Que pena
    κρίνω = julgar
    Κροατία = Croácia
    κρύβω = esconder
    κρυμμένος, -η, -ο = escondido
    κρύος, -α, -ο = frio
    το κρυπτόλεξο = caça-palavras
    ο κύκλος = círculo
    κυκλώνω = circular
    η κυρία = senhora
    η Κυριακή = domingo
    ο κύριος = senhor
    ο λαβύρινθος = labirinto
    ο λαγός = lebre
    το λάδι = óleo
    το λάθος = erro
    η λαϊκή (αγορά) = feira de rua
    τα λαχανικά = legumes
    το λάχανο = repolho
    λείπω = estar ausente
    η λεμονάδα = limonada
    το λεμόνι = limão
    η λέξη = palavra
    το λεξικό = dicionário
    το λεξιλόγιο = vocabulário
    το λεπτό = minuto
    λεπτός, -ή, -ό = fino, magro
    λευκός, -ή, -ό = branco
    λέω = dizer
    το λεωφορείο = ônibus
    η λιακάδα = brilho do sol
    λίγοι, -ες, -α (contável) = alguns
    λίγος, -η, -ο (não contável) = pouco
    το λιμάνι = porto
    η λίμνη = lago
    τα λιπαρά = gordura
    η λίστα = lista
    ο λογαριασμός = conta
    ο λόγος (causa) = razão
    το Λονδίνο = Londres
    το λουλούδι = flor
    το Λουξεμβούργο = Luxemburgo
    το Λύκειο = colégio
    ο λύκος = lobo
    λύνω = resolver
    λυπάμαι = lamentar
    η λύπη = tristeza
    λυπημένος, -η, -ο = triste
    το μαγαζί = loja
    ο/η μάγειρας/-ισσα = cozinheiro
    μαγειρεύω = cozinhar
    μαγικός, -ή, -ό = mágica
    το μαγιό = maiô
    μαζεύω = reunir
    μαζί = junto
    μαθαίνω = aprender
    το μάθημα = lição
    μαθήματα για το σπίτι = lição de casa
    Μαθηματικά = matemática
    ο/η μαθητής/-τρια = aluno
    ο Μάιος = maio
    μακαρόνια = massa, macarrão
    μακριά = longe
    μακρύς, -ιά, -ύ = longo
    τα μαλλιά = cabelos
    μάλλον = talvez
    ο μανάβης = merceeiro
    το μανάβικο = mercearia
    το μαρούλι = alface
    ο Μάρτιος = março
    το μάτι = olho
    μαύρος, -η, -ο = preto
    το μαχαίρι = faca
    με = com
    μεγάλος, -η, -ο = grande
    το μέγεθος = tamanho
    μεθαύριο = depois de amanhã
    μελαχρινός, -ή, -ό = moreno
    μελετάω, -ώ = estudar
    τα μέλη του σώματος = partes do corpo
    το μέλι = mel
    η μελιτζάνα = berinjela
    μένω = ficar, estar, morar
    η μέρα = dia
    μερικοί, -ές, -ά = algum
    το μέρος = parte, lugar
    μέσα (μένω μέσα στο σπίτι) = (ficar) dentro de casa
    μέσα σε = em
    τα μέσα μεταφοράς = meios de transporte
    η μέση (parte do corpo) = cintura
    η μέση (lugar) = meio
    το μεσημέρι = meio-dia
    ο μεσίτης = corretor
    το μέσο = meios
    μετά = depois
    μεταφράζω = traduzir
    μετράω, -ώ = contar
    τα μετρητά = dinheiro
    το μέτρο = metro
    το μετρό = metrô
    μέχρι = até
    το μηδέν = zero
    η μηλιά = macieira
    το μήλο = maçã
    ο μήνας = mês
    το μήνυμα = mensagem
    η μητέρα = mãe
    η μαμά = mãe
    η μηχανή = máquina
    μικρός, -ή, -ό = pequeno
    μιλάω, -ώ = falar, dizer
    ο μισθός = salário
    μισός, -ή, -ό = metade
    η μνήμη = memória
    μοβ = roxo
    μοιάζω = parecer 
    μοιράζω = distribuir
    μόλις = apenas
    το μολύβι = lápis
    μόνιμα = permanentemente
    μόνιμος, -η, -ο = permanente
    η μονοκατοικία = casa isolada
    μονόκλινος, -η, -ο = com só uma cama
    μόνος, -η, -ο = sozinho
    μονός, -ή, -ό = solteiro
    μοντέρνος, -α, -ο = moderno
    η Μόσχα = Moscou
    το μουσείο = museu
    η μουσική = música
    μουσικός, -ή, -ό = musical
    ο/η μουσικός = músico
    μπαίνω = entrar
    ο μπακάλης = merceeiro
    η μπάλα = bola
    το μπαλέτο = balé
    το μπαλκόνι = varanda
    ο μπαμπάς = pai
    η μπανάνα = banana
    η μπανιέρα = banheira
    το μπάνιο = banheiro
    κάνω μπάνιο = tomar banho
    το μπαρ = bar
    το μπάσκετ = basquete
    μπεζ = bege
    η μπίρα = cerveja
    το μπιφτέκι = hambúrguer
    μπλε = azul
    η μπλούζα = blusa
    μπορώ = poder, ser capaz
    το μπουκάλι = garrafa
    το μπουφάν = jaqueta
    Μπράβο = Muito bem
    η μπριζόλα = bife
    το μπρόκολο = brócolis
    μπροστά = na frente
    το μυαλό = mente
    Μύκονος = Míconos
    μυρίζω = cheirar
    η μύτη = nariz
    το μωρό = bebê
    ναι = sim
    νέος, -α, -ο = novo, jovem
    το νερό = água
    το νησί = ilha
    ο/η νικητής/-τρια = vencedor
    νιώθω = sentir
    ο Νοέμβριος = novembro
    το νόημα = sentido
    νοικιάζω = alugar
    νομίζω = pensar
    η Νορβηγία = Noruega
    Νορβηγός, -ίδα = norueguês (pessoa)
    νορβηγικός, -ή, -ό = norueguês
    νορβηγική γλώσσα = norueguês (idioma)
    νορβηγικά = norueguês (idioma)
    το νοσοκομείο = hospital
    ο/η νοσοκόμος/-α = enfermeiro
    νόστιμος, -η, -ο = gostoso
    η νότα = nota
    το νούμερο = número
    Ντουμπάι = Dubai
    η νταντά = babá
    η ντομάτα = tomate
    το ντόνατ = donut
    η ντουλάπα = guarda-roupas
    το ντουλάπι = armário 
    τα ντραμς = bateria (tambores)
    ντύνομαι = vestir-se
    το νυφικό = vestido de noiva
    η νύχτα = noite
    Νυχτώνει = Anoitece
    νωρίς = cedo
    ο/η ξάδερφος/-η = primo 
    ξανά = de novo
    ξανθός, -ή, -ό = loiro
    ξεκινάω, -ώ = começar
    το ξενοδοχείο = hotel
    ξενυχτάω, -ώ = ficar acordado (tarde)
    ο ξενώνας = hostel, albergue
    ξέρω = saber
    ξεφεύγω = escapar
    ξεχνάω, -ώ = esquecer
    ξεχωριστά = separadamente
    ξοδεύω = gastar
    το ξύδι = vinagre
    το ξύλο = madeira
    ξυπνάω, -ώ = acordar
    η ξύστρα = apontador
    ογδόντα = oitenta
    όγδοος, -η, -ο = oito
    ο/η οδηγός = guia
    οδηγώ = dirigir (um veículo), guiar
    η οδοντογλυφίδα = palito de dente
    η οδός = rua, estrada, avenida
    η οικογένεια = família
    το οικογενειακό δέντρο = árvore genealógica
    η οικοδομή = edifício
    οκτώ, οχτώ = oito
    ο Οκτώβριος = outubro
    η Ολλανδία = Holanda
    Ολλανδός, -ή = holandês (pessoa)
    ολλανδικός, -ή, -ό = holandês
    ολλανδική γλώσσα = holandês (idioma)
    ολλανδικά = holandês (idioma)
    όλοι, -ες, -α = todo, todos
    ο Όλυμπος = Monte Olímpo
    η ομάδα = equipe
    όμοιος, -α, -ο = semelhante
    η ομοιότητα = semelhança
    όμορφος, -η, -ο = belo
    η ομπρέλα = guarda-chuva
    όμως = mas, porém
    το όνειρο = sonho
    το όνομα = nome
    η όπερα = ópera
    οποίος, -α, -ο (pessoa) = quem
    όποιος, -α, -ο = qualquer um, qualquer
    οποιοσδήποτε, οποιαδήποτε, οποιοδήποτε (substantivo, adjetivo) = qualquer
    όποτε = a qualquer hora
    όπου = em qualquer lugar
    όπως = como
    ορθογώνιο = retângulo
    Ορίστε = Aqui está
    ο όροφος = chão
    όταν = quando
    η Ουγγαρία = Hungria
    το ούζο = ouzo
    η Ουκρανία = Ucrânia
    ο ουρανός = céu
    όχι = não
    οχτακόσιοι/οκτακόσιοι, -ες, -α = oitocentos
    ο πάγκος = banco (assento)
    το παγωτό = sorvete
    το παζλ = quebra-cabeças
    ο/η παθολόγος = patologista
    το παιδί = criança
    τα παιδιά = crianças
    ο/η παιδίατρος = pediatra
    παίζω = brincar
    παίρνω = pegar
    το παιχνίδι = jogo, brinquedo
    το πακέτο = pacote
    το Πακιστάν = Paquistão
    πάλι = de novo
    παλιός, -ά, -ό = velho
    το παλτό = casaco
    η Παναγία = Santa Maria
    ο Παναμάς = Panamá
    το πανεπιστήμιο = universidade
    πάντα = sempre
    το παντελόνι = calça
    το παντζάρι = beterraba
    η παντομίμα = pantomima
    η παντόφλα = chinelo
    παντρεύομαι = casar-se
    πάνω = cima
    πάνω σε = em cima de
    το παπούτσι = sapato
    ο παππούς = avô
    η παραγγελία = ordem, comando
    παραγγέλνω = ordenar
    το παράδειγμα = exemplo
    παραδοσιακός, -ή, -ό = tradicional
    το παράθυρο = janela
    παρακαλώ = agradar
    (Σε/Σας) παρακαλώ = Por favor
    Παρακαλώ (respondendo a 'obrigado') = De nada
    παρακάτω = debaixo
    παρακολουθώ = vigiar
    η παραλία = praia
    το παραμύθι = conto de fadas
    παραπάνω / πιο πάνω = acima
    παραπάνω / περισσότερο = mais
    η Παρασκευή = sexta-feira
    παρατηρώ = observar
    το Παρίσι = Paris
    το πάρκιγκ = estacionamento
    το πάρκο = parque
    παρουσιάζω = apresentar
    το πάρτι = festa
    το Πάσχα = Páscoa
    η πατάτα = batata
    τα πατατάκια = chips de batata
    ο πατέρας = pai
    ο Παύλος = Paulo
    το πεζοδρόμιο = calçada
    πεινάω = estar com fome
    ο/η πελάτης/-ισσα = cliente
    η Πέμπτη = quinta-feira
    πέμπτος, -η, -ο = quinto
    πενήντα = cinquenta
    πεντακόσιοι, -ες, -α = quinhentos
    πέντε = cinco
    πεντέμισι = cinco e meio
    το πεπόνι = melão
    το περιβάλλον = ambiente
    περιγράφω = descrever
    περιμένω = esperar
    το περιοδικό = revista
    η περιοχή = região
    το περίπτερο = quiosque
    περισσότερο = mais
    περνάω, -ώ = passar
    περνάω καλά = divertir-se
    περπατάω, -ώ = andar
    πέρσι/πέρυσι = ano passado
    το πετρέλαιο = petróleo
    ο Πέτρος = Pedro
    η Πετρούπολη = São Petersburgo
    η πετσέτα = toalha
    πέφτω = cair
    πηγαίνω = ir
    πια = não mais 
    το πιάνο = piano
    πιάνω = tocar
    το πιάτο = prato
    πιθανός, -ή, -ό = provável, possível
    πιθανώς = provavelmente
    ο πίνακας (na sala de aula) = lousa
    ο πίνακας (exercício) = tabela
    ο πίνακας (obra de arte) = pintura
    πίνω = beber
    πιο = mais
    το πιπέρι = pimenta
    η πιπεριά = pimentão
    το πιρούνι = garfo
    η πισίνα = piscina
    πιστεύω = acreditar
    η πιστωτική κάρτα = cartão de crédito
    πίσω = atrás
    οι πιτζάμες = pijama
    η πίτσα = pizza
    πλάι = ao lado
    η πλατεία = praça
    πλένω = lavar
    ο πληθυντικός (αριθμός) = (número) plural
    η/οι πληροφορία/-ες = informação
    πληρώνω = pagar
    το πλοίο = navio
    το πλυντήριο = máquina de lavar
    το ποδήλατο = bicicleta
    το/τα πόδι/πόδια = pé, pés
    το ποδόσφαιρο = futebol
    ποιανού, -ής (para uma pessoa) = de quem
    ποιος, -α, -ο (não para pessoas) = qual
    ποιος, -α, -ο (para pessoas) = quem
    η πόλη = cidade
    πολλοί, ές, -ά (contável) = muitos, bastante
    πολύ = muito
    η πολυθρόνα = poltrona
    το πολυκατάστημα = loja de departamento
    η πολυκατοικία = edifício de apartamentos
    πολύς, πολλή, πολύ (não contável) = muito
    πονάω, -ώ = doer, sentir dor
    ο πόνος = dor
    η πόρτα = porta
    η Πορτογαλία = Portugal
    Πορτογάλος, -ίδα = português (pessoa)
    πορτογαλικός, -ή, -ό = português
    πορτογαλική γλώσσα = português (idioma)
    πορτογαλικά = português (idioma)
    η πορτοκαλάδα = laranjada
    πορτοκαλής, -ιά, -ί = laranja
    το πορτοκάλι = laranja
    η πορτοκαλιά = laranjeira
    το πορτοφόλι = carteira
    πόσοι, -ες, -α = quantos
    πόσος, -η, -ο = quanto
    ποτέ = nunca
    πότε = quando
    το ποτήρι = copo
    ποτίζω = regar, dar para beber
    το ποτό = bebida
    που (relativo) = quem, qual
    πού (interrogativo) = onde
    το πουκάμισο = camisa
    πουλάω = vender
    το πουλί = pássaro
    το πράγμα = coisa
    η πραγματικότητα = realidade
    πράσινο = verde
    πρέπει = eu/você/ele deve
    πριν (από) = antes
    το πρόβλημα = problema
    το πρόγραμμα = horário, programa
    προετοιμάζω = preparar
    η προετοιμασία = preparação
    προηγούμενος, -η, -ο = anterior
    το προϊόν = produto
    ο προορισμός = destino
    προς = para
    προσεκτικά = cuidadosamente
    προσέχω = prestar atenção
    προσκαλώ = convidar
    η πρόσκληση = convite
    η προσοχή = atenção
    προσπαθώ = tentar
    προσφέρω = oferecer
    το πρόσωπο (indivíduo, ou na gramática) = pessoa
    το πρόσωπο (parte do corpo) = rosto
    η πρόταση = frase
    προτείνω = sugerir
    προτιμώ = preferir
    προφέρω = pronunciar
    η προφορά = pronúncia
    το πρωί = manhã
    το πρωινό = café da manhã
    πρώτα = primeiramente
    η Πρωτομαγιά = primeiro de maio
    πρώτος, -η, -ο = primeiro
    η Πρωροχρονιά = Véspera de Ano-Novo
    ο πύργος = torre
    ο πυρετός = febre
    ο/η πωλητής/-τρια = vendedor, assistente de loja
    πώς = como
    Πώς σε λένε; = Como se chama?
    το ραδιόφωνο = rádio
    το ρεπό = dia de folga
    το ρεύμα (ηλεκτρικό) = eletricidade
    ρίχνω = jogar
    ροζ = rosa
    το ρολόι (de parede) = relógio
    το ρολόι (de pulso) = relógio
    ο ρόλος = parte, papel (de um ator)
    το ρούχο = tecido
    το ρύζι = arroz
    η Ρώμη = Roma
    η Ρωσία = Rússia
    Ρώσσος, -ίδα = russo (pessoa)
    ρωσσικός, -ή, -ό = russo
    ρωσσική γλώσσα = russo (idioma)
    ρωσσικά = russo (idioma)
    ρωτάω, -ώ = perguntar
    το Σάββατο = sábado
    το Σαββατοκύριακο = fim de semana
    το σακάκι = jaqueta
    το σαλάμι = salame
    η σαλάτα = salada
    το σαλόνι = sala de estar
    η σαμπάνια = champagne
    το σαμπουάν = xampu
    σαν = como
    το σάντουιτς = sanduíche
    το σαπούνι = sabão
    σαράντα = quarenta
    σβήνω = apagar
    η σβήστρα = borracha (para apagar)
    σε = em, a
    η σειρά = série, ordem
    σελίδα = página
    το σενάριο = cenário
    το σεντόνι = lençol
    ο Σεπτέμβριος = setembro
    η Σερβία = Sérvia
    σερβίρω = servir
    ο σερβιτόρος = garçom
    σημαίνω = significar
    σημαντικός, -ή, -ό = importante
    το σημείωμα = anotação, memorando
    σημειώνω = fazer anotações
    σήμερα = hoje
    σίγουρα = certamente
    σίγουρος, -η, -ο = certo
    το Σίδνεϋ = Sydney
    το σινεμά = cinema
    η σκάλα = escada
    οι σκάλες = escadas
    σκέφτομαι = pensar
    το σκίτσο = esboço, desenho
    η σκόνη = poeira
    σκουπίζω = varrer
    ο/το σκούφος/σκουφί = gorro
    ο σκύλος = cachorro
    σοβαρά = a sério
    σοβαρός, -ή, -ό = sério
    το σόι = parentesco
    η σοκολάτα = chocolate
    το σουβλάκι = souvlaki
    η Σουηδία = Suécia
    σουηδική γλώσσα = sueco (idioma)
    σουηδικά = sueco (idioma)
    σουηδικός, -ή, -ό = sueco
    Σουηδός, -ή = sueco (pessoa)
    το σούπερ μάρκετ = supermercado
    σπαγγέτι = espaguete
    το σπανάκι = espinafre
    το/η σπήλαιο/σπηλιά = caverna
    το σπίτι (residência) = casa
    το σπίτι (família) = lar
    σπουδάζω = estudar
    οι σπουδές = estudos
    σταματάω, -ώ = parar
    η στάση λεωφορείου = ponto de ônibus
    το σταυρόλεξο = palavras cruzadas
    το σταφύλι = uva
    στέλνω = enviar
    η στήλη = coluna
    το/ο στιλό/στιλός = caneta
    ο στίχος = verso
    το στολίδι = decoração
    στολίζω = decorar
    στολισμένος, -η, -ο = decorado
    Συγνώμη/Συγγνώμη = Desculpe
    η συγνώμη/συγγνώμη = desculpa
    ο συγγραφέας = autor, escritor
    συγκρίνω = comparar
    η σύγκριση = comparação
    τα συγχαρητήρια = parabéns
    σύγχρονος = contemporâneo
    η συζήτηση = discussão
    συζητώ = discutir
    συμβουλεύω = aconselhar
    η συμβουλή = conselho
    ο/η συμμαθητής/-τρια = colega de escola
    συμμετέχω = participar
    συμπληρώνω = completar
    σύμφωνα = de acordo com
    το σύμφωνο = consoante
    ο/η συνάδελφος = colega
    """

    def shave_marks(txt):
        norm_txt = unicodedata.normalize('NFD', txt)
        shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
        shaved = shaved.replace("(", "").replace(")", "")
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
