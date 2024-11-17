class Conta {
  numero: string;
  saldo: number;

  constructor(numero: string, saldo: number) {
    this.numero = numero;
    this.saldo = saldo;
  }


  sacar(valor: number): boolean {
    if (this.saldo >= valor) {
      this.saldo -= valor;
      return true;
    } else {
      console.log(`Saque de R$${valor} não realizado. Saldo insuficiente.`);
      return false;
    }
  }


  transferir(destino: Conta, valor: number): boolean {
    if (this.sacar(valor)) {
      destino.saldo += valor;
      console.log(`Transferência de R$${valor} realizada para a conta ${destino.numero}.`);
      return true;
    } else {
      console.log(`Transferência de R$${valor} não realizada. Saldo insuficiente na conta ${this.numero}.`);
      return false;
    }
  }

  consultarSaldo(): number {
    return this.saldo;
  }
}


const conta1 = new Conta("1", 100);
const conta2 = new Conta("2", 50);


console.log("Saque R$30 da conta 1:", conta1.sacar(30)); 
console.log("Saldo da conta 1:", conta1.consultarSaldo()); 
console.log("Saque R$80 da conta 1:", conta1.sacar(80)); 
console.log("Saldo da conta 1:", conta1.consultarSaldo()); 


console.log("\nTransferência de R$40 da conta 1 para conta 2:", conta1.transferir(conta2, 40)); 
console.log("Saldo da conta 1:", conta1.consultarSaldo()); 
console.log("Saldo da conta 2:", conta2.consultarSaldo()); 

console.log("\nTransferência de R$50 da conta 1 para conta 2:", conta1.transferir(conta2, 50)); 
console.log("Saldo da conta 1:", conta1.consultarSaldo()); 
console.log("Saldo da conta 2:", conta2.consultarSaldo()); 
