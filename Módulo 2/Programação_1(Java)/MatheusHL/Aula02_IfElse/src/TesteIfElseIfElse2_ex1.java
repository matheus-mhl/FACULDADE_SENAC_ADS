
public class TesteIfElseIfElse2_ex1 {

	public static void main(String[] args) {
		double salarioBase = 3000.00; //Troque o valor do salário para teste
		double aliquota = 0.0;
		double deducao = 0.0;
		double imposto;
        
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

        System.out.println("Salário base: R$ " + salarioBase);
        System.out.println("Alíquota: " + (aliquota * 100) + "%");
        System.out.println("Dedução: R$ " + deducao);
        System.out.printf("Imposto de renda a pagar: R$ %.2f%n", imposto);

	}

}
