/**
 * Created by roman on 9/3/15.
 *
 * Задать движение по экрану строк (одна за другой) из массива строк.
 * Направление движения по апплету и значение каждой строки выбирается случайным образом.
 *
 */

import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Random;
import javax.swing.*;

public class main {
    public static void main(String[] args) {

        // заполняю массив строк, которые будут двигаться
        final ArrayList<String> strings = new ArrayList<String>();
        strings.add("Задать движение по экрану строк");
        strings.add("(одна за другой)");
        strings.add("из массива строк");
        strings.add("направление движения по апплету");
        strings.add("и значение каждой строки");
        strings.add("выбирается случайным образом");

        // делаю форму и лейбл
        final JFrame frame = new JFrame("Движение по экрану строк");
        frame.setPreferredSize(new Dimension(800, 500));
        frame.setVisible(true);
        frame.setLayout(null); // обязательно удаляю лейаут, чтобы было абс. позиционирование

        final JLabel lbl = new JLabel();
        lbl.setLocation(-1, 0);
        lbl.setSize(300, 20); // неприятный хардкод размеров лейбла
        frame.add(lbl);

        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.pack();

        // главный таймер - в нем происходит вся логика движения
        Timer timer = new Timer(50, new ActionListener() {
            int speedX, speedY; // скорость движения текста
            Random rnd = new Random();
            @Override
            public void actionPerformed(ActionEvent arg0) {
                Point loc = lbl.getLocation();

                // если вышли за пределы, то сброс на новое слов
                if (loc.x > frame.getWidth() || loc.y > frame.getHeight() || loc.x < 0 || loc.y < 0) {
                    lbl.setLocation(frame.getWidth()/2, frame.getHeight()/2); // встаю примерно по центру окна
                    speedX = -5+rnd.nextInt(10); // задаю случайную скорость
                    speedY = -5+rnd.nextInt(10); // задаю случайную скорость
                    lbl.setText(strings.get(rnd.nextInt(strings.size()-1))); // задаю случайную строку
                } else {
                    lbl.setLocation(loc.x + speedX, loc.y + speedY); // свдигаю лейбл с заданной скоростью
                }
            }});
        timer.start();
    }
}