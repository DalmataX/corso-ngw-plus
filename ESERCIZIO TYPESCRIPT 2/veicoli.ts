class Veicolo {
  private readonly _targa: string;

  constructor(
    public marca: string,
    public modello: string,
    public velocitaMassima: number,
    targa: string
  ) {
    this._targa = targa;
  }

  get targa(): string {
    return this._targa;
  }

  descrizione(): string {
    return `Veicolo ${this.marca} ${this.modello}, velocita' massima: ${this.velocitaMassima} km/h`;
  }
}

class Auto extends Veicolo {
  constructor(
    marca: string,
    modello: string,
    velocitaMassima: number,
    targa: string,
    public numeroPorte: number
  ) {
    super(marca, modello, velocitaMassima, targa);
  }

  descriviAuto(): void {
    console.log(`${this.descrizione()}, numero di porte: ${this.numeroPorte}`);
  }
}

const miaAuto = new Auto("Fiat", "500", 180, "AB123CD", 3);
console.log(miaAuto.descrizione());
miaAuto.descriviAuto();
console.log("Targa:", miaAuto.targa);

const lambo = new Auto("Lamborghini", "Huracan", 325, "XB153CL", 2);
console.log(lambo.descrizione());
lambo.descriviAuto();
console.log("Targa:", lambo.targa);

const tuaAuto = new Auto("Toyota", "Aygo X", 160, "KK109PM", 5);
console.log(tuaAuto.descrizione());
tuaAuto.descriviAuto();
console.log("Targa:", tuaAuto.targa);
