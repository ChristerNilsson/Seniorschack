*Datorschack består i princip av addition och subtraktion av heltal*

Mittspelet är komplexare än öppningen och slutspelet.  
Här måste alla drag genereras och ett träd genomsökas.  
Att utvärdera ställningen i schack är komplicerat.  
Svag evaluering kan kompenseras med att söka djupare.  

### Minimax 

![Minimax](X_minimax.png)

### Evaluering i schack

* Material (t ex P=100,N=280,B=350,R=500,Q=900)
* Piece Square Tables
	* Vit vs Svart
	* bonde, springare, löpare, torn, dam, kung
	* 64 rutor
	* Spelöppning vs Slutspel (interpolation)
* Mobilitet
	* Hur många drag spelaren kan göra i den givna positionen
* Kungens säkerhet
* Bondestruktur
	* Dubbelbönder
	* Ensamma bönder
	* Fribönder
* osv.

[Minimax](minimax.html)  

[Piece Square Table](Piece_Square_Table.html)

### Länkar

[Wikipedia](https://en.wikipedia.org/wiki/Kalah)
[Kalaha](https://christernilsson.github.io/Lab/2019/118-Kalaha/)
[Binärt Träd](X_tree.svg)
[Nokia 3310](https://youtube.com/clip/Ugkxax12m2ISro9LvHjkgzt_ZY9GwCM0f3Vh?si=J4J9fmi1io-Wgexb)
[Minimax - källkod](https://github.com/ChristerNilsson/Lab/blob/master/2019/118-Kalaha/coffee/minimax.coffee)
[Chess Programming](https://www.chessprogramming.org/Main_Page)
[Chess.stackexchange](https://chess.stackexchange.com)
[Python Chess](https://python-chess.readthedocs.io/en/latest)

