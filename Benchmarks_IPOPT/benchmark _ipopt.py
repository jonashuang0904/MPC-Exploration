# Using panda framework to generate the table for the paper
# using for loop to solve each .nl file and generate the table
# try to use the "try and except" to catch if the computation is not successful
# if the computation is successful, then generate the table
import pandas as pd
import os
from casadi import *
import time

solver_type = 'ipopt'
solver_options = {'ipopt.max_iter': 1000, 
                  'ipopt.print_level': 1, 
                  'print_time': 1, 
                  'ipopt.tol': 1e-6}

# Set the path to the directory containing the .NL files
nl_dir = "path_to_nl_files"


class OptimizationProblem:
    # Initialize the class
    def __init__(self, nl_dir, solver_type, solver_options):
        self.nl_dir = nl_dir
        self.solver_type = solver_type
        self.solver_options = solver_options
        self.nl_files = [f for f in os.listdir(nl_dir) if f.endswith(".nl")]
        self.results = pd.DataFrame(columns=["nlp_f_t_wall", "nlp_f_n_eval","nlp_g_t_wall","nlp_g_n_eval","total_t_wall"])
        self.max_iter = solver_options.get("ipopt.max_iter", 1000)
        
    # Set single file solve method
    def solve(self, nl_file):
        global nlpsol 
        self.nl_path = os.path.join(self.nl_dir, nl_file)
        try:
            # Create an NLP instance
            start_clock = time.perf_counter()
            nl = NlpBuilder()
            
            # Parse an NL-file
            nl.import_nl(self.nl_path, {"verbose": False})
            
            # NLP solver options
            solver = nlpsol("solver", "ipopt", nl, self.solver_options)
            
            # Solve NLP
            res = solver(lbx=nl.x_lb,
                        ubx=nl.x_ub,
                        lbg=nl.g_lb,
                        ubg=nl.g_ub,
                        x0=nl.x_init)
                       
            print(res["x"])
            
            end_clock = time.perf_counter()
            # Calculate the wall clock time
            wall_clock_time = end_clock - start_clock
            # Calculate the number of objective function evaluations and iterations
            
            metrics = {
                "nlp_f_t_wall": solver.stats()['t_wall_nlp_f'],
                "nlp_f_n_eval": solver.stats()['n_call_nlp_f'],
                "nlp_g_t_wall": solver.stats()['t_wall_nlp_g'],
                "nlp_g_n_eval": solver.stats()['n_call_nlp_g'],
                "total_t_wall": solver.stats()['t_wall_total']
            }

            # If the time exceeds 100 seconds, raise an exception
            if wall_clock_time > 100:
                raise Exception("Wall clock time exceeded")
            return metrics
        
        # Catch any exceptions and return an error message   
        except Exception as e:
            print(f"Error solving {nl_file}:{str(e)}")
            print(f"Solver stats: {solver.stats()}")
            return {col: "Error" for col in self.results.columns}
            
    # Set the series solve method
    def solve_series(self):
        for nl_file in self.nl_files:
            metrics= self.solve(nl_file)
            self.results.loc[nl_file] = metrics
            # Save the results to a CSV file
            self.results.to_csv("path_to_results.csv")
            
if __name__ == "__main__":
    # Create an optimization problem instance
    opt_problem = OptimizationProblem(nl_dir, solver_type, solver_options)
    # Solve the optimization problem
    opt_problem.solve_series()
    # Print the results
    print(f"output: {opt_problem.results}")
            