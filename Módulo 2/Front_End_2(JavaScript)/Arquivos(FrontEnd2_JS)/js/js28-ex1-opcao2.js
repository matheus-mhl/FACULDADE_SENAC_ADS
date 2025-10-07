class Conta {
    #agencia;
    #numeroConta;
    #saldo=0;
    get agencia() {
        return this.#agencia;
    }
    set agencia(agencia) {
        this.#agencia = agencia;
    }
    get numeroConta() {
        return this.#numeroConta;
    }
    set numeroConta(numeroConta) {
        this.#numeroConta = numeroConta;
    }
    get saldo() {
        return this.#saldo;
    }
    set saldo(saldo) {
        this.#saldo = saldo;
    }
    depositar(valor) {
        this.#saldo = this.#saldo + valor;
    }
    sacar(valor) {
        let novoSaldo = this.#saldo - valor;
        if (novoSaldo < 0) {
            return false;
        }
        this.#saldo = novoSaldo;
        return true;
    }
}