class AlphaBeta:
    def __init__(self):
        self.MAX = float('inf')
        self.MIN = float('-inf')

    def minimax(self, depth, nodeIndex, maximizingPlayer, values, alpha, beta):
        
        if depth == 3:  
            return values[nodeIndex]

        if maximizingPlayer:
            best = self.MIN
            for i in range(2):  
                val = self.minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
                best = max(best, val)
                alpha = max(alpha, best)  
                if beta <= alpha:  
                    break
            return best
        else:
            best = self.MAX
            for i in range(2):  
                val = self.minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
                best = min(best, val)
                beta = min(beta, best)  
                if beta <= alpha:  
                    break
            return best

if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]  
    ab = AlphaBeta()
    result = ab.minimax(0, 0, True, values, ab.MIN, ab.MAX)
    print("The optimal value is:", result)