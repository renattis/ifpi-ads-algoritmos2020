class Equipamento {
  private ligado: boolean; // Atributo ligado (boolean)

  constructor() {
    this.ligado = false; // Inicialmente desligado
  }

  // Liga o equipamento se não estiver ligado
  liga(): void {
    if (!this.ligado) {
      this.ligado = true;
      console.log("Equipamento ligado.");
    } else {
      console.log("Equipamento já está ligado.");
    }
  }

  // Desliga o equipamento se não estiver desligado
  desliga(): void {
    if (this.ligado) {
      this.ligado = false;
      console.log("Equipamento desligado.");
    } else {
      console.log("Equipamento já está desligado.");
    }
  }

  // Inverte o estado do equipamento
  inverte(): void {
    this.ligado = !this.ligado;
    console.log(`Equipamento ${this.ligado ? "ligado" : "desligado"}.`);
  }

  // Retorna se o equipamento está ligado
  estaLigado(): boolean {
    return this.ligado;
  }
}

// Testando a classe Equipamento
const equipamento = new Equipamento();

// Testes dos métodos
console.log("Inicialmente ligado?", equipamento.estaLigado()); // false
equipamento.liga(); // Equipamento ligado.
equipamento.liga(); // Equipamento já está ligado.
console.log("Ligado?", equipamento.estaLigado()); // true

equipamento.desliga(); // Equipamento desligado.
equipamento.desliga(); // Equipamento já está desligado.
console.log("Ligado?", equipamento.estaLigado()); // false

equipamento.inverte(); // Equipamento ligado.
equipamento.inverte(); // Equipamento desligado.
