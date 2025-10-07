/*
 * Faça um programa que leia 10 valores inteiros, um de cada vez, e encontre quantos destes valores são pares, 
 * quantos são ímpares, além de calcular a média de todos os números informados. Todos os dados calculados devem 
 * ser exibidos ao final do programa. 
*/

import java.util.Scanner;
public class ex2_10Valores_pares_e_impares {

	public static void main(String[] args) {
		try (Scanner sc = new Scanner(System.in)) {
			int numero;
			int contPar = 0;
			int contImpar = 0;
			int soma = 0;
			
			for (int i = 1; i<=10; i++) {
				System.out.println("Ente com" + i + "o numero: ");
				numero = sc.nextInt();
				if (numero%2==0) {
					contPar++;
				} else {
					contImpar++;
				}
				soma = soma + numero;
			}
			System.out.println("Existe" + contPar + "pares e" + contImpar + "impares");
		}
	}

}
