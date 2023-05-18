import socket

QB_HOST = '192.168.0.100'  # Replace with the QB's IP address
QB_PORT = 5000

def send_message(sock, message):
    sock.sendall(message.encode())

def receive_message(sock):
    data = sock.recv(1024).decode()
    return data.strip()

def login(sock):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    send_message(sock, f"LOGIN {username} {password}")
    response = receive_message(sock)
    if response == "SUCCESS":
        print("Login successful!")
        return True
    else:
        print("Login failed. Please try again.")
        return False

def generate_html_question_form(question):
    html = f"""
    <html>
    <body>
    <h1>Question</h1>
    <p>{question}</p>
    <form method="post">
    <textarea name="answer" rows="4" cols="50"></textarea><br>
    <input type="submit" value="Submit Answer">
    </form>
    </body>
    </html>
    """
    return html

def display_question(sock):
    send_message(sock, "GET_QUESTION")
    question = receive_message(sock)
    html = generate_html_question_form(question)
    print(html)

def main():
    # Establish connection with the Question-Bank
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as qb_socket:
        try:
            qb_socket.connect((QB_HOST, QB_PORT))
        except ConnectionRefusedError:
            print("Failed to connect to the Question-Bank.")
            return

        # Login
        if not login(qb_socket):
            return

        # Display questions
        for _ in range(10):
            display_question(qb_socket)

    print("Testing complete.")

if __name__ == '__main__':
    main()
