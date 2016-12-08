# coding=utf-8


def handle(self):
    # отправка точно такого-же сообщения, которое пришло на вход
    self.data = self.request.recv(1024).strip()
    self.request.sendall(self.data)
