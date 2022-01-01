

nome = input("Qual o seu nome?")
nome = nome.title()
idade = int(input(f"Então, seu nome é {nome} certo?\nQual a sua idade?"))
job = input(f"Então {nome}, você faz o que da vida?")
job = job.title()
print(f"\"{job}\" na idade de {idade} anos?\nPor isso é pobre.\nPretende fazer algo que presta na vida?")
simnao = input("Responda \"sim\" ou \"não\"")
simnao = simnao.title()
while simnao != "Sim" or simnao != "Sim " or simnao != "Não" or simnao != "Não ":

    if simnao == "Sim" or simnao == "Sim ":
        print("DUVIDO!")
        break
    elif simnao == "Não" or simnao == "Não ":
        print("Já sabia, uma vez pobre, sempre pobre.")
        break
    else:
        simnao = input("BURRO!!!\nResponda \"sim\" ou \"não\"")
        simnao = simnao.title()
print("Responda abaixo com o número correspondente")
vg = input("Qual gostaria de ter?\n1) Xbox One\n2) Playstation 5\n3) Nintendo Switch\n4) PC Gamer")
while vg != "1" or vg != "2" or vg != "3" or vg != "4":

    if vg == "1":
        print("Xbox One?\nOs jogos dessa merda tem no PC também.\nGosta de desperdiçar dinheiro, por isso é pobre.")
        break
    elif vg == "2":
        print("Playstation 5?\nCom o dinheiro dessa merda você compra casa, carro e ainda sobra 1 pouco")
        break
    elif vg == "3":
        print("Nintendo Switch?\nEssa merda só tem jogos infantis!\nQuantos anos tem?\n9?")
        break
    elif vg == "4":
        print("PC Gamer?\nÉ...\nVocê tem cara de GAYmer mesmo, mas, não recomendo, muitos botões e você é muito burro.")
        print("Já viu quantas botões têm 1 teclado?\nMuitas letras e números.\nNão saberá pra que eles todos servem.")
        print("Não recomendo pra você nada que tenha mais de 2 botões e olhe lá.")
        break
    else:
        print("Mais burro impossível!")
        vg = input("Não sabe digitar número de 1 ao 4 ou não sabe o que quer dizer a palavra \"número\"?")
