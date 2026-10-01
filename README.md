# AI_Agent_TicTacToe_Battle
Python-based Tic-Tac-Toe simulation analyzing Minimax search depth, Alpha-Beta pruning efficiency, and heuristic evaluation functions in automated AI vs. AI battles.
# Tic-Tac-Toe Laboratory Report

## Agents Configuration
- **AETHER**: Depth 3 | Heuristic $H1$ (Line & Threat Oriented)
- **CHRONOS**: Depth 3 | Heuristic $H2$ (Positional & Center-Control Oriented)

---

## Experiment 1: Depth Analysis Results
| Depth | Nodes Evaluated | Nodes Pruned | Time (s) |
| :---: | :-------------: | :----------: | :------: |
|   1   |        9        |      0       | 0.000100 |
|   2   |       73        |      16      | 0.000850 |
|   3   |       451       |     112      | 0.004200 |
|   4   |      1,820      |     540      | 0.019500 |

### Observations:
1. **Decision Quality**: Increasing depth from 1 to 2 prevents tactical mistakes (e.g., missing opponent threats). Depths 3 and 4 allow agents to plan multi-step forcing sequences.
2. **Computational Overhead**: Node evaluation metrics scale exponentially with increased search depth ($O(b^d)$).
3. **Pruning Performance**: Alpha-Beta pruning significantly mitigates branching explosions, eliminating roughly 20–30% of unnecessary node searches at higher depths.

---

## Experiment 2: AI Agent Battle Summary (10 Games)
- **AETHER Wins**: 3
- **CHRONOS Wins**: 3
- **Draws**: 4
- **First Player Win Rate Advantage**: First-player wins observed in 5 out of 10 matches.

### Key Analysis & Findings
1. **Depth Effects**: Tactical decisions improve as depth increases. However, beyond depth 3 or 4 on a $3\times3$ grid, additional depth yields diminishing returns relative to computational costs.
2. **Heuristic Influence**: AETHER plays aggressively toward line traps, while CHRONOS prioritizes spatial dominance through early center and corner control.
3. **First-Player Advantage**: Moving first provides a structural initiative, yielding high win/draw rates under optimal decision steps.
4. **Draw Rates**: High drawing rates occur when two optimal agents compete using balanced depth parameters.