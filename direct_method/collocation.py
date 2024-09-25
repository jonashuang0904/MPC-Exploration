import casadi as ca
import numpy as np
import matplotlib.pyplot as plt

# Parameters
########################################################################################################
# MPC Configs
solver_type = "ipopt"
# Solver options
solver_options = {}
# solver_options["qpsol"] = "osqp"
# solver_options["max_iter"] = 500

prediction_horizon = 50
delta_t = 0.02

# Parameters of the used model
m = 1 # The weight of the mass in kg
k = 1 # The spring constant
c = 0.01 # The damping of the system

# bounds for the input u in Newton
u_lb = -10
u_ub = 10

# Simulation Configs
Nsimulation = 100 # Length of the simulation
delta_t_sim = 0.01
traj_freq = 1
traj_amplitude = 0.1
reference_traj = traj_amplitude * np.sin(np.linspace(0, (Nsimulation-1) * delta_t_sim * 2, Nsimulation * 2) * 2 * np.pi * traj_freq)

# Parameters of the system
sim_m = 1 # The weight of the mass
sim_k = 1 # The spring constant
sim_c = 0.01 # The damping of the system

def main():
    # Setup MPC
    ########################################################################################################
    opti = ca.Opti()
    
    # Set up all neccessary optimization variables and additional parameters (which can be set later on)
    x0 = opti.parameter(1, 1)
    dx0 = opti.parameter(1, 1)
    x_ref = opti.parameter(1, prediction_horizon)
    x = opti.variable(1, prediction_horizon + 1)
    dx = opti.variable(1, prediction_horizon + 1)
    u = opti.variable(1, prediction_horizon)
        
    # Initial state constraints
    opti.subject_to(x[0] == x0) # lift off the initial state
    opti.subject_to(dx[0] == dx0) # lift off the initial state

    # initialize objective function
    J = 0
    
    # Build NLP/Optimization Problem over all steps of prediction horizon
    ########################################################################################################
    for i in range(prediction_horizon):
        # state and control at knot points
        x_k = x[i]
        dx_k = dx[i]    
        x_next = x[i+1]
        dx_next = dx[i+1]
        u_k = u[i]
        
        # Dynamics
        f_i = ca.vertcat(dx_k, (u_k - c * dx_k - k * x_k) / m)
        f_next = ca.vertcat(dx_next, (u[min(i+1, prediction_horizon-1)] - c * dx_next - k * x_next) / m) # dirty hack
        
        # interpolation constraint
        x_mid_calc = 0.5 * (x_k + x_next) + delta_t / 8 * (f_i[0] - f_next[0]) # midpoint position
        dx_mid_calc = 0.5 * (dx_k + dx_next) + delta_t / 8 * (f_i[1] - f_next[1]) # midpoint velocity
        u_mid_k = 0.5 * (u[i] + u[min(i+1, prediction_horizon-1)])
        f_mid = ca.vertcat(dx_mid_calc, (u_mid_k - c * dx_mid_calc - k * x_mid_calc) / m) # midpoint dynamics

        # Collocation constraint (Hermite-Simpson method)
        x_mid_dot = -3/(2 * delta_t) * (x_k - x_next) - 0.25 * (f_i[0] + f_next[0]) # midpoint state derivative (velocity)
        dx_mid_dot = -3/(2 * delta_t) * (dx_k - dx_next) - 0.25 * (f_i[1] + f_next[1]) # midpoint state derivative (acceleration)
        delta_x = x_mid_dot - f_mid[0]
        delta_dx = dx_mid_dot - f_mid[1]
        opti.subject_to(delta_x == 0) # state derivative at midpoint = midpoint dynamics (velocity)
        opti.subject_to(delta_dx == 0) # state derivative at midpoint = midpoint dynamics (acceleration)

        # Bound constraints on control
        opti.subject_to(opti.bounded(u_lb, u_k, u_ub))

        # Objective function
        J = J + 10 * (x_next - x_ref[i])**2 + 0.0001 * u_k**2
        
    # Minimize the objective function
    opti.minimize(J)
    opti.solver(solver_type)

    # Run Simulation
    ########################################################################################################
    # Start values
    x_sim = 0
    v_sim = 0
    u_sim = 0
    measured_traj_x = []
    control_traj_u = []

    for i in range(Nsimulation):
        # get current states from simulation here
        # simulation implemented with Euler forward
        x_sim = x_sim + v_sim * delta_t_sim
        v_sim = v_sim + (-k * x_sim - c * v_sim + u_sim) * (delta_t_sim/m)
        measured_traj_x.append(x_sim)
        
    
        # MPC is executed with a lower frequency than the simulation
        if i % int(delta_t/delta_t_sim) == 0:
            indices = [int(delta_t/delta_t_sim) * x + i for x in list(range(1, prediction_horizon + 1))]
            x_ref_now = reference_traj[indices]
            
            # Set start values for MPC
            opti.set_value(x0, x_sim)
            opti.set_value(dx0, v_sim)
            opti.set_value(x_ref, x_ref_now)
            solution = opti.solve()
            
            # warm start for next iteration
            opti.set_initial(solution.value_variables())
            
            u_pred = solution.value(u)
            # print(f"Predicted input: {u_pred}")
            # print(f"Solution at step {i}: u_pred: {u_pred}, x_pred: {solution.value(x)}")
            # print(f"Predicted x: {solution.value(x)}")
            # Use first value of u_pred as system input
            u_sim = u_pred[0]
        control_traj_u.append(u_sim)
            
    
    fig, axs = plt.subplots(2)
    axs[0].plot(reference_traj, label = "x_{ref}")
    axs[0].plot(measured_traj_x, label = "x")
    axs[0].set_ylabel("Distance [m]")
    axs[0].legend()
    
    axs[1].plot(control_traj_u, label = "u")
    axs[1].set_ylabel("Acceleration [a]")
    axs[1].set_xlim(axs[0].get_xlim())
    axs[1].legend()
    
    plt.xlabel("steps [n]")
    plt.show()
    
    
if __name__ == "__main__":
    main()