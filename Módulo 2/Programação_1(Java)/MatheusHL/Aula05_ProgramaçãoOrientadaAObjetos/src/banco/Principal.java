package banco;

public class Principal {

	public static void main(String[] args) {
		Conta cc1 = new Conta();

		cc1.agencia = 1;
		cc1.numero = 101;
		cc1.saldo = 200;
		
		Conta ccBob = new Conta();
		ccBob.agencia = 1;
		ccBob.numero = 102;
		ccBob.saldo = 400;
		
		System.out.println("saldo da conta cc1: " + cc1.saldo);
		System.out.println("saldo da conta ccBob: " + ccBob.saldo);
		
		System.out.println("Depositando...");
		cc1.deposita(1000);
		System.out.println("saldo da conta cc1: " + cc1.saldo);
		System.out.println("saldo da conta ccBob: " + ccBob.saldo);
	}

}
