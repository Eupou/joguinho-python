print("Indo ao parquinho adventures!\n")
print("Você gostaria de ir ao parquinho\nsim - 1, não - 2")

def bad_end():
    print("Você sai de casa e se depara com um goblin! :o")
    print("Goblin: Daqui você não passara!\n")
    print("1 - Usar patins, 2 - Zoar o goblin, 3 - Bater no goblin")
    aswer = int(input("Você: "))
    if aswer == 1:
        print("Você usa seu patins e fogue do goblin!")
        print("Agora você está no parquinho\nbrincando sozinho, triste e sem ninguém! T-T")
    if aswer == 2:
        print("Você zoa o goblin ele se sente humilhado e vai embora triste!")
        print("Você pensa no que fez até chegar ao parquinho\nse sentindo culpado pelo que fez chora e brinca sonzinho! T-T")
    if aswer == 3:
        print("Você bate no goblin,\ngoblin começa a chorar e vai embora.\nVocê volta para casa e deita na sua cama pensando no que fez. T-T")
    print("\nFinal ruim")

def avarage_end():
    print("Você sai de casa e se depara com um goblin! :o")
    print("Goblin: Daqui você não passara!\n")
    print("1 - Usar guarda-chuva, 2 - Ignorar o goblin, 3 - Falar para o goblin sair da frente")
    aswer = int(input("Você: "))
    if aswer == 1:
        print("Você abre seu guarda-chuva e passa sem que o goblin te veja!")
        print("Agora você está no parquinho\nbrincando sozinho!")
    if aswer == 2:
        print("Você ignora o goblin,\ne passa por ele como se ele nem existisse!")
        print("Você chega no parquinho e vê o goblin brincado com seus amigos\njá você está brincando sozinho!")
    if aswer == 3:
        print("Você fala para o goblin sair da frente,\ngoblin fica chateado e vai embora.\nVocê chega ao parquinho e fica lá sem ninguém!")
    print("\nFinal médio")

def good_end():
    print("Você sai de casa e se depara com um goblin! :o")
    print("Goblin: Daqui você não passara!\n")
    print("1 - Mostrar patinho, 2 - Chamar o goblin para ir com você, 3 - Elogiar o goblin")
    aswer = int(input("Você: "))
    if aswer == 1:
        print("Você mostra o patinho para o goblin e ele fica  encantado!")
        print("Vocês vão juntos para o parquinho e agora estão se divertindo com o patinho! :)")
    if aswer == 2:
        print("Você chama o goblin para ir com você,\nele aceita e agora está feliz!")
        print("Vocês agora brincam juntos e aproveitam o parquinho! :)")
    if aswer == 3:
        print("Você elogia o goblin,\ngoblin lisongeado e segue você até o parquinho!\nVocês chegam ao parquinho e finalmente podem brincar!")
    print("\nFinal bom")

def choose_item():
    print("Mas calma é muito perigoso sair assim!\nleve alguma coisa")
    print("1 - Guarda-chuva, 2 - Pato de borracha, 3 - Patins")
    aswer = int(input("Você: "))
    if aswer == 1:
        print("Agora você tem um guarda-chuva")
        avarage_end()
    if aswer == 2:
        print("Agora você tem um patinho")
        good_end()
    if aswer == 3:
        print("Agora você tem um patins")
        bad_end()

aswer = int(input("Você: "))
if aswer == 1:
    print(aswer)
    print("-Sim, claro que eu gostaria de ir! :)\n")
    choose_item()
else: 
    print("Não, estou cansadinho! ;-;")
