function listaSpesa() {
    let lista = ['biscotti', 'latte', 'pasta'];
    let i = true;
  
    while (i) {
      let prodotto = prompt("Cosa vuoi aggiungere alla lista della spesa?");
  
      if (prodotto) {
        lista.push(prodotto);
        alert("Prodotto aggiunto alla lista!");
      }
  
      let risposta = prompt("Vuoi aggiungere altri prodotti? Rispondi con 'SI' per continuare o 'NO/ESCI' per uscire.");
  
      if (risposta === "NO" || risposta === "ESCI") {
        i = false;
        console.log("Lista finale:", lista);
      }
    }
  }
  