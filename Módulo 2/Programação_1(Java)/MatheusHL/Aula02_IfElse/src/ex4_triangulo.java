import java.util.*;

public class ex4_triangulo {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Entre com o lado 1: ");
		int lado1 = sc.nextInt();
		System.out.println("Entre com o lado 2: ");
		int lado2 = sc.nextInt();
		System.out.println("Entre com o lado 3: ");
		int lado3 = sc.nextInt();
		
		boolean okLado1 = (lado1<lado2+lado3)? true : false;
		boolean okLado2 = (lado2<lado1+lado3)? true : false;
		boolean okLado3 = (lado1<lado2+lado1)? true : false;
		
		if(okLado1 & okLado2 & okLado3) {
			if ((lado1==lado2) & (lado2==lado3)) {
				System.out.println("Triangulo Equilatero");
			} else if (((lado1==lado2)& (lado2!=lado3))| ((lado1!=lado2) & (lado2==lado3)))
				System.out.println("Triangulo Isoceles");
			} else {
				System.out.println("Triângulo Ecaleno");
			}
	} else { //CORRIGIR ERRO
		System.out.println("NÃO É TRIÂNGULO!!");
	}
		}

	}

}
