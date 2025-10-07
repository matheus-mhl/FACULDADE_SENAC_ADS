/*
 * Crie um programa que solicita ao usuário que digite números repetidamente e calcula a soma. O programa deve parar de pedir números quando 
 * o usuário digitar “0” e, então, imprimir a soma total dos números digitados (o “0” não deve ser incluído na soma).
*/
import java.util.Scanner;

public class ex3_calcule_soma {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1;
        int soma = 0;

        while (true) {
            System.out.print("Digite um número (0 para sair): ");
            num1 = sc.nextInt();

            if (num1 == 0) {
                break; // sai do laço se o número for 0
            }

            soma += num1; // soma = soma + num1
        }

        System.out.println("Soma = " + soma);
        sc.close();
    }
}

