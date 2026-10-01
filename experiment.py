import time
import csv
import os
from game import TicTacToe
from agents import Agent
from heuristic import heuristic_h1, heuristic_h2

class ExperimentRunner:
    def __init__(self, output_dir="results"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def run_depth_experiment(self):
        """Experiment 1: Depth Analysis on a single AI Agent."""
        print("--- Running Experiment 1: Depth Analysis ---")
        csv_file = os.path.join(self.output_dir, "depth_experiment.csv")
        
        results = []
        for depth in range(1, 5):
            agent = Agent("a", "X", depth=depth, heuristic_fn=heuristic_h1)
            game = TicTacToe()
            
            start_time = time.perf_counter()
            # Perform search from initial board state
            _ = agent.choose_move(game)
            elapsed_time = time.perf_counter() - start_time

            results.append({
                "Depth": depth,
                "Nodes Evaluated": agent.last_nodes_eval,
                "Nodes Pruned": agent.last_nodes_pruned,
                "Time (s)": f"{elapsed_time:.6f}"
            })

        # Save to CSV
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Depth", "Nodes Evaluated", "Nodes Pruned", "Time (s)"])
            writer.writeheader()
            writer.writerows(results)

        print(f"Experiment 1 complete. Results saved to {csv_file}\n")

    def run_agent_battle(self):
        """Experiment 2: 10-Game AI Agent Battle (AETHER vs CHRONOS)."""
        print("--- Running Experiment 2: AI Agent Battle ---")
        csv_file = os.path.join(self.output_dir, "battle_results.csv")
        
        game_records = []

        for game_num in range(1, 11):
            game = TicTacToe()
            
            # Alternate starting player
            if game_num % 2 != 0:
                p1_name, p1_h = "AETHER", heuristic_h1
                p2_name, p2_h = "CHRONOS", heuristic_h2
            else:
                p1_name, p1_h = "CHRONOS", heuristic_h2
                p2_name, p2_h = "AETHER", heuristic_h1

            agent1 = Agent(p1_name, 'X', depth=3, heuristic_fn=p1_h)
            agent2 = Agent(p2_name, 'O', depth=3, heuristic_fn=p2_h)

            first_player = p1_name
            aether_nodes, chronos_nodes = 0, 0
            aether_pruned, chronos_pruned = 0, 0
            moves_count = 0

            start_time = time.perf_counter()
            current_agent = agent1

            while not game.is_terminal():
                move = current_agent.choose_move(game)
                game.make_move(move[0], move[1], current_agent.symbol)
                moves_count += 1

                if current_agent.name == "AETHER":
                    nexus_nodes += current_agent.last_nodes_eval
                    nexus_pruned += current_agent.last_nodes_pruned
                else:
                    titan_nodes += current_agent.last_nodes_eval
                    titan_pruned += current_agent.last_nodes_pruned

                # Swap turn
                current_agent = agent2 if current_agent == agent1 else agent1

            elapsed_time = time.perf_counter() - start_time
            winner_symbol = game.check_winner()

            if winner_symbol == 'X':
                winner_name = agent1.name
            elif winner_symbol == 'O':
                winner_name = agent2.name
            else:
                winner_name = "DRAW"

            record = {
                "game": game_num,
                "first": first_player,
                "winner": winner_name,
                "moves": moves_count,
                "aether_nodes": aether_nodes,
                "chronos_nodes": chronos_nodes,
                "aether_pruned": aether_pruned,
                "chronos_pruned": chronos_pruned,
                "time_sec": f"{elapsed_time:.4f}"
            }
            game_records.append(record)

        # Save to CSV
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=game_records[0].keys())
            writer.writeheader()
            writer.writerows(game_records)

        print(f"Experiment 2 complete. Results saved to {csv_file}\n")