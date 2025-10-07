package teste;
import banco.Conta;

public class TesteClasse1 {

	public static void main(String[] args) {
		Conta conta1 = new Conta();
		conta1.agencia = 1;
		conta1.numero = 100;
		conta1.saldo = 200;
		
		System.out.println("Saldo inicial: " + conta1.saldo);
		conta1.deposita(1000);
		System.out.println("Novo Saldo: " + conta1.saldo);
		
		if (conta1.saca(2000)) {
			System.out.println("Novo Saldo: " + conta1.saldo);
		} else {
			System.out.println("SEM SALDO");
		}	
	}
}
