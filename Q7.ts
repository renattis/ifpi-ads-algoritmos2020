class Triangulo {
  ladoA: number;
  ladoB: number;
  ladoC: number;

  constructor(ladoA: number, ladoB: number, ladoC: number) {
    this.ladoA = ladoA;
    this.ladoB = ladoB;
    this.ladoC = ladoC;
  }

  // Verifica se os lados formam um triângulo válido
  formaTriangulo(): boolean {
    const { ladoA, ladoB, ladoC } = this;
    return (
      Math.abs(ladoB - ladoC) < ladoA && ladoA < ladoB + ladoC &&
      Math.abs(ladoA - ladoC) < ladoB && ladoB < ladoA + ladoC &&
      Math.abs(ladoA - ladoB) < ladoC && ladoC < ladoA + ladoB
    );
  }

  // Verifica se é um triângulo isósceles
  ehIsoceles(): boolean {
    if (!this.formaTriangulo()) return false;
    return (
      this.ladoA === this.ladoB ||
      this.ladoA === this.ladoC ||
      this.ladoB === this.ladoC
    );
  }

  // Verifica se é um triângulo equilátero
  ehEquilatero(): boolean {
    if (!this.formaTriangulo()) return false;
    return this.ladoA === this.ladoB && this.ladoB === this.ladoC;
  }

  // Verifica se é um triângulo escaleno
  ehEscaleno(): boolean {
    if (!this.formaTriangulo()) return false;
    return this.ladoA !== this.ladoB && this.ladoA !== this.ladoC && this.ladoB !== this.ladoC;
  }
}

// Instanciando diferentes triângulos e testando os métodos
const triangulo1 = new Triangulo(3, 4, 5);
console.log("Triângulo 1 forma triângulo?", triangulo1.formaTriangulo()); // true
console.log("Triângulo 1 é isósceles?", triangulo1.ehIsoceles()); // false
console.log("Triângulo 1 é equilátero?", triangulo1.ehEquilatero()); // false
console.log("Triângulo 1 é escaleno?", triangulo1.ehEscaleno()); // true

const triangulo2 = new Triangulo(5, 5, 5);
console.log("\nTriângulo 2 forma triângulo?", triangulo2.formaTriangulo()); // true
console.log("Triângulo 2 é isósceles?", triangulo2.ehIsoceles()); // true
console.log("Triângulo 2 é equilátero?", triangulo2.ehEquilatero()); // true
console.log("Triângulo 2 é escaleno?", triangulo2.ehEscaleno()); // false

const triangulo3 = new Triangulo(10, 2, 2);
console.log("\nTriângulo 3 forma triângulo?", triangulo3.formaTriangulo()); // false
console.log("Triângulo 3 é isósceles?", triangulo3.ehIsoceles()); // false
console.log("Triângulo 3 é equilátero?", triangulo3.ehEquilatero()); // false
console.log("Triângulo 3 é escaleno?", triangulo3.ehEscaleno()); // false
