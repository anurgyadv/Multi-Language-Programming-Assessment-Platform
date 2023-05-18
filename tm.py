import http.server
import socketserver
import webbrowser

def login():
    # Read the username and password from the user
    username = input("Username: ")
    password = input("Password: ")

    # Check if the user credentials are valid
    if authenticate_user(username, password):
        print("Login successful.")
        return username
    else:
        print("Invalid username or password.")
        return None

def authenticate_user(username, password):
    # Read user credentials from the users.txt file
    with open("users.txt", "r") as file:
        for line in file:
            user, pwd = line.strip().split(":")
            if user == username and pwd == password:
                return True
    return False

def test(username):
    # Check if the user is logged in
    if not username:
        print("You need to login first.")
        return

    # Set the session information
    session_info = {"username": username, "questions": ["Question 1", "Question 2", "Question 3"]}

    # Start the HTTP server
    server_address = ("", 8000)
    handler = TestPageHandler(session_info)
    httpd = socketserver.TCPServer(server_address, handler)

    print(f"Welcome, {username}! Opening the test page...")
    webbrowser.open("http://localhost:8000/test")

    # Serve the test page
    httpd.serve_forever()

def start_server():
    PORT = 8000
    # handler = http.server.SimpleHTTPRequestHandler

    # Create an object of the above class
    handler_object = MyHttpRequestHandler

    with socketserver.TCPServer(("", PORT), handler_object) as httpd:
        print("Server started at localhost:" + str(PORT))
        httpd.serve_forever()

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'loginp.html'
        elif self.path == '/test':
            self.path = 'test.html'
        elif self.path == '/loginpage':
            self.path = 'login.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

class TestPageHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, session_info):
        self.session_info = session_info
        super().__init__()

    def do_GET(self):
        if self.path == "/test":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes(f"Welcome, {self.session_info['username']}! This is the test page.", "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(b"404 - Page not found")

def main():
    # Prompt for login
    # username = login()

    # # Open the test page if login is successful
    # if username:
    #     test(username)
    start_server()

if __name__ == "__main__":
    main()