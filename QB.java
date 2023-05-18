import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class QuestionBank {
    private static final int PORT = 5000;

    private static final List<String> questions = new ArrayList<>();
    private static final List<String> answers = new ArrayList<>();

    public static void main(String[] args) {
        populateQuestionsAndAnswers();  // Add questions and answers to the lists

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Question-Bank is running on port " + PORT);

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("New connection from: " + clientSocket.getInetAddress().getHostAddress());

                Thread thread = new Thread(() -> handleClient(clientSocket));
                thread.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void handleClient(Socket clientSocket) {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
             PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                String[] tokens = inputLine.split(" ");
                String command = tokens[0];

                if ("LOGIN".equals(command)) {
                    String username = tokens[1];
                    String password = tokens[2];
                    boolean success = login(username, password);
                    out.println(success ? "SUCCESS" : "FAILURE");
                } else if ("GET_QUESTION".equals(command)) {
                    String question = getRandomQuestion();
                    out.println(question);
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static boolean login(String username, String password) {
        // Add your login logic here
        return true;
    }

    private static String getRandomQuestion() {
        Random random = new Random();
        int index = random.nextInt(questions.size());
        return questions.get(index);
    }

    private static void populateQuestionsAndAnswers() {
        // Add your questions and answers here
        questions.add("What is the capital of France?");
        answers.add("Paris");

        questions.add("What is the largest planet in our solar system?");
        answers.add("Jupiter");

        questions.add("Who painted the Mona Lisa?");
        answers.add("Leonardo da Vinci");
    }
}
