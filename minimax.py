import math

class MinimaxEngine:
    def __init__(self, heuristic_fn):
        self.heuristic_fn = heuristic_fn
        self.nodes_evaluated = 0
        self.nodes_pruned = 0

    def reset_stats(self):
        """Resets search metrics before execution."""
        self.nodes_evaluated = 0
        self.nodes_pruned = 0

    def search(self, game, depth, alpha, beta, is_maximizing, player_symbol):
        """
        Alpha-Beta Search Algorithm.
        """
        self.nodes_evaluated += 1

        # Base Cases: Game over or cutoff depth reached
        if game.is_terminal() or depth == 0:
            return self.heuristic_fn(game, player_symbol), None

        opponent_symbol = 'O' if player_symbol == 'X' else 'X'
        valid_moves = game.get_valid_moves()
        best_move = None

        if is_maximizing:
            max_eval = -math.inf
            for move in valid_moves:
                child_game = game.clone()
                child_game.make_move(move[0], move[1], player_symbol)
                
                eval_score, _ = self.search(child_game, depth - 1, alpha, beta, False, player_symbol)
                
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move

                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    # Prune remaining sibling branches
                    self.nodes_pruned += (len(valid_moves) - (valid_moves.index(move) + 1))
                    break
            return max_eval, best_move

        else:
            min_eval = math.inf
            for move in valid_moves:
                child_game = game.clone()
                child_game.make_move(move[0], move[1], opponent_symbol)
                
                eval_score, _ = self.search(child_game, depth - 1, alpha, beta, True, player_symbol)
                
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move

                beta = min(beta, min_eval)
                if beta <= alpha:
                    # Prune remaining sibling branches
                    self.nodes_pruned += (len(valid_moves) - (valid_moves.index(move) + 1))
                    break
            return min_eval, best_move