Antag att vi har tio personer. Bilda en 10x10-matris med absoluta elodifferenser.  
Det räcker att ange 45 celler, eftersom matrisen är symmetrisk.

|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |elo|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 |   |  **3**| 50|144|181|203|275|303|307|308|2416
| 2 |  **3**|   | 47|141|178|200|272|300|304|305|2413
| 3 | 50| 47|   | **94**|131|153|225|253|257|258|2366
| 4 |144|141|**94**|   | 37| 59|131|159|163|164|2272
| 5 |181|178|131| 37|   |**22**| 94|122|126|127|2235
| 6 |203|200|153| 59|**22**|   | 72|100|104|105|2213
| 7 |275|272|225|131| 94| 72|   |**28**| 32| 33|2141
| 8 |303|300|253|159|122|100|**28**|   |  4|  5|2113
| 9 |307|304|257|163|126|104| 32|  4|   |**1**|2109
| 0 |308|305|258|164|127|105| 33|  5|**1**|   |2108

| |1|2|3|4|5|6|7|8|9|0|elo|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 |   | 1 | • | • | • | • | • | • | • | • | 2416
| 2 | 1 |   | • | • | • | • | • | • | • | • | 2413
| 3 | • | • |   | 1 | • | • | • | • | • | • | 2366
| 4 | • | • | 1 |   | • | • | • | • | • | • | 2272
| 5 | • | • | • | • |   | 1 | • | • | • | • | 2235
| 6 | • | • | • | • | 1 |   | • | • | • | • | 2213
| 7 | • | • | • | • | • | • |   | 1 | • | • | 2141
| 8 | • | • | • | • | • | • | 1 |   | • | • | 2113
| 9 | • | • | • | • | • | • | • | • |   | 1 | 2109
| 0 | • | • | • | • | • | • | • | • | 1 |   | 2108

Blossom föreslår att rond 1 spelas enligt ovan, eftersom totalsumman av de fem cellerna då blir så låg som möjligt.   (3 + 94 + 22 + 28 + 1 = 148)  
I Schweizer skulle denna summa bli 203 + 272 + 253 + 163 + 127 = 1018  
(I viss mån liknar detta ett sudoku eftersom rond 1 ska förekomma exakt en gång per rad och kolumn.)  


Bordslista
 | Bord||diff|
|:-:|-|-:|
|1|1 möter 2|3|
|2|3 möter 4|94|
|3|5 möter 6|22|
|4|7 möter 8|28|
|5|9 möter 0|1|

I nästa rond tar man bort de celler som spelats eller har förbjuden färgmatchning och får nya par.  

[Wikipedia](https://en.wikipedia.org/wiki/Blossom_algorithm) 