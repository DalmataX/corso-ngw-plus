function valore() {
    let input;
    while (input !== "ESCI") {
        input = prompt("Inserisci un valore:");
        if (input !== "ESCI") {
            console.log("Hai inserito:", input);
        }
    }
    console.log("Hai terminato il programma.");
}
