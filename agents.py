import random
import math
from minimax import MinimaxEngine

class Agent:
    """Configurable AI Agent."""
    def __init__(self, name, symbol, depth, heuristic_fn):
        self.name = name
        self.symbol = symbol
        self.depth = depth
        self.engine = MinimaxEngine(heuristic_fn)
        self.last_nodes_eval = 0
        self.last_nodes_pruned = 0

    def choose_move(self, game):
        """Chooses best move using Alpha-Beta Minimax with random tie-breaking."""
        self.engine.reset_stats()
        valid_moves = game.get_valid_moves()
        
        if not valid_moves:
            return None

        move_scores = []
        alpha = -math.inf
        beta = math.inf

        # Evaluate all legal moves
        for move in valid_moves:
            child = game.clone()
            child.make_move(move[0], move[1], self.symbol)
            score, _ = self.engine.search(child, self.depth - 1, alpha, beta, False, self.symbol)
            move_scores.append((score, move))

        # Identify max score
        max_score = max(score for score, _ in move_scores)
        best_moves = [move for score, move in move_scores if score == max_score]

        # Break ties randomly for dynamic games
        chosen_move = random.choice(best_moves)

        self.last_nodes_eval = self.engine.nodes_evaluated
        self.last_nodes_pruned = self.engine.nodes_pruned

        return chosen_move