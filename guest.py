import socket

class Guest:

    def __init__(self, host:str, port:int, player:str):
        self.player = player
        self.host = host
        self.port = port
        self.join_game()

    def join_game(self):    
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            self.opponent = s.recv(4096).decode('utf-8')
            s.send(self.player.encode('utf-8'))
            print(f"You have joined {self.opponent}'s game!")
    

if __name__ == '__main__':
    Guest('127.0.0.1', 2020, 'kaitlen')
            
