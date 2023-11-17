# **CodeAlpha | Python Intern | Remote Internship**

## **Task No# 01 : Hangman Game**
### **Perform Task**
- Design a text-based Hangman game. The program selects a random word, and the player guesses one letter at a time to uncover the word.You can set a limit on the number of incorrect guesses allowed.

---

## **Project No# 01: Text-Based Hangman Game in Python**

#### **Introduction:**
  - The Text-Based Hangman Game is a simple yet engaging Python project designed to entertain and challenge players. The program randomly selects a word from a predefined list, and players attempt to guess the word one letter at a time.

#### **Features:**
  - **Word Selection:** The game selects a random word from a list of options, ensuring variety in each playthrough.
  - **Guessing Mechanism:** Players input one letter at a time to uncover the hidden word. The game tracks guessed letters and displays the current state of the word after each guess.
  - **Limits on Incorrect Guesses:** To add suspense, the game sets a limit on the number of incorrect guesses allowed (default: 5). Players must strategize to reveal the word before reaching the maximum attempts.

#### **Usage:**
  - Players are welcomed to the game with a friendly message.
  - They input their guesses, receiving feedback on correctness and the remaining attempts.
  - The game continues until the word is guessed correctly or the player exhausts their attempts.

#### **Conclusion:**
  - The Text-Based Hangman Game is an entertaining project that showcases foundational Python concepts such as randomization, input handling, and conditional statements. It provides a hands-on experience in creating interactive programs and is suitable for beginners and those looking to reinforce their Python skills. Players can enjoy the challenge of guessing words while exploring the world of text-based gaming. Feel free to customize the code, add more words, or tweak the difficulty level for an enhanced gaming experience.

---

## **Task No# 02 : URL Shortener**
### **Perform Task**
- Develop a URL shortening service like Bitly. Users can input a long URL, and the application will generate a shorter, unique URL that redirects to the original link

---

## **Project No# 02: URL Shortener in Python**

#### **Introduction:**
  - The Python Tkinter URL Shortener is an intuitive GUI application that replicates the frontend experience of a URL shortening service, akin to platforms like Bitly. This application empowers users to input lengthy URLs and swiftly generates shorter, unique URLs, which are conveniently copied to the clipboard for effortless sharing.

#### **Key Features:**
  - **Tkinter GUI:** Leveraging the Tkinter library, the program delivers a user-friendly interface. Essential widgets such as labels, entry fields, and buttons are employed to enhance the user experience.
  - **ShortUUID Generation:** Integrating the shortuuid library, the application generates distinctive short URLs. These pseudo short URLs serve as placeholders, simulating the eventual result of a backend system.
  - **Clipboard Interaction with Pyperclip:** The pyperclip library facilitates cross-platform clipboard operations, ensuring that the generated short URL is swiftly copied, ready for immediate use.

#### **Functionality:**
  - Users input a long URL, click the "Shorten URL" button, and witness the swift generation of a unique short URL. The application provides real-time feedback through labels and copies the short URL to the clipboard for seamless sharing.

#### **Enhancements:**
  - The window size is set to 500x300 pixels to provide a more spacious and visually appealing layout. The size adjustment is achieved using the geometry method on the root window.

#### **Conclusion:**
  - While this project only simulates the frontend aspects of a URL shortening service, it offers a practical demonstration of creating interactive applications with Tkinter. It underscores the simplicity of integrating external libraries for unique identifier generation and clipboard functionality. To fully realize a URL shortening service, a corresponding backend system would be necessary to manage URL storage, retrieval, and redirection.

#### **Usage:**
  1) Execute the Python script.
  2) Input a long URL.
  3) Click "Shorten URL" to promptly generate a unique short URL.
  4) The short URL is presented and copied to the clipboard for immediate sharing.
