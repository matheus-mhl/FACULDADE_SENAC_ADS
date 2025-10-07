/*Tabuada e Classificação de Números
Objetivo: Praticar estruturas de repetição (for ou while), métodos e a estrutura condicional switch, e a utilização de atributos públicos e privados
1.	Código com atributos Públicos
Crie uma classe chamada Matematica.
Atributos:
o	numero (int) - public
Métodos:
o	Crie um método public chamado gerarTabuada(). Dentro deste método:
	Use uma estrutura de repetição (for ou while) para imprimir a tabuada do número, de 1 a 10. Por exemplo: "5 x 1 = 5", "5 x 2 = 10", etc.
o	Crie um método public chamado classificarNumero(). Dentro deste método:
	Use uma estrutura condicional if/else if/else para classificar o número como "Positivo", "Negativo" ou "Zero".
Na classe Main:
o	Crie um objeto Matematica.
o	Peça ao usuário para inserir um número via teclado (use a classe Scanner).
o	Utilize o objeto criado para definir diretamente o número.
o	Chame os métodos gerarTabuada() e classificarNumero() e imprima os resultados.*/


package ex4;

public class Matematica {
	
	public int numero;

	public static void gerarTabuada() {
		for (int i = 1; i <= 10; i++) {
			System.out.println(this.numero + " x " + i + " = " + (this.numero*i));
		}

	}

	public static voidmain(String[] args) {
		Scanner sc = mew Scanner(System.in);
		
		Matmatica tabuada = new Matematica();
	}
