import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Created by roman on 9/3/15.
 *
 * 1.Написать регулярное выражение, определяющее является ли данная строка строкой "abcdefghijklmnopqrstuv18340" или нет.
 * – пример правильных выражений: abcdefghijklmnopqrstuv18340.
 * – пример неправильных выражений: abcdefghijklmnoasdfasdpqrstuv18340.
 *
 */
import java.util.regex.*;

public class main {
    public static void main(String[] args) {
        // проверка на соответствие строки шаблону
        Pattern p1 = Pattern.compile("^abcdefghijklmnopqrstuv18340$");
        String str  = "abcdefghijklmnopqrstuv18340";
        System.out.println(str + ": " + p1.matcher(str).matches());

        str  = "abcdefghijklmnoasdfasdpqrstuv18340";
        System.out.println(str + ": " + p1.matcher(str).matches());

        str  = "123abcdefghijklmnopqrstuv18340";
        System.out.println(str + ": " + p1.matcher(str).matches());
    }
}