import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.Random;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        int MAX_NUMBER = 1_234_000_100;
        int first_try;
        long seed;
        WebElement check_button;
        WebElement input_box;

        WebDriver driver = new ChromeDriver();

        driver.get("https://r1-ctf-vulnerable.numa.host/");

        List<WebElement> buttons = driver.findElements(By.className("btn-outline-primary"));

        buttons.get(1).click(); // Reseteamos la seed

        seed = System.currentTimeMillis(); // Creamos la nuestra cercana a la real
        Random rand = new Random(seed);
        first_try = rand.nextInt(MAX_NUMBER); // primer número a introducir

        buttons = driver.findElements(By.className("btn-outline-primary"));

        check_button = buttons.getFirst(); // Botón de check
        input_box = driver.findElement(By.id("number")); // input box

        /* Introducimos el número y hacemos click a check */
        input_box.sendKeys(String.valueOf(first_try));
        check_button.click();

        /* Será incorrecto con casi total seguridad, cogemos el número que nos dice la web */
        Thread.sleep(500);
        List<WebElement> numbers = driver.findElements(By.tagName("il"));
        String number = numbers.getFirst().getText();

        /* Bruteforce de la seed */
        System.out.println("Starting checks with " + number);
        while (Integer.parseInt(number)!= first_try) {
            seed = seed -1 ;
            rand = new Random(seed);
            first_try = rand.nextInt(MAX_NUMBER);

        }

        System.out.println("Found number: " + first_try + " with seed " + seed);
        rand = new Random(seed);
        int aux = rand.nextInt(MAX_NUMBER);

        /* Introducimos el número que nos printee la siguiente línea y vemos la flag */
        System.out.println("Your next number for the flag is "+ rand.nextInt(MAX_NUMBER));
        // URJC{H0y_3s_tu_d14_d3_su3rt3}

        Scanner sc = new Scanner(System.in); // Scanner para que no se cierre la página
        sc.nextLine();
        driver.quit();

    }
}
