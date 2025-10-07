package br.senac.rj.empresa.teste;
import br.senac.rj.empresa.modelo.Funcionario;

public class TesteFuncionario1 {
    public static void main(String[] args) {
        // Criando um novo funcionário
        Funcionario f = new Funcionario();

        // Atribuindo valores aos atributos
        f.registro = 101;
        f.nome = "João da Silva";
        f.cargo = 2;           // Esperado: 40% de bonificação
        f.salario = 3000.00;

        // Exibindo os dados antes da bonificação
        System.out.println("=== DADOS DO FUNCIONÁRIO ===");
        System.out.println("Registro: " + f.registro);
        System.out.println("Nome: " + f.nome);
        System.out.println("Cargo: " + f.cargo);
        System.out.println("Salário antes da bonificação: R$ " + f.salario);

        // Armazenando salário antes da bonificação
        double salarioOriginal = f.salario;

        // Aplicando a bonificação
        f.aplicarBonificacao();

        // Calculando o valor da bonificação
        double bonificacao = f.salario - salarioOriginal;

        // Exibindo o resultado final
        System.out.println("\n=== RESULTADO ===");
        System.out.println("Bonificação aplicada: R$ " + bonificacao);
        System.out.println("Salário final com bonificação: R$ " + f.salario);
    }
}
