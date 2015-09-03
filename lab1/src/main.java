import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Created by roman on 9/3/15.
 *
 * 1. Ввести n строк с консоли, найти самую короткую строку. Вывести эту строку и ее длину.
 *
 */

public class main
{
    public static void main(String[] args)
    {
        int n; // число строк
        while ( true ) // ввод числа строк
        {
            System.out.println("Введите число строк");
            Scanner sc1 = new Scanner(System. in );
            try
            {
                n = sc1.nextInt();
                if (n > 0) break;
            }
            catch(InputMismatchException fg)
            {
                // если введенное значение не является числом
                System.out.print("Вы ввели не число. " );
            }
        }

        // считывание строк из консоли
        Scanner sc2 = new Scanner(System.in);
        String shortestString = null; // самая короткая строка0
        for (int i = 0; i < n; i++)
        {
            System. out.println( "Введите строку №" + (i+1));
            String str = sc2.nextLine();
            if (i == 0) {
                shortestString = str;
            } else if (shortestString.length() > str.length()) {
                // если введенная строка короче, чем самая короткая, то обновляем самую короткую
                shortestString = str;
            }
        }
        System.out.println("Длинна самой короткой строки: "+shortestString.length());
        System.out.println("Самая короткая строка: "+shortestString);
    }
}