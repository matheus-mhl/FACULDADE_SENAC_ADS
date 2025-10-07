
public class TesteIfElseIfElse2_ex2 {

	public static void main(String[] args) {
		double salarioBase = 3000.00; //Troque o valor do salário para teste
		double aliquota = 0.0;
		double deducao = 0.0;
		double imposto;
		double salarioLiquido;
        
		if (salarioBase <= 2826.66) {
            aliquota = 0.0;
            deducao = 0.0;
        } else if (salarioBase <= 3751.05) {
            aliquota = 0.15;
            deducao = 354.80;
        } else if (salarioBase <= 4664.68) {
            aliquota = 0.225;
            deducao = 636.13;
        } else {
            aliquota = 0.275;
            deducao = 869.36;
        }
		
		imposto = (salarioBase * aliquota) - deducao;
		salarioLiquido = salarioBase - imposto;

        System.out.println("Salário base: R$ " + salarioBase);
        System.out.println("Alíquota: " + (aliquota * 100) + "%");
        System.out.println("Dedução: R$ " + deducao);
        System.out.printf("Imposto de renda a pagar: R$ %.2f%n", imposto);
        System.out.printf("Salário líquido: R$ %.2f%n", salarioLiquido);
        
	}

}

//exercicio com conteudo adicional e 'Scanner' - *como importar SCANNER!!!!

/*
import java.util.Scanner;

public class TesteIfElseIfElse2 {

	public static void main(String[] args) {
//		double salario = 4000.00;
		double salario;
		double rate;
		double liquid;
		double deduct = 0;
		double imposto;
		
		Scanner sc = new Scanner(System.in);
		System.out.print("Entre com seu salário: ");
		salario = sc.nextDouble();
		
	if (salario<= 2826.66) {rate = 0;
		}
	else if (salario<=3751.05) {rate = 0.15; deduct = 354.80;
		}
	else if (salario<=4664.68) {rate = 0.225; deduct = 636.13;
		}
	else {rate = 0.275;
		 deduct = 869.36;}
	
	imposto = salario*rate-deduct;	
	liquid = salario - imposto;
	
	
	System.out.println("O salário bruto é de " + salario);
	System.out.println("O imposto de renda é de " + (salario*rate-deduct));
	System.out.println("O salário liquido é de " + liquid);
	System.out.println(salario>=20000 ? "Salário de diretor" : "Salário de funcionário normal");
				
	}

}
 */
