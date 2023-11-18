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

---

## **Task No# 03 : Basic ChatBot**
### **Perform Task**
- Create a text-based chatbot that can have conversations with users. You can use natural language processing libraries like NLTK or spaCy to make your chatbot more conversational.

---

## **Project No# 03: Basic ChatBot Application with Tkinter and NLTK**

#### **Introduction:**
  - The "Basic ChatBot" project showcases a simple yet engaging text-based conversational interface built using Python and Tkinter. This user-friendly application enables users to interact with a chatbot that responds to their queries and prompts. The project utilizes the Tkinter library for creating a graphical user interface (GUI) and leverages the nltk library for natural language processing, allowing the chatbot to engage in meaningful conversations.

#### **Key Features:**

  1) **User Interface with Tkinter:** The application boasts an intuitive GUI designed using Tkinter, providing a visually appealing and responsive platform for users to interact with the chatbot.
  2) **Themed Appearance:** The ttkthemes library enhances the aesthetics by incorporating the "elegance" theme, contributing to a polished and modern user interface.
  3) **Interactive Conversations:** The chatbot responds dynamically to user input, engaging in conversations on various topics. It understands and responds to greetings, inquiries about its capabilities, jokes, and more.
  4) **Input Validation:** The application includes input validation to ensure that users provide meaningful messages. If an empty message is entered, a prompt alerts the user to enter a valid message.
  5) **Conversation History Display:** The scrolled text widget displays the ongoing conversation, making it easy for users to review the chatbot's responses and their own messages.
  6) **Send Button and Enter Key Interaction:** Users can send messages either by clicking the "Send" button or by pressing the Enter key, providing flexibility in interacting with the chatbot.

#### **Functionality:**
  - Upon launching the application, users are greeted with a welcome message from the chatbot. They can then engage in conversations by typing messages in the input field and receiving responses from the chatbot. The application provides a diverse set of responses, including answering questions about the chatbot's capabilities, telling jokes, and handling farewell messages.

#### **Conclusion:**
  - The "Basic ChatBot" project demonstrates the integration of Python's Tkinter and nltk libraries to create an interactive and visually appealing chatbot application. While it serves as a starting point, the project can be expanded by adding more sophisticated natural language processing capabilities, integrating external APIs for real-time information retrieval, and enhancing the chatbot's responses for a more lifelike interaction.

#### **Usage:**

  - Launch the application.
  - Enter messages in the input field.
  - Click the "Send" button or press Enter to interact with the chatbot.
  - Explore various topics and enjoy the chatbot's responses.

#### **Note:**
  - This project lays the foundation for developing more advanced chatbot applications with extended functionalities and improved conversational abilities.
