function valore() {
    let input;
    while (true) {
        input = prompt("Inserisci un valore:");
        if (input === "ESCI") {
            alert("Hai terminato il programma.");
            break;
        }
        alert("Hai inserito: " + input);
    }
}

