# PA3/Pos Tagging Program
Report Project:
<p align = "center">
  <a href = "https://github.com/romerotac/PA3"> English </a>|
  <span>Italian</span>
</*>

La prima parte del progetto fa uso del programma tagger.py e di due file di testo.
Il programma deve essere eseguito in questo modo:

python tagger.py pos-train.txt pos-test.txt > pos-test-with-tags.txt

Dove pos-train.txt consiste nel file di testo che viene utilizzato per allenare il modello a riconoscere specifici associazioni fra word|tag (o parola|classe), e post-test.txt e il documento di testo contenente parola senza nessuna associazione. Con l'esecuzione del programma si otterrà un nuovo file di testo chiamato pos-test-with-tags.txt la quale consiste nel file pos-test ma questa volta con un'appropriata classificazione.

Nota –Regole–:
Durante l 'esecuzione del programma tagger.py, viene selezionata la prima regola. Ci sono in totale 5, e queste possono essere modificate all’interno del codice sotto la funzione rules. Ogni regola può incrementare o decrementare la precisione del modello.

Nota –create_before_after:
Questa funzione viene utilizzata per creare un file di testo contenente una tabella con il numero totale di volte un tag e seguita da un’altra. Questo può essere utile nella creazione di regole.

La seconda e ultima parte del progetto, consiste nel valutare l’efficienza del modello creato.
Il programma deve essere eseguito in questo modo:

python scorer.py pos-test-with-tags.txt pos-test-key.txt > pos-tagging-report.txt

Dove si utilizza il file di testo creato in precedenza e lo si compara con un secondo file test identico al primo, ma con la corretta associazione. Una volta eseguito il programma otterremo un file di testo contenente il numero totale di associazioni corrette comparato con il numero totale di parole nel testo, così come la percentuale di accuratezza e una tabella corrispondente al numero di associazione correte e non corrette per ogni tag.

P.S Per regole si intende tutte le soluzioni che possono incrementare l’accuratezza del programma. Queste possono essere basati sul regex o la dipendenza fra diversi tag

"***Esempi di file di testo inerenti alla seconda parte si trovano in <a href = "https://github.com/romerotac/PA3/tree/master/file_report"> file_report <a> e nella cartella tag_with_rules puoi trovare file di testo inerenti alla prima parte del programma ***"
