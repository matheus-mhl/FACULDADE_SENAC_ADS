import java.util.Scanner;

/*
 * Faça um programa que imprima a tabuada de um numero “n” (dado de entrada do 
 * seu programa)  utilizando estrutura de repetição.
*/
import java.util.*;
public class ex1_tabuada {

	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in);
		
		System.out.println("Entre com um numero: ");
		int numero = sc.nextInt();
		
		System.out.println("Tabuada de " + numero);
		for(int i = 0; i<=10; i++) {
			System.out.println(numero + "x" + i + " = " + (i*numero));
		}

	}

}
