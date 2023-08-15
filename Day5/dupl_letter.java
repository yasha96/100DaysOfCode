import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class DuplicateLettersCheck {

    public static boolean hasDuplicateLetters(String sentence) {
        String[] words = sentence.split(" ");

        for (String word : words) {
            Set<Character> letterSet = new HashSet<>();
            for (char letter : word.toLowerCase().toCharArray()) {  // Convert to lowercase
                if (letterSet.contains(letter)) {
                    return true;
                }
                letterSet.add(letter);
            }
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String userInput = scanner.nextLine();
        scanner.close();

        boolean result = hasDuplicateLetters(userInput);
        System.out.println(result);
    }
}

