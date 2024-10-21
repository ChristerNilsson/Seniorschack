Spelöppningen går snabbt att genomföra om man har tillgång till en databas med öppningar.

[Lichess Openings Explorer](https://lichess.org/analysis#explorer)

En metod är att ange aktuell ställning och se vilket drag som är vanligast.  
T ex spelas 1. e4 c5 2. Nf3 i 17% av alla partier. (45% * 46% * 82% = 17%)

Man kan välja mellan Over-The-Board 2200+ eller alla Lichess-partier.  
Man kan även ta med statistik över vinster, förluster och remier när man väljer bästa draget.  

Principiellt utseende av en spelöppningsdatabas:
```
1	2	3	4	5	6 (halvdrag)
e4 45%
	c5 46%
		Nf3 82%
		Nc3 8%
	e5 34%
		Nf3 92%
			Nc6 86%
				Bb5 66%
					a6 72%
					Nf6 20%
				Bc4 18 %
					Bc5 53%
					Nf6 43%
			Nf6 12%
		Bc4 3%
d4 36%
Nf3 10%
c4 7%
g3 1%
b3 0%
```

```
8 U V W X Y Z - _
7 M N O P Q R S T
6 E F G H I J K L
5 w x y z A B C D
4 o p q r s t u v
3 g h i j k l m n
2 8 9 a b c d e f
1 0 1 2 3 4 5 6 7
  a b c d e f g h
```

* Ett drag kan lagras med tre bytes. e2e4 => 0cs, c7c5 => 1Oy
	* halvdrag + frånruta + tillruta. (Procenten kan beräknas)
	* Då ryms en miljon drag på 3 Mb.
* Vill man variera sitt spel kan man låta slumpen spela in.
* Förr eller senare tar trädet slut.
	* Då börjar mittspelet.
