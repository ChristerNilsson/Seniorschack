<style>
	table {
		border-spacing: 0;
		border-collapse: collapse;
		/* width: 400px;
		height: 400px; */
		font-size: 32px;
		color: black;
	}

	th {
		color: white;
	}

	td {
		width: 50px;
		height: 50px;
	}

	table tr:nth-child(even) td:nth-child(odd),
	table tr:nth-child(odd) td:nth-child(even) {
		background-color: #b58863; /* Mörkbruna rutor */
	}

	table tr:nth-child(even) td:nth-child(even),
	table tr:nth-child(odd) td:nth-child(odd) {
		background-color: #f0d9b5; /* Ljusa rutor */
	}
</style>

Genom att ge ett värde för varje pjäs på varje ruta vid varje tillfälle,  
kan man räkna ut värdet av en viss given ställning.

* Enkelt att införa 
* Bra prestanda, pga inkrementell uppdatering
* Brädets rutor = 64
* Antal olika pjäser = 6
* Antal färger = 2
* En tabell för öppning, en för slutspel = 2
* Totalt ger detta 64 * 6 * 2 * 2 = 1536 heltal
* Interpolera mellan dessa mha material,
	* Spelöppning: 2 * (9 + 5 + 3 + 3 + 8) = 56
	* Slutspel: 0

## Torn

| a | b | c | d | e | f | g | h |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|  4|  4|  4|  6|  6|  4|  4|  4|
|  0|  0|  0|  0|  0|  0|  0|  0|
|  0|  0|  0|  0|  0|  0|  0|  0|
|  0|  0|  0|  0|  0|  0|  0|  0|
|  0|  0|  0|  0|  0|  0|  0|  0|
|  0|  0|  0|  0|  0|  0|  0|  0|
| 20| 20| 20| 20| 20| 20| 20| 20|
| 10| 10| 10| 10| 10| 10| 10| 10|

## Kung, slutspel

| a | b | c | d | e | f | g | h |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|  0|  8| 16| 18| 18| 16|  8|  0|
|  8| 16| 24| 32| 32| 24| 16|  8|
| 16| 24| 32| 40| 40| 32| 24| 16|
| 25| 32| 40| 48| 48| 40| 32| 25|
| 25| 32| 40| 48| 48| 40| 32| 25|
| 16| 24| 32| 40| 40| 32| 24| 16|
|  8| 16| 24| 32| 32| 24| 16|  8|
|  0|  8| 16| 18| 18| 16|  8|  0|

## Undersök!

| a | b | c | d | e | f | g | h |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   | ♚|   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   | ♔|   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   | ♖|   |   |   |   |

* Utgående från
	* Kc3, Rd1 (vit)
	* Kf6 (svart)
	* FEN: 8/8/5k2/8/8/2K5/8/3R4 w - - 0 1
	* Tornet värderas till 500 centipawns

* Hur mycket ändras evalueringen av Kd4?
* Hur mycket ändras evalueringen av Rd8?
* Hur mycket ändras evalueringen av Kg6?
* Vits tre bästa drag är:
	* Kd4, Rd5 och Re1
	* Hur mycket ändras evalueringen av dessa?
* Hur hanterar Jordans program detta slutspel?
	* Hur få nivåer behöver användas?
* Hur skulle du vilja förbättra matriserna ovan?

[Schackprogram](https://christernilsson.github.io/JavaScript-Chess/)  
[Bill Jordan](Bill_Jordan)  
[Simplified Evaluation Function](https://www.chessprogramming.org/Simplified_Evaluation_Function)  
[Piece-Square Tables](https://www.chessprogramming.org/Piece-Square_Tables)  

```
♟♞♝♜♛♚     ♙♘♗♖♕♔
```
