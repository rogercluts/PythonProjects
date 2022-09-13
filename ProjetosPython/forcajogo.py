from random import randint
def pegar_letra_digitada():
	letra = ""
	while letra == "":
		letra = input("Digite uma letra: ")
		if len(letra) == 0 or len(letra) > 1:
			letra = ""
			print("Letra digitada inválida.")
	return letra
def exibir_palavra(palavra, letras):
	exibicao_palavra = ""
	for letra in palavra:
		if letras.count(letra) > 0:
			exibicao_palavra += letra
		else:
			exibicao_palavra += "_"
		exibicao_palavra += " "
	print(exibicao_palavra)
palavras = [
	"revista",
	"papel",
	"humano",
	"caneta",
	"toalha"
]
acertos = 0
erros_permitidos = 6
erros = 0
palavra_sorteada = palavras[randint(0, len(palavras) - 1)]
letras_digitadas = []
print("A palavra sorteada possui {} letras.".format(len(palavra_sorteada)))
exibir_palavra(palavra_sorteada, letras_digitadas)
print("Erros permitidos: {}".format(erros_permitidos))
while True:
	letra_digitada = pegar_letra_digitada()
	if letras_digitadas.count(letra_digitada) > 0:
		print("Você já informou essa letra.")
	else:
		letras_digitadas.append(letra_digitada)
		exibir_palavra(palavra_sorteada, letras_digitadas)
		if palavra_sorteada.count(letra_digitada) == 0:
			erros += 1
			print("Você errou pela {}ª vez. Tente de novo!".format(erros))
			if erros == erros_permitidos:
				print("Você perdeu o jogo.")
				print("A palavra era: {}.".format(palavra_sorteada))
				break
		else:
			acertos += palavra_sorteada.count(letra_digitada)
			if acertos == len(palavra_sorteada):
				print("Você acertou a palavra. Parabéns!")
				print("Você precisou de {} tentativas para isso.".format(len(letras_digitadas)))
				break