from experiment import ExperimentRunner

if __name__ == "__main__":
    print("==================================================")
    print("   AI AGENT BATTLE - TIC-TAC-TOE EXPERIMENTS   ")
    print("==================================================")
    
    runner = ExperimentRunner()
    
    # Run Experiment 1 (Depth Analysis)
    runner.run_depth_experiment()
    
    # Run Experiment 2 (10-Game Battle)
    runner.run_agent_battle()
    
    print("All tasks completed successfully!")