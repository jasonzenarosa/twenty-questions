import socket

class Host:

    def __init__(self, islocal:bool, port:int, player:str):
        self.player = player
        self.guesses_left = 20
        if islocal:
            self.host = "127.0.0.1"
        else:
            self.host = "0.0.0.0"
        self.port = port
        self.make_game()


    def make_game(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            
            print('Waiting for connection...')
            conn, addr = s.accept()
            
            conn.send(self.player.encode('utf-8')) # send player username
            self.opponent = conn.recv(4096).decode('utf-8') # receive opponent username
            print(f'{self.opponent} has joined your game!')
            self.game(input('Enter a word!\n'), conn)
    

    def game(self, secret:str, conn:socket.socket):
        conn.send(secret.encode('utf-8'))
        while self.guesses_left > 0:
            print(f"{self.opponent}'s turn...")
            guess = conn.recv(4096).decode('utf-8')
            self.guesses_left -= 1
            if guess == secret:
                print(f'{self.opponent} has guessed your word. Thanks for playing!')
                conn.send(b'C')
                break
            else:
                if guess[-1] == '?':
                    print(guess)
                else:
                    print(f'{guess}?')
                response = self.response()
                conn.send(response.encode('utf-8'))
                if response == 'C':
                    print('Thanks for playing!')
                    break
        else:
            print(f'{self.opponent} has run out of guesses. Thanks for playing!')
            

    def response(self):
        while True:
            user_input = input('What is your response? (y - yes, n - no, s - sometimes, c - correct answer)\n').upper()
            if user_input in ['Y', 'N', 'S', 'C']:
                return user_input
            else:
                print('Invalid input. Try again!')


if __name__ == '__main__':
    Host(True, 2022, 'jason')
