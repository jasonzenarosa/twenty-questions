import socket

class Guest:

    def __init__(self, host:str, port:int, player:str):
        self.player = player
        self.guesses_left = 20
        self.host = host
        self.port = port
        self.join_game()


    def join_game(self):    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            self.opponent = s.recv(4096).decode('utf-8')
            s.send(self.player.encode('utf-8'))
            print(f"You have joined {self.opponent}'s game!")
            self.game(s)
    

    def game(self, s:socket.socket):
        print(f"{self.opponent}'s turn...")
        s.recv(4096)
        while self.guesses_left > 0:
            s.send(self.guess().encode())
            print(f"{self.opponent}'s turn...")
            response = s.recv(4096).decode('utf-8')
            if response == 'Y':
                print('Yes!')
            elif response == 'N':
                print('No!')
            elif response == 'S':
                print('Sometimes!')
            elif response == 'C':
                print('You got it! Thanks for playing!')
                break
        else:
            print('You are out of guesses. Thanks for playing!')


    def guess(self):
        guess = input('Ask a question or enter a guess!\n')
        return guess


if __name__ == '__main__':
    Guest('127.0.0.1', 2022, 'kaitlen')
            
