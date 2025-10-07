class Conta {
    agencia;
    numeroConta;
    saldo=0;
    depositar(valor) {
        this.saldo = this.saldo + valor;
    }
    sacar(valor) {
        let novoSaldo = this.saldo - valor;
        if (novoSaldo < 0) {
            return false;
        }
        this.saldo = novoSaldo;
        return true;
    }
}