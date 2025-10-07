/*
 * 1) Crie um novo projeto chamado orientacaoaobjetos2 e nele crie uma classe pública chamada Funcionario em um pacote chamado br.senac.rj.empresa.modelo que 
 * contenha os seguintes atributos públicos:
	registro (tipo int)
	nome (tipo String)
	cargo (tipo int)
	salario (tipo double)
*/

package br.senac.rj.empresa.modelo;

public class Funcionario {
	public int registro;
	public String nome;
	public int cargo;
	public double salario;

	

/*
 * 2) Crie na classe Funcionario um método chamado aplicarBonificacao que 
 * calcule o novo salário do funcionário conforme os critérios abaixo:
- 20% de bonificação se cargo igual a 1
- 40% de bonificação se cargo igual a 2
- 60% de bonificação se cargo igual a 3
- 0% de bonificação se cargo diferente de 1, 2 ou 3
*/

	public void aplicarBonificacao() {
		double percentualBonificacao = 0.0;
		
		if (cargo == 1) {
			percentualBonificacao = 0.20; //20%
		}else if (cargo == 2) {
			percentualBonificacao = 0.40; //40%
		}else if (cargo == 3) {
			percentualBonificacao = 0.60; //60%
		}
		salario += salario * percentualBonificacao;
	}
	
}