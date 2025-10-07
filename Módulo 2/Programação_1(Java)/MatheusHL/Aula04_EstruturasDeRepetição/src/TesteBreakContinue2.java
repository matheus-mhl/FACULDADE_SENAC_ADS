
public class TesteBreakContinue2 {

    public static void main(String[] args) {
        // Imprime números primos entre 1 e 10
        int numero;
        int contador;
        int resto;
        int numDivisores;
        int totalNumeros = 10;

        for (numero = 2; numero <= totalNumeros; numero++) { // número 1 não é primo
            numDivisores = 0;
            contador = 1;

            while (contador < numero) {
                resto = numero % contador;
                if (resto == 0) {
                    numDivisores++;
                    if (numDivisores > 2) { // Se já tiver mais de 2 divisores, não é primo
                        break; // Sai do laço
                    }
                }
                contador++;
            }

            if (numDivisores > 2) {
                continue; // Não imprime este número, vai para o próximo
            }

            System.out.println(numero + " é um número primo.");
        }
    }



	}


