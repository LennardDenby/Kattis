import java.util.Scanner;

public class solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int statues = Integer.parseInt(scanner.nextLine());
        int printers = 1;
        int days = 0;

        while (printers < statues) {
            printers += printers;
            days++;
        }
        System.out.println(days + 1);

        scanner.close();
    }
}
