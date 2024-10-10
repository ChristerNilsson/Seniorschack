* A
	* B e4
		* C e5
			* D Nf3
			* E Bc4
		* F c5
			* G Nf3
			* H Nc3
	* I d4
		* J d5
			* K Nf3
			* L c4
		* M Nf6
			* N Nf3
			* O c4

Ovan har vi ett litet träd i fyra nivåer.  
Förgreningsfaktorn är två.  
I verkligheten kan den ofta vara 20-40.  
Antalet noder är femton.  
Antalet löv är åtta.  
A anger utgångsläget, i detta fall befinner vi oss i spelöppningen,  
men det skulle kunna vara vilken ställning som helst.  
Dragen som visas är de två mest frekventa.  

* A
	* B e4
		* C e5
			* D Nf3 <red>-5</red>
			* E Bc4 <red>-4</red>
		* F c5
			* G Nf3 <red>1</red>
			* H Nc3 <red>2</red>
	* I d4
		* J d5
			* K Nf3 <red>1</red>
			* L c4 <red>9</red>
		* M Nf6
			* N Nf3 <red>4</red>
			* O c4 <red>3</red>

Här har löven utvärderats.  
Positivt tal innebär att vit står bättre,  
negativt att svart leder.  

Uppgiften är nu att låta de maximala värdena sippra uppåt en nivå i trädet.  
Då får vi:  

* A
	* B e4
		* C e5  <red>-4</red>
			* D Nf3 -5
			* E Bc4 -4
		* F c5 <red>2</red>
			* G Nf3 1
			* H Nc3 2
	* I d4
		* J d5 <red>9</red>
			* K Nf3 1
			* L c4 9
		* M Nf6 <red>4</red>
			* N Nf3 4
			* O c4 3

Därefter är det svarts tur och svart väljer de mest negativa dragen:  

* A
	* B e4 <red>-4</red>
		* C e5 -4
			* D Nf3 -5
			* E Bc4 -4
		* F c5 2
			* G Nf3 1
			* H Nc3 2
	* I d4 <red>4</red>
		* J d5 9
			* K Nf3 1
			* L c4 9
		* M Nf6 4
			* N Nf3 4
			* O c4 3

Slutligen är det vits tur och då maximeras det:  

* A <red>4</red>
	* B e4 -4
		* C e5 -4
			* D Nf3 -5
			* E Bc4 -4
		* F c5 2
			* G Nf3 1
			* H Nc3 2
	* I d4 <red>4</red>
		* J d5 9
			* K Nf3 1
			* L c4 9
		* M Nf6 <red>4</red>
			* N Nf3 <red>4</red>
			* O c4 3

Vit väljer alltså nod I, d4, med värdet 4.  
Vi ser också att huvudspåret (Principal Variation) blir:  

+4 1. d4 Nf6 2. Nf3

I nedanstående analys ser vi fem huvudspår och att matt i två drag är oundvikligt.  
Lägg märke till att Stockfish sökt igenom tretton miljoner ställningar per sekund.  
och gått igenom 32 nivåer i trädet.  

![Lichess](Minimax.png)