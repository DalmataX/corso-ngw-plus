var __extends =
  (this && this.__extends) ||
  (function () {
    var extendStatics = function (d, b) {
      extendStatics =
        Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array &&
          function (d, b) {
            d.__proto__ = b;
          }) ||
        function (d, b) {
          for (var p in b)
            if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p];
        };
      return extendStatics(d, b);
    };
    return function (d, b) {
      if (typeof b !== "function" && b !== null)
        throw new TypeError(
          "Class extends value " + String(b) + " is not a constructor or null"
        );
      extendStatics(d, b);
      function __() {
        this.constructor = d;
      }
      d.prototype =
        b === null
          ? Object.create(b)
          : ((__.prototype = b.prototype), new __());
    };
  })();
var Veicolo = /** @class */ (function () {
  function Veicolo(marca, modello, velocitaMassima, targa) {
    this.marca = marca;
    this.modello = modello;
    this.velocitaMassima = velocitaMassima;
    this._targa = targa;
  }
  Object.defineProperty(Veicolo.prototype, "targa", {
    get: function () {
      return this._targa;
    },
    enumerable: false,
    configurable: true,
  });
  Veicolo.prototype.descrizione = function () {
    return "Veicolo "
      .concat(this.marca, " ")
      .concat(this.modello, ", velocita' massima: ")
      .concat(this.velocitaMassima, " km/h");
  };
  return Veicolo;
})();
var Auto = /** @class */ (function (_super) {
  __extends(Auto, _super);
  function Auto(marca, modello, velocitaMassima, targa, numeroPorte) {
    var _this =
      _super.call(this, marca, modello, velocitaMassima, targa) || this;
    _this.numeroPorte = numeroPorte;
    return _this;
  }
  Auto.prototype.descriviAuto = function () {
    console.log(
      ""
        .concat(this.descrizione(), ", numero di porte: ")
        .concat(this.numeroPorte)
    );
  };
  return Auto;
})(Veicolo);
var miaAuto = new Auto("Fiat", "500", 180, "AB123CD", 3);
console.log(miaAuto.descrizione());
miaAuto.descriviAuto();
console.log("Targa:", miaAuto.targa);
var lambo = new Auto("Lamborghini", "Huracan", 325, "XB153CL", 2);
console.log(lambo.descrizione());
lambo.descriviAuto();
console.log("Targa:", lambo.targa);
var tuaAuto = new Auto("Toyota", "Aygo X", 160, "KK109PM", 5);
console.log(tuaAuto.descrizione());
tuaAuto.descriviAuto();
console.log("Targa:", tuaAuto.targa);
