function aggiungiProdotto(lista) {
    let prodotto = prompt("Cosa vuoi aggiungere alla lista della spesa?");
    if (prodotto) {
      lista.push(prodotto);
      alert("Prodotto aggiunto alla lista!");
    }
  }
  
  function rimuoviUltimoProdotto(lista) {
    if (lista.length > 0) {
      let prodottoRimosso = lista.pop();
      console.log(`Prodotto rimosso: ${prodottoRimosso}`);
      alert(`Prodotto rimosso dalla lista: ${prodottoRimosso}`);
    } else {
      alert("La lista e' vuota, non c'e' nulla da rimuovere.");
    }
  }
  
  function listaSpesa() {
    let lista = [];
    let continua = true;
  
    while (continua) {
      let scelta = prompt("Vuoi AGGIUNGERE o ELIMINARE l'ultimo prodotto dalla lista? (Inserisci AGGIUNGERE, ELIMINARE o ESCI)");
  
      switch (scelta) {
        case "AGGIUNGERE":
          aggiungiProdotto(lista);
          break;
        case "ELIMINARE":
          rimuoviUltimoProdotto(lista);
          break;
        case "ESCI":
          continua = false;
          console.log("Lista finale:", lista);
          alert("Lista finale: " + lista.join(", "));
          break;
        default:
          alert("Opzione non valida. Scegliere tra AGGIUNGERE, ELIMINARE o ESCI.");
          break;
      }
    }
  }
  
  listaSpesa();
  