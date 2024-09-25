# MPC-Exploration
# Definitions

## Optimal Control Problems

### Continuous Time Optimal Control Problem (CTOCP)

See (Rawlings et al., 2022, p. 543)

![image](/uploads/aa733567687ddead8058f5de43df280b/image.png)

### Discrete Time Optimal Control Problem (DTOCP)

See (Rawlings et al., 2022, p. 536)

![image](/uploads/ed24e26679fd988d69cd71fba11c84cf/image.png)

# MPC Benchmarking

## Tasks
- Definition common propertiers of MPC @koehrer @grobbel
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
- Analysis (implementation and benchmarking) of selcted MPC approaches
- List of MPC experts and organisations @grobbel

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
- Forward backward sweep with costates (probably indirect method) (probably differential dynamic programming)
- Primal dual problems/feasibility

### Ideas for a Taxonomy
- Which problem classes can be solved by MPCs?
- How are these solution approaches/methods defined?
- What are the differences between them?
- What arepossible criteria of comparison?
  - convergence
    - local
    - global
  - performance
    - calculation time
    - numerical precision of the soultion
- To which class do our reserach problems belong?
- Which of solution approaches/methods are commonly used for our reserach problem class?
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

