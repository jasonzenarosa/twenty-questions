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


if __name__ == '__main__':
    Host(True, 2020, 'jason')
