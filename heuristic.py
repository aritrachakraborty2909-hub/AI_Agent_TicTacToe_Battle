def heuristic_h1(game, player):
    """
    Heuristic 1 (Line Threat Focus - AETHER):
    Focuses on counting open lines, immediate threats, and double-line potentials.
    """
    opponent = 'O' if player == 'X' else 'X'
    winner = game.check_winner()
    
    if winner == player:
        return 100
    elif winner == opponent:
        return -100
    elif game.is_draw():
        return 0

    score = 0
    lines = _get_all_lines(game.board)

    for line in lines:
        p_count = line.count(player)
        o_count = line.count(opponent)
        
        if p_count == 2 and o_count == 0:
            score += 10  # Strong winning threat
        elif o_count == 2 and p_count == 0:
            score -= 10  # Opponent strong threat
        elif p_count == 1 and o_count == 0:
            score += 2   # Potential line
        elif o_count == 1 and p_count == 0:
            score -= 2   # Opponent potential line

    return score


def heuristic_h2(game, player):
    """
    Heuristic 2 (Positional + Threat Focus - CHRONOS):
    Combines center and corner spatial control with line threat analysis.
    """
    opponent = 'O' if player == 'X' else 'X'
    winner = game.check_winner()
    
    if winner == player:
        return 100
    elif winner == opponent:
        return -100
    elif game.is_draw():
        return 0

    score = 0
    
    # Spatial / Positional Priority
    if game.board[1][1] == player:
        score += 4  # Center control
    elif game.board[1][1] == opponent:
        score -= 4

    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for r, c in corners:
        if game.board[r][c] == player:
            score += 2  # Corner control
        elif game.board[r][c] == opponent:
            score -= 2

    # Line Threat Priority
    lines = _get_all_lines(game.board)
    for line in lines:
        p_count = line.count(player)
        o_count = line.count(opponent)

        if p_count == 2 and o_count == 0:
            score += 12
        elif o_count == 2 and p_count == 0:
            score -= 12

    return score


def _get_all_lines(board):
    """Helper function to extract rows, columns, and diagonals."""
    lines = []
    # Rows and Columns
    for i in range(3):
        lines.append([board[i][0], board[i][1], board[i][2]])
        lines.append([board[0][i], board[1][i], board[2][i]])
    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])
    return lines