public class TesteIfElse1 {
    public static void main(String[] args) {
        int a = 1;
        int b = 2;

        System.out.println("a = " + a);         // prints a = 1
        System.out.println("b = " + b);         // prints b = 2

        if (a == b) {
            System.out.println("a é igual a b");
        } else {
            System.out.println("a é diferente de b"); // this executes
        }

        if (a != b)
            System.out.println("a é diferente de b"); // this also executes

        a = b;  // now a = 2

        System.out.println("a = " + a);         // prints a = 2
        System.out.println("b = " + b);         // prints b = 2

        if (a == b)
            System.out.println("a é igual a b");      // this executes now
        else
            System.out.println("a é diferente de b");
    }
}
