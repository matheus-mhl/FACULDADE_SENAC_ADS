package CalculadoraSimples;
/*Calculadora Simples (Sem Métodos)
Objetivo
Criar um programa em Java que simule uma calculadora simples, utilizando apenas o método main() e os conceitos básicos de:
•	Estrutura de repetição (while)
•	Condicionais (if, switch)
•	Entrada e saída de dados
________________________________________
🧱 Instruções
1.	Criar a classe Calculadora
o	Toda a lógica será implementada dentro do método main().
2.	Exibir o menu de opções
o	O menu deve ser mostrado repetidamente até que o usuário escolha sair.
3.	Ler a opção do usuário
o	Verificar se a opção é válida.
o	Se for uma operação, solicitar dois números inteiros.
o	Executar a operação escolhida e exibir o resultado.
o	Se a opção for inválida, exibir uma mensagem de erro.
4.	Encerrar o programa
o	Quando o usuário escolher 'S' ou 's', o programa deve finalizar.
________________________________________
Menu de Opções
Escolha a opção:
‘+’ - Soma de 2 números inteiros.
‘-’ - Diferença entre 2 números (maior pelo menor).
‘*’ - Produto entre 2 números.
‘/’ - Divisão entre 2 números (o denominador não pode ser zero).
‘S’ ou ‘s’ - Sair
________________________________________
Entrada
•	Um caractere representando a operação
•	Dois números inteiros (exceto na opção de saída)
________________________________________
Saída
•	Resultado da operação escolhida
•	Mensagem de erro para opção inválida ou divisão por zero
________________________________________
Repetição
•	O programa deve continuar executando até que o usuário escolha sair.
*/
import java.util.Scanner;

public class CalculadoraSimples {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		char opcao;
		
		while(true) {
			//Menu de opções:
			System.out.println("\n Escolha a opção: ");
            System.out.println("‘+’ - Soma de 2 números inteiros.");
            System.out.println("‘-’ - Diferença entre 2 números (maior pelo menor).");
            System.out.println("‘*’ - Produto entre 2 números.");
            System.out.println("‘/’ - Divisão entre 2 números (o denominador não pode ser zero).");
            System.out.println("‘S’ ou ‘s’ - Sair");
            System.out.print("Opção: ");
            
            //Lendo input do usuário
            opcao = input.next().charAt(0);
            
            //Verifica se o usuário quer SAIR
            if (opcao == 'S' || opcao == 's') {
            	System.out.println("Encerrando o proframa...");
            	break; //Finalizano o loop
            }
            
            int num1, num2; //numeros que serão usados nas operações
            
            //Usando o switch
            switch(opcao){
            	case '+':
            		System.out.println("Digite o PRIMEIRO numero: ");
            		num1 = input.nextInt();
            		System.out.println("Digite o SEGUNDO numero ");
            		num2 = input.nextInt();
            		System.out.println("RESULTADO: " + (num1 + num2));
            		break;//FIM do método SOMA
            		
            	case '-':
            		System.out.println("Digite o PRIMEIRO numero: ");
            		num1 = input.nextInt();
            		System.out.println("Digite o SEGUNDO numero: ");
            		num2 = input.nextInt();
            		System.out.println("RESULTADO: " + (num1 - num2));
            		break;//FIM do método SUBTRAÇÃO 
            		
            		//Método de SUBTRACAO OTIMIZADO/CORRIGIDO
            		/*case '-':
                    System.out.print("Digite o primeiro número: ");
                    num1 = input.nextInt();
                    System.out.print("Digite o segundo número: ");
                    num2 = input.nextInt();
                    // Diferença do maior pelo menor
                    int diferenca = (num1 > num2) ? (num1 - num2) : (num2 - num1);
                    System.out.println("Resultado: " + diferenca);
                    break;*/
            		
            	case '*':
            		System.out.println("Digite o PRIMEIRO numero: ");
            		num1 = input.nextInt();
            		System.out.println("Digite o SEGUNDO nuero: ");
            		num2 = input.nextInt();
            		System.out.println("RESULTADO: " + (num1 * num2));
            		break;
            		
            	case '/':
            		System.out.println("Digite o PRIMEIRO numero: ");
            		num1 = input.nextInt();
            		System.out.println("Digite o SEGUNDO numero: ");
            		num2 = input.nextInt();
            		if (num2 == 0) {
            			System.out.println("ERRO ***não é possível dividir por zero(0)***");
            		}
            		else {
            			System.out.println("RESULTADO: " + (num1 / num2));
            			}
            		break;
            	
            	default:
            		System.out.println("Opção inválida, por favor utilize uma das seguintes opções: '+' , '-' , '*' , '/'");
            		
            		
            }
		}
		input.close(); //Comando utilizado para FECHAR SCANNER
	}
}