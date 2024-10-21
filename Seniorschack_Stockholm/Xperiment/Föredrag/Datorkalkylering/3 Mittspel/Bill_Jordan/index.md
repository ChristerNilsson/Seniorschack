[Try it!](https://christernilsson.github.io/JavaScript-Chess/)

Bill Jordans program finns på [github](https://github.com/billjordanchess/JavaScript-Chess) och även som en [bok](https://www.amazon.com/How-Write-JavaScript-Chess-Engine/dp/B08L3ZWHXN).  
Det består av 1796 rader [Javascriptkod](https://github.com/billjordanchess/JavaScript-Chess/blob/master/engine2.js).  

Programmet använder sig av följande tekniker:

* Draggenerering
* Iterativ fördjupning
	* en nivå, två nivåer, osv
* Minimax med alpha beta
	* Alpha-Beta ger ca ett halvdrag extra, med samma tid.
* Dragsortering
	* Hjälper alpha-beta att kapa grenar
* Hashtabeller
	* Hanterar dragomkastning
* Piece Square Tables

## Mitt omdöme

* Jordans bok innehåller mest kod + kommentarer. Koden saknade indentering och blev därmed svårare att läsa. Bill har lyssnat på min kritik och detta åtgärdas i en kommande upplaga.

* Programmets spelstyrka känns helt ok. Starkare spelare tvingas dock öka sökdjupet och då blir programmet långsammare. 

* KRK löses mha fem nivåer, utan slutspelsdatabas. Den kortaste lösningen enligt Syzygy hittas oftast inte, men uppgiften löses. Även KQK, KBBK och KBNK löses. KQKR löstes dock ej.
