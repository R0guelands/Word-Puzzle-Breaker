from itertools import permutations
import numpy as np
import time

def main():
		class func:
				contador = 0
				achadas = []
				palavras = []
				letras_org = []
				t0 = 0
				br = ""
				size = 0
				letras = ""

		def define_basics():
				while True:
					func.br =  str(input("Use Pt-BR or English dictionary? p/e: "))
					if func.br != "p" and func.br != "e":
							print("\nPlease choose one of the options\n")
							time.sleep(1)
							continue
					else:
							break
				while True:
						func.letras = str(input("\nInput the letters without spaces: "))
						if " " in func.letras:
								print("\nType the letters without spaces")
								time.sleep(1)
								continue
						else:
								func.letras = func.letras.lower()
								break
				while True:
						func.size = int(input("\nType the minimun amount of syllables to be outputed (2, ...): "))
						if len(func.letras) < 3 or func.size < 2:
								print("\nChoose more letters")
								time.sleep(1)
								continue
						else:
								print("")
								break
				for x in range(len(func.letras)):
						func.letras_org.append(func.letras[x])

		def lista(x):
				if func.br == "p":
						arquivo = open('palavras_br.txt', 'r')
				if func.br == "e":
						arquivo = open('palavras_ing.txt', 'r')		
				func.palavras = []
				for linhas in arquivo:
						linhas = linhas.replace('\n', '')
						linhas = linhas.lower()
						letras_org_2 = []
						for xx in range(0, len(linhas)):
								letras_org_2.append(linhas[xx])
						contained = [i for i in func.letras_org if i in letras_org_2]
						if len(linhas) == x and len(contained) >= func.size:
								func.palavras.append(linhas)
				return

		def samples(casa):
				perm = np.array(list(permutations(func.letras_org, casa)))
				return perm
		
		def process():
				func.t0 = time.time()
				for casa in range(func.size, len(func.letras_org) + 1):
						t1 = time.time()
						sample = samples(casa)
						lista(casa)
						palavrass = []
						for montagem in sample:
								func.palavra = ""
								for i in montagem:
										func.palavra += i
								palavrass.append(func.palavra)
						contador1 = 0
						for item in palavrass:
								if item in func.palavras and item not in func.achadas:
										func.contador += 1
										contador1 += 1
										func.achadas.append(item)
						t2 = time.time()
						print("{}/{} -> %.2fs / {} words found with {} syllables / {} possible words".format(casa, len(func.letras_org), contador1, casa, len(func.palavras) ) % (t2 - t1))
				print("\nNumber of words found: ", func.contador)
				print("\nFound words:\n")
				for x in range(1, len(func.achadas) + 1):
						print("{} - {}".format(x, func.achadas[x - 1]))
				print("\nTime of processing: %.2fs" % (t2 - func.t0))
		
		define_basics()
		process()

if __name__ == "__main__":
		main()
