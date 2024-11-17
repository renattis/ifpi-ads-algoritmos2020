class Jogador {
  força: number;
  nível: number;
  pontos: number;

  constructor(força: number, nível: number, pontos: number) {
    this.força = força;
    this.nível = nível;
    this.pontos = pontos;
  }

 
  calcularAtaque(): number {
    return this.força * this.nível;
  }

  
  atacar(atacado: Jogador): void {
    if (!atacado.estaVivo()) {
      console.log(`Jogador atacado já está fora de combate.`);
      return;
    }

    const dano = this.calcularAtaque();
    atacado.pontos -= dano;

    console.log(
      `Jogador atacou! Dano: ${dano}. Pontos do atacado agora: ${Math.max(
        atacado.pontos,
        0
      )}.`
    );
  }


  estaVivo(): boolean {
    return this.pontos > 0;
  }


  toString(): string {
    return `Força: ${this.força}, Nível: ${this.nível}, Pontos: ${this.pontos}`;
  }
}


const jogador1 = new Jogador(10, 3, 100);
const jogador2 = new Jogador(8, 4, 120);

console.log("Jogador 1:", jogador1.toString());
console.log("Jogador 2:", jogador2.toString());

console.log("\n** Batalha Iniciada **");


jogador1.atacar(jogador2);
console.log("Jogador 2 após ataque:", jogador2.toString());


jogador2.atacar(jogador1);
console.log("Jogador 1 após ataque:", jogador1.toString());


console.log("\n** Resultado Final **");
if (jogador1.pontos > jogador2.pontos) {
  console.log("Jogador 1 venceu a batalha!");
} else if (jogador2.pontos > jogador1.pontos) {
  console.log("Jogador 2 venceu a batalha!");
} else {
  console.log("A batalha terminou empatada!");
}
