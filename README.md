# Model Predictive Control Exploration
This project aims to give an easily accessible overview of the state of the art in numerical online MPC approaches. The motivation is that we want a deeper understanding of MPC performance related to our research topics.
## Optimal Control Problems

### Continuous Time Optimal Control Problem (CTOCP)

See (Rawlings et al., 2022, p. 543)

![image](https://github.com/user-attachments/assets/53f1f4d0-ce8d-4f02-b98b-747ba1b609c8)


### Discrete Time Optimal Control Problem (DTOCP)

See (Rawlings et al., 2022, p. 536)

![image](https://github.com/user-attachments/assets/ed3e1685-402e-4f93-b583-345b4ee69372)


# MPC Benchmarking

## Tasks
- Definition of common properties of MPC
  - From literature collection
- Overview of existing MPC approaches/methods
  - See mind map
  - What is a good taxonomy?
- Overview of existing MPC tools/frameworks
  - Collect Literature/Websites
  - What are possible criteria of comparison?
- Overview of existing benchmarks of MPCs
  - Collect Literature/Websites
  - What are possible criteria of comparison?
- Analysis (implementation and benchmarking) of selected MPC approaches
- List of MPC experts and organisations 

## Ideas

### Known Problem Classes
- See literature collection and mind map
- optimization problems (OP)
  - unconstrained/constrained
    - feasible/infeasible
  - convex/nonconvex

### New Solution Approaches/Methods
- Particle swarm
- Multi-start
- Forward-backward sweep with costates (probably indirect method) (probably differential dynamic programming)
- Primal-dual problems/feasibility

### Ideas for a Taxonomy
- Which problem classes can be solved by MPCs?
- How are these solution approaches/methods defined?
- What are the differences between them?
- What are possible criteria of comparison?
  - convergence
    - local
    - global
  - performance
    - calculation time
    - numerical precision of the solution
- To which class do our research problems belong?
- Which solution approaches/methods are commonly used for our research problem class?
- Compare own taxonomy with
  - Slides 2024-04-26-MPC-Overview-Ye.pdf

## Possible Tools/Frameworks

### Ideas for Comparison

- What arepossible criteria of comparison?
  - approach/method used/supported by solver
- license
- convergence
  - local
  - global
- performance
  - calculation time
  - numerical precision of the soultion
  - programming language interface

### Academic Benchmarks
- casadi example pack https://github.com/casadi/casadi/releases/download/3.6.4/casadi-example_pack-v3.6.4.zip
- own mass spring damper example https://essgitlab.fzi.de/ess-cit/mpc-exploration/-/blob/main/mass-spring-damper-example.py?ref_type=heads


### Common Interface for Casadi / ACADOS
- Can we use the same interface for solving our optimization problems? (e.g. ACADOS only takes functions depending on x,u)
