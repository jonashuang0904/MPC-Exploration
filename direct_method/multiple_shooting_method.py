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
    x0 = opti.parameter(1,1)
    dx0 = opti.parameter(1,1)
    x_ref = opti.parameter(1,prediction_horizon)
    x = opti.variable(1,prediction_horizon + 1)
    dx = opti.variable(1,prediction_horizon + 1)
    u = opti.variable(1,prediction_horizon)

    # Initial state constraints
    opti.subject_to(x[0] == x0)
    opti.subject_to(dx[0] == dx0)

    # initialize objective function
    J = 0

    # Build NLP/Optimization Problem over all steps of prediction horizon
    ########################################################################################################
    for i in range(prediction_horizon):
        
        # Get relevant optimization variables for this time step
        x_k = x[i]
        dx_k = dx[i]
        x_next = x[i+1]
        dx_next = dx[i+1]
        u_k = u[i]
        
        # Set system dynamics for damper, spring, mass system
        # x_next = x_k + dx_k * t --> this is linear
        opti.subject_to(x_next == x_k + dx_k * delta_t)
        # dx_next = dx_k + ... --> we used Euler forward here, better use RK4!
        opti.subject_to(dx_next == dx_k + (-k * x_k - c * dx_k + u_k) * (delta_t/m))
        
        # Bound constraints on control
        opti.subject_to(opti.bounded(u_lb, u_k, u_ub))
        
        # Add stage cost to objective function
        J = J + 10 * (x_next - x_ref[i])**2 + 0.0001 * u_k**2

    opti.minimize(J)
    opti.solver(solver_type, solver_options)
        

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
            indices = [int(delta_t/delta_t_sim) * x + i for x in list(range(1,prediction_horizon + 1))]
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
