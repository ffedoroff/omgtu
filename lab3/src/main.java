/**
 * Created by roman on 9/3/15.
 *
 * Ввести строки из файла, записать	их в стек. Вывести строки в файл в обратном порядке.
 *
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;

public class main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("/home/roman/.bash_logout"));
        Stack<String> strings = new Stack<String>();

        // считывание строк в стек
        while (sc.hasNextLine()) {
            strings.push(sc.nextLine());
        }

        // вывод строк из стека
        while (!strings.empty()) {
            System.out.println(strings.pop());
        }
    }
}