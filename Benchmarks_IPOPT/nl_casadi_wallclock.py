from casadi import *
import time
"""
This example demonstrates how NL-files, which can be generated
by AMPl or Pyomo, can be imported in CasADi and solved using
e.g. the interface to AMPL

Joel Andersson
2012

"""
start_cpu = time.process_time()
start_clock = time.perf_counter()

# Create an NLP instance
nl = NlpBuilder()

# Parse an NL-file
nl.import_nl("D:\\KIT MIT\\HiWi\\mpc-exploration\\IPOPT\\NL_files\\_arki0003.nl.nl",{"verbose":False})

# NLP solver options
opts = {}
opts["expand"] = True
# opts["verbose"] = True
# opts["ipopt"] = dict(max_iter=10, linear_solver="ma57", hessian_approximation="limited-memory")

# Create an NLP solver
nlpsol = nlpsol("nlpsol", "ipopt", nl, opts)

# Solve NLP
res = nlpsol(lbx=nl.x_lb,
             ubx=nl.x_ub,
             lbg=nl.g_lb,
             ubg=nl.g_ub,
             x0=nl.x_init)

print(res["x"])

end_cpu = time.process_time()
end_clock = time.perf_counter() # provides the highest available resolution to measure a short duration

cpu_time = end_cpu - start_cpu
wall_clock_time = end_clock - start_clock

print(f"CPU time: {cpu_time} seconds")
print(f"Clock time: {wall_clock_time} seconds")