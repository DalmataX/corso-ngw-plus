let listaSpesa = {};

function aggiungiElemento() {
    let elemento = prompt("Inserisci un elemento:");
    let quantita = prompt("Inserisci la quantita':");
    listaSpesa[elemento] = quantita;
    alert(`Aggiunto alla lista.`);
    visualizzaLista();
}

function rimuoviElemento() {
    let elemento = prompt("Inserisci l'elemento da rimuovere:");
    delete listaSpesa[elemento];
    alert(`Rimosso dalla lista!`);
    visualizzaLista();
}

function visualizzaLista() {
    let lista = [];
    lista.push("Lista della Spesa:");
    for (let item in listaSpesa) {
        lista.push(`${item} : ${listaSpesa[item]}`);
    }
    alert(lista.join(''));
}

function gestisciLista() {
    let scelta;
    do {
        scelta = prompt("Scegli un'operazione: 1. Aggiungi | n2. Rimuovi | 3. Visualizza | 4. Esci");
        switch (scelta) {
            case '1':
                aggiungiElemento();
                break;
            case '2':
                rimuoviElemento();
                break;
            case '3':
                visualizzaLista();
                break;
            case '4':
                alert("Uscita dal programma.");
                break;
            default:
                alert("Scelta non valida.");
        }
    } while (scelta !== '4');
}
