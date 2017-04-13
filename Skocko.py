from random import randint as rnd
lista = [0, 0, 0, 0]

def prodjiKroz(x):
	cTacno = 0
	cMesto = 0
	cOmasaj = 0
	for y in range(0, len(x)):
		if x[y] == 1:
			cTacno += 1
		elif x[y] == 0:
			cMesto += 1
		else:
			cOmasaj += 1
	if cTacno != 4:
		return "Pogodjenih: {0}\nNa mestu nije: {1}\nDok je promaseno: {2}\n".format(cTacno, cMesto, cOmasaj)
	else:
		return "Svaka cast! Pogodili ste kombinaciju"

def proveri(a, b):
	p = [-1, -1, -1, -1]
	global lista
	for i in range(0, len(b)):
		lista[i] = b[i]
	if a[0] == b[0]:
		p[0] = 1
		lista[0] = 99
	if a[1] == b[1]:
		p[1] = 1
		lista[1] = 99
	if a[2] == b[2]:
		p[2] = 1
		lista[2] = 99
	if a[3] == b[3]:
		p[3] = 1
		lista[3] = 99
	for i in range(0, 4):
		if p[i] == -1:
			for j in range(0, len(lista)):
				if a[i] == lista[j]:
					p[i] = 0
					lista[j] = 99
	for i in range(0, 4):
		for j in range(0, 4):
			if p[i] > p[j]:
				p[i], p[j] = p[j], p[i]
	return p

def main():
	komb = [0, 0, 0, 0]
	br = 7
	for i in range(0, 4):
		komb[i] = rnd(1, 7)
	//print (komb)
	while True:
		br -= 1
		inp = input("Unesite vasu kombinaciju: ")
		inparr = []
		inpp = int(inp)
		inparr.append((int)((inpp / 1000)))
		inparr.append((int)((inpp / 100) % 10))
		inparr.append((int)((inpp % 100) / 10))
		inparr.append((int)(inpp % 10))
		p = proveri(inparr, komb)
		if prodjiKroz(p) == "Svaka cast! Pogodili ste kombinaciju":
			print(prodjiKroz(p))
			break
		else:
			print (prodjiKroz(p))
		if br == 0:
			print("Nemate vise pokusaja")
			print(komb)
			break
		elif br > 1:
			print("Imate jos {} pokusaja".format(br))
		else:
			print("Imate jos {} pokusaj".format(br))
		
if __name__ == '__main__':
	main()
