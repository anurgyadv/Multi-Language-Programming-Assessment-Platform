# Multi-Language-Programming-Assessment-Platform


Flow of the project - 

1. Understand the Requirements: Review the project description and make sure you have a clear understanding of the requirements, constraints, and expected functionality of each component.

2. Choose Programming Languages: Select two programming languages (Java, C, or Python) for implementing the Test-Manager (TM) and Question-Banks (QBs). Consider the strengths and familiarity of your team members with these languages.

3. Design the System Architecture: Define the high-level architecture of your system, including the interactions between the web browser, TM, and QBs. Determine how data will flow, how authentication will be handled, and how questions and answers will be exchanged.

4. Design the User Interface: Decide on the basic HTML user interface elements that will be used in the TM. Plan how you will present questions, receive student answers, and display progress and marks.

5. Implement the Test-Manager (TM): Start developing the TM application using the chosen programming language. Implement the authentication mechanism, session management, and the logic to retrieve questions from the QBs. Create the necessary endpoints or functions to handle student submissions and calculate marks.

6. Implement the Question-Banks (QBs): Develop the QB application using the other programming language you selected. Implement the logic to generate random or repeatably randomized questions based on the chosen programming languages. Include the functionality to execute and mark students' programming attempts.

7. Define the Communication Protocol: Design and implement a simple application-layer protocol for communication between the TM and QBs. This protocol should facilitate the exchange of queries, responses, and files.

8. Handle File Storage: Determine how and where you will store student information, questions, and other necessary files. Use simple text files for storing data, as specified in the project constraints.

9. Test and Debug: Test each component of the system individually and then integrate them to ensure they work together seamlessly. Debug any issues or errors that arise during testing.

10. Enhance and Refine: Once the core functionality is working, consider adding additional features to enhance the user experience, such as error handling, progress tracking, and displaying detailed feedback for incorrect attempts.

High-Level System Architecture:

1. Web Browser - HTTP/HTML:
   - The web browser serves as the user interface for students to access the system.
   - It communicates with the Test-Manager (TM) using the HTTP protocol, sending requests and receiving responses in HTML format.
   - The browser displays questions, receives student answers, and shows progress and marks.

2. Test-Manager (TM) - Python:
   - The TM handles the management of the testing process.
   - It receives HTTP requests from the web browser and handles authentication, session management, and student interactions.
   - The TM communicates with the Question-Banks (QBs) to retrieve questions and submit students' attempts.
   - Data flow: TM receives student responses, sends requests to QBs, receives question data, and sends responses back to the web browser.

3. Question-Banks (QBs) - Java:
   - The QBs generate and mark questions for specific programming languages (Java, C, Python).
   - They receive requests from the TM, process them, and return the appropriate question data and marking results.
   - The QBs communicate with the TM using a custom application-layer protocol designed for query, response, and file exchange.
   - Data flow: QBs receive requests from TM, generate question data, execute student attempts, perform marking, and send responses back to TM.

Authentication:
- The TM manages student authentication using a text-based name and password stored in a file.
- When students log in, the TM verifies their credentials against the stored information.

Question and Answer Exchange:
- The TM requests questions from the QBs based on the student's session and chosen programming language.
- QBs randomly select questions or generate repeatably randomized questions.
- Students submit their answers through the web browser to the TM.
- The TM sends the student's attempts to the corresponding QB for marking.
- QBs execute the attempts and compare the output with the expected answer, providing marking results to the TM.

Overall, the web browser interacts with the TM via HTTP/HTML, while the TM communicates with the QBs using a custom application-layer protocol. Data flows between these components to handle authentication, question retrieval, student attempts, and marking. The TM orchestrates the overall testing process, managing student sessions and providing the necessary functionality for testing and marking.


