public class lab2refactor {

    // a. Accepts all characters
    public static class TextInputBuilder {
        protected StringBuilder value = new StringBuilder();

        public void add(char c) {
            value.append(c); // Adds all characters
        }

        public String getValue() {
            return value.toString(); // Returns accumulated string
        }
    }

    // b. Accepts only digits (0–9)
    public static class NumericInputBuilder extends TextInputBuilder {
        @Override
        public void add(char c) {
            if (Character.isDigit(c)) {
                super.add(c);
            }
        }
    }

    // c. Accepts only odd digits (1, 3, 5, 7, 9)
    public static class OddNumericInputBuilder extends NumericInputBuilder {
        @Override
        public void add(char c) {
            if (Character.isDigit(c) && (c - '0') % 2 == 1) {
                super.add(c);
            }
        }
    }

    // d. Accepts only even digits (0, 2, 4, 6, 8)
    public static class EvenNumericInputBuilder extends NumericInputBuilder {
        @Override
        public void add(char c) {
            if (Character.isDigit(c) && (c - '0') % 2 == 0) {
                super.add(c);
            }
        }
    }

    // e. Main method to test all builders
    public static void main(String[] args) {
        TextInputBuilder textInput = new TextInputBuilder();
        textInput.add('1');
        textInput.add('a');
        textInput.add('0');
        System.out.println("TextInputBuilder: " + textInput.getValue()); // Output: 1a0

        TextInputBuilder numericInput = new NumericInputBuilder();
        numericInput.add('1');
        numericInput.add('a');
        numericInput.add('0');
        System.out.println("NumericInputBuilder: " + numericInput.getValue()); // Output: 10

        TextInputBuilder oddInput = new OddNumericInputBuilder();
        oddInput.add('1');
        oddInput.add('4');
        oddInput.add('7');
        oddInput.add('a');
        System.out.println("OddNumericInputBuilder: " + oddInput.getValue()); // Output: 17

        TextInputBuilder evenInput = new EvenNumericInputBuilder();
        evenInput.add('1');
        evenInput.add('4');
        evenInput.add('8');
        evenInput.add('b');
        System.out.println("EvenNumericInputBuilder: " + evenInput.getValue()); // Output: 48
    }
}