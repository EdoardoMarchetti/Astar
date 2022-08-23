Istruzioni per l'utilizzo del codice:

1) Creazione delle liste dei nodi e degli archi:
	- Tramite file: usando la classe FileReader è possibile creare le liste a partire da dei documenti di testo.
	  Nel file dei nodi ogni riga deve essere della forma ID X Y
	  Nel file degli archi ogni riga deve essere nella forma ID Start END COST
	- Tramite la creazioni di oggetti Node e Edge: è possibile altrimenti creare due liste tramite manualmente.

2) Creazione del Grafo:
	- Creare un oggetto di tipo Grafo passando al costruttore della classe le due liste create al passo 1

3) Definizione del problema:
	- Creare un istanza della classe Problem indicando il grafo, l'id del nodo che rappresenta lo stato iniziale 
	  e l'id del nodo che rappresenta lo stato di goal

4) Invocare la procedura richiesta passandole l'oggeto problema creato al passo precedente.

5) Stampa dei risultati:
	- Nel codice consegnato sono presenti delle linee di codice per stampare a video i risultati ottenuti, 
	  ovvero il numero di nodi che appartengono alla soluzione, il numero di nodi esplorati, il costo della soluzione
	  e il tempo impiegato per la risoluzione dell'algoritmo. 
	 