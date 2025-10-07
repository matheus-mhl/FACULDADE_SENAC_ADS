/*
Exercício 3: Jogo de Adivinhação

Crie um jogo simples onde o programa "pensa" em um número aleatório entre 1 e 100. O jogador tem no máximo 5 tentativas para adivinhar o número.

Requisitos:
1.	Para cada tentativa, informe ao usuário se o palpite foi muito alto ou muito baixo.
2.	Se o jogador acertar, exiba uma mensagem de parabéns e diga em quantas tentativas ele conseguiu.
3.	Se ele não conseguir em 5 tentativas, exiba o número correto e uma mensagem de derrota.
Conteúdos necessários:
•	Random (para gerar o número)
•	for (para o laço de 5 tentativas)
•	if/else if/else
•	break (para sair do loop se acertar)
*/

package ex4;
import java.util.Random; //Para gerar numero aleatorio
import java.util.Scanner; // Para ler entradada do teclado

public class JogoDeAdivinhacao {

	public static void main(String[] args) {
		Random random = new Random();
		
		int numero = random.nextInt(100) + 1; //O '+1' é adicionado para que o programa trabalhe com os valores de 1 a 100(Pois normalmente se trabalha de 0 a 99 quando utiliado 'random.nextInt')
		
		int tentativasMax = 5;
		boolean acertou = false;
		
		System.out.println("Tente adivinhar o número (entre 1 e 100) gerado por mim.");
		System.out.println("Você terá" + tentativasMax + "chances de acertar.");
		System.out.println("Boa sorte!!");
		
		

	}

}
