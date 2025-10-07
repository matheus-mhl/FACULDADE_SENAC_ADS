function exibirValorA() {
    alert(`O valor da variável a é " ${a} e seu tipo é ${typeof a}`); //alerado em sala e aula, o código nao está rodando ao tentar abrir o js2.html, *verificar pq*
}
function alterarValorA() {
    var a = "João"; // Escopo de função
    alert(`Valor da variável a foi alterado localmente para ${a}`);
}
function exibirValorB() {
    alert("O valor da variável b é " + b + " e seu tipo é " + typeof b);
}
function alterarValorB() {
	b = 30; // Alteração no escopo global
    alert(`Valor da variável b foi alterado globalmente para ${b}`);
}
function exibirValorC() {
    alert("O valor da variável c é " + c + " e seu tipo é " + typeof c);
}
function alterarValorC() {
	const c = 10; // Redeclaração fora do escopo global
    alert(`Valor da variável c foi alterado localmente para ${c}`);
}
