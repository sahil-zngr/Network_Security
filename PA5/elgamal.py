import random

prime = 91744613 #q

primitveRoot = 2 # alpha



class ElGamal:
    def __init__(self, Xa, q = 91744613, alpha = primitveRoot):
        """
        contructor 
        q prime number
        alpha alpha < q and alpha a primitive root of q
        Select private Xa X A < q - 1
        Calculate  Ya = alpha Xa mod q
        Public key PU = {q, alpha , Ya }
        Private key Xa
        """
        self.q = q
        print(q, alpha)
        self.alp = alpha
        self.Xa = Xa
        self.Ya = pow(self.alp, self.Xa, self.q)


    def Encrypt(self, M):
        """
        Plaintext: M < q
        Select random integer k < q
        Calculate K = (Ya)^k mod q
        Calculate  C1 = alpha^k mod q
        Calculate C2 = KM mod q
        Ciphertext: (C1 , C2 )
        """
        k  = random.randint(2, self.q - 1)
        K = pow(self.Ya, k, self.q)
        C1 = pow(self.alp, k, self.q)
        C2 = (K*M) % self.q

        return (C1, C2)

    def Decrypt(self, C1, C2):
        """
        Ciphertext: (C1 , C2 )
        Calculate K = (C1 ) Xa mod q
        Plaintext: M = (C2 * K^-1) mod q
        """
        K = pow(C1, self.Xa, self.q)
        M = (C2 * pow(K, -1, self.q)) % self.q
        
        return M



