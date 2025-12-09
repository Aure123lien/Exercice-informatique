import java.util.Scanner;

public class TicTacToe {
    private static char[][] board = new char[3][3];
    private static char currentPlayer = 'X';
    private static Scanner scanner = new Scanner(System.in);

    private static void initializeBoard() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = ' ';
            }
        }
    }

    private static void printBoard() {
        System.out.println("  0 1 2");
        for (int i = 0; i < 3; i++) {
            System.out.print(i + " ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j]);
                if (j < 2) System.out.print("|");
            }
            System.out.println();
            if (i < 2) System.out.println("  -----");
        }
    }

    private static void switchPlayer() {
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    private static char checkWinner() {
        // Vérifier les lignes du morpion
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ') {
                return board[i][0];
            }
        }
        // Vérifier les colonnes du morpion
        for (int j = 0; j < 3; j++) {
            if (board[0][j] == board[1][j] && board[1][j] == board[2][j] && board[0][j] != ' ') {
                return board[0][j];
            }
        }
        // Vérifier les diagonales du morpion
        if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ') {
            return board[0][0];
        }
        if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ' ') {
            return board[0][2];
        }
        return ' ';
    }

    private static boolean isBoardFull() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == ' ') {
                    return false;
                }
            }
        }
        return true;
    }

    private static void makeMove() {
        int row, col;
        while (true) {
            System.out.print("Joueur " + currentPlayer + ", entrez la ligne (0-2): ");
            row = scanner.nextInt();
            System.out.print("Joueur " + currentPlayer + ", entrez la colonne (0-2): ");
            col = scanner.nextInt();
            if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == ' ') {
                board[row][col] = currentPlayer;
                break;
            } else {
                System.out.println("Mouvement invalide. Essayez encore.");
            }
        }
    }

    public static void main(String[] args) {
        // Le début du programme
        System.out.println("Bienvenue dans mon jeu du Morpion ");

        boolean playAgain = true;
        while (playAgain) {
            // Le chargement du morpion
            initializeBoard();
            currentPlayer = 'X';

            printBoard();

            // La boucle principale du jeu
            while (true) {
                makeMove();
                printBoard();
                char winner = checkWinner();
                if (winner != ' ') {
                    System.out.println("Le joueur " + winner + " a gagné !");
                    break;
                } else if (isBoardFull()) {
                    System.out.println("Match nul !");
                    break;
                }
                switchPlayer();
            }

            System.out.print("Voulez-vous rejouer ? (o/n): ");
            String response = scanner.next();
            playAgain = response.equalsIgnoreCase("o");
        }

        scanner.close();
    }
}