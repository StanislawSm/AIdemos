import numpy as np

class HMM:
    def __init__(self, observed, transition_matrix, emission_matrix, initial_distribution):
        self.I = initial_distribution
        self.V = np.array(observed)
        self.A = np.array(transition_matrix)
        self.B = np.array(emission_matrix)

        self.K = self.A.shape[0]
        self.N = self.V.shape[0]

    def forward(self):
        N = self.N  # observed amount
        K = self.K  # transition amount
        I = self.I  # initial distribution
        B = self.B  # emission
        V = self.V  # observed
        A = self.A  # transition

        alpha = np.zeros((N, K))
        for t in range(0, N):
            for j in range(0, K):
                if t == 0:
                    alpha[t, j] = I[j] * B[j, V[t]]
                else:
                    for i in range(0, K):
                        alpha[t, j] += alpha[t - 1, i] * A[i, j]
                    alpha[t, j] *= B[j, V[t]]

        return np.argmax(alpha, axis=1), alpha

    def backward(self):
        beta = np.zeros((self.N, self.K))
        # TODO: calculate backward values


        return np.argmax(beta, axis=1), beta

    def forward_backward(self):
        fbv = np.zeros((self.N, self.K))
        # TODO: calculate forward-backward values


        return np.argmax(fbv, axis=1)

    def viterbi(self):
        T1 = np.empty((self.K, self.N))
        T2 = np.empty((self.K, self.N), np.int)
        # TODO: calculate T1 and T2 values


        # TODO: .. and viterbi hidden state sequance
        viterbi = np.empty(self.N, np.int) # placeholder

        return viterbi





