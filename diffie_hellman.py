class DiffieHellmanUser:
    def __init__(self, private_key, g = None, q = None):
        self.num = private_key
        self.g = g
        self.q = q
        self.shared_h = None
        self.h = None
        self.secret = None

    def generate_h(self):
        self.h = (self.g ** self.num) % self.q

    def getSecret(self):
        self.secret = (self.shared_h ** self.num) % self.q

    def sendData(self, user):
        user.acceptData(self.g, self.q)

    def acceptData(self, g, q):
        if self.g is None: self.g = g
        if self.q is None: self.q = q

    def exchange(self, user):
        user.acceptAndExchange(self.h, self)

    def acceptAndExchange(self, h, user = None):
        self.shared_h = h
        if user is not None: user.acceptAndExchange(self.h)


class KeyExchanger:
    def __init__(self, user_a, user_b):
        self.user_a = user_a
        self.user_b = user_b

    def generateSecretKey(self):
        self.user_a.sendData(self.user_b)
        self.user_a.generate_h(); self.user_b.generate_h()
        self.user_a.exchange(self.user_b)
        self.user_a.getSecret(); self.user_b.getSecret();

if __name__ == '__main__':
    alice = DiffieHellmanUser(private_key = 8, g = 7, q = 5)
    bob = DiffieHellmanUser(private_key = 13)
    k = KeyExchanger(alice, bob)
    k.generateSecretKey()
    print(f'A: {alice.secret}\nB: {bob.secret}')
