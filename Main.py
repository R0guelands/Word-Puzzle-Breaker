from itertools import permutations
import numpy as np
import time


def main():
    class Func:
        contador = 0
        achadas = []
        palavras = []
        letras_org = []
        t0 = 0
        br = ""
        size = 0
        letras = ""
        size_max = 0

    def define_basics():
        while True:
            Func.br = str(input("Use Pt-BR or English dictionary? p/e: "))
            if Func.br != "p" and Func.br != "e":
                print("\nPlease choose one of the options\n")
                time.sleep(1)
                continue
            else:
                break
        while True:
            Func.letras = str(input("\nInput the letters without spaces: "))
            if " " in Func.letras:
                print("\nType the letters without spaces")
                time.sleep(1)
                continue
            else:
                Func.letras = Func.letras.lower()
                break
        while True:
            Func.size = int(input("\nType the minimun amount of syllables to be outputed (2, ...): "))
            if len(Func.letras) < 3 or Func.size < 2:
                print("\nChoose more letters")
                time.sleep(1)
                continue
            else:
                Func.size_max = int(input("\nType the maximum amount of syllables to be outputed: "))
                print("")
                break
        for x in range(len(Func.letras)):
            Func.letras_org.append(Func.letras[x])

    def lista(x):
        if Func.br == "p":
            arquivo = open('palavras_br.txt', 'r')
        if Func.br == "e":
            arquivo = open('palavras_ing.txt', 'r')
        Func.palavras = []
        for linhas in arquivo:
            linhas = linhas.replace('\n', '')
            linhas = linhas.lower()
            letras_org_2 = []
            for xx in range(0, len(linhas)):
                letras_org_2.append(linhas[xx])
            contained = [i for i in Func.letras_org if i in letras_org_2]
            if len(linhas) == x and len(contained) >= Func.size:
                Func.palavras.append(linhas)
        return

    def samples(casa):
        perm = np.array(list(permutations(Func.letras_org, casa)))
        return perm

    def process():
        Func.t0 = time.time()
        for casa in range(Func.size, Func.size_max + 1):
            t1 = time.time()
            sample = samples(casa)
            lista(casa)
            palavrass = []
            for montagem in sample:
                Func.palavra = ""
                for i in montagem:
                    Func.palavra += i
                palavrass.append(Func.palavra)
            contador1 = 0
            for item in palavrass:
                if item in Func.palavras and item not in Func.achadas:
                    Func.contador += 1
                    contador1 += 1
                    Func.achadas.append(item)
            t2 = time.time()
            print("{}/{} -> %.2fs / {} words found with {} syllables / {} possible words".format(casa, Func.size_max, contador1, casa, len(Func.palavras)) % (t2 - t1))
        print("\nNumber of words found: ", Func.contador)
        print("\nFound words:\n")
        for x in range(1, len(Func.achadas) + 1):
            print("{} - {}".format(x, Func.achadas[x - 1]))
        print("\nTime of processing: %.2fs" % (t2 - Func.t0))

    define_basics()
    process()


if __name__ == "__main__":
    main()
