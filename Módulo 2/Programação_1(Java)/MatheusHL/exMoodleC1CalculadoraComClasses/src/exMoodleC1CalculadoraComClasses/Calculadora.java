package exMoodleC1CalculadoraComClasses;

public class Calculadora {
	//Criando atributos dentro da classe:
	/*Criando numeros(num1 e num2) e a 'opcao' para caracteres*/
	private int num1;
	private int num2;
	private char opcao;
	
	//Agora iremos criar GETTERS e SETTERS:
	public int getNum1() {
		return num1;
		}
	public int setNum1(int num1) {
		this.num1 = num1;
	}
	public int getNum2() {
		return num2;
		}
	public int setNum2(int num2) {
		this.num2 = num2;
	}
}