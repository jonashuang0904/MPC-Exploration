a good tool for creting markdown tables: [here](https://www.tablesgenerator.com/latex_tables)

# Optimal Control Frameworks
"Definition" of framework: Has a modeling language and can interface solvers  
Add https://plato.asu.edu/sub/nlores.html#control  
Add 2024-07-18-Benchmark.pdf (Desktop)
<table><thead>
  <tr>
    <th>Name</th>
    <th>Link</th>
    <th>Problem Formulations</th>
    <th>Usable NLP solvers</th>
    <th>Usable QP solvers</th>
    <th>Programming Language</th>
    <th>License</th>
    <th>Comment</th>
  </tr></thead>
<tbody>
  <tr>
    <td>CasADi</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://web.casadi.org/">web.casadi.org</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://web.casadi.org/python-api/">python-api</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://web.casadi.org/docs/">docs</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/casadi/casadi">github.com/casadi</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/casadi/casadi/wiki/Onboarding-Guide">Onboarding-Guide</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>NLPs</td>
    <td>blocksqp, bonmin, fatrop, IPOPT, KNITRO, SNOPT, WORHP, feasiblesqpmethod, qrsqp, scpgen, sqpmethod</td>
    <td>clp, CPLEX, GUROBI, highs, hpipm, hpmpc, OOQP, OSQP, PROXQP, qpOASES, sqic, superscs, ipqp, nlpsol, qrqp</td>
    <td>C, C++, Python, MATLAB, OCTAVE</td>
    <td>LGPL 3.0</td>
    <td>Numerical optimization, optimal control, algorithmic differentiation, sensitivity analysis, IVP, NLP, QP</td>
  </tr>
  <tr>
    <td>do-mpc</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.do-mpc.com/en/latest/">do-mpc.com</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/do-mpc/do-mpc">github.com/do-mpc</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>OCPs with collocation (orthogonal)</td>
    <td>IPOPT, maybe all CasADi solvers</td>
    <td>?</td>
    <td>Python</td>
    <td>LGPL 3.0</td>
    <td>MPC, MHE orthogonal collocation</td>
  </tr>
  <tr>
    <td>control-toolbox</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://control-toolbox.org/">control-toolbox.org</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/control-toolbox">github.com/control-toolbox</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://ct.gitlabpages.inria.fr/gallery/notebooks.html">Gallery Notebooks</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>OCPs with indirect and direct methods</td>
    <td>IPOPT</td>
    <td>?</td>
    <td>Julia</td>
    <td>MIT</td>
    <td>Indirect methods, direct methods (transcription, maybe bocop3)</td>
  </tr>
  <tr>
    <td>JAX, mpcjax</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://jax.readthedocs.io/en/latest/index.html">jax.readthedocs.io</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/rdyro/mpcjax">github.com/rdyro/mpcjax</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>OCPs direct methods</td>
    <td>SCP (maybe SQP) methods</td>
    <td>?</td>
    <td>Python</td>
    <td>MIT</td>
    <td>GPU</td>
  </tr>
  <tr>
    <td>AMPL</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://ampl.com/">ampl.com</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://dev.ampl.com/ampl/introduction.html">Introduction</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>NLPs</td>
    <td>SNOPT, MINOS, KNITRO, IPOPT, CONOPT, LOQO</td>
    <td>COPT, CPLEX, Gurobi, Mosek, Xpress</td>
    <td>Python, C++, MATLAB, CLI, many more</td>
    <td>Proprietary</td>
    <td>Modeling Language</td>
  </tr>
  <tr>
    <td>ACADOS</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/acados/acados">github.com/acados</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://docs.acados.org/">docs.acados.org</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>OCPs with multiple shooting</td>
    <td>ACADOs (custom SQP)</td>
    <td>HPIPM, qpOASES, DAQP, OSQP</td>
    <td>Python, MATLAB, OCTAVE, C</td>
    <td>BSD 2-Clause</td>
    <td></td>
  </tr>
  <tr>
    <td>FORCESPRO</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.embotech.com/softwareproducts/forcespro/features/">FORCESPRO</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>NLPs and OCPs</td>
    <td>Custom IP and SQP</td>
    <td>?</td>
    <td>Python, MATLAB (C++ only execution)</td>
    <td>Proprietary</td>
    <td></td>
  </tr>
  <tr>
    <td>MUSCOD-II</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://simopt.iwr.uni-heidelberg.de/muscod-ii">MUSCOD-II</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>DIDO</td>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://en.wikipedia.org/wiki/DIDO_(software)">DIDO</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td>OCPs</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Pseudospectral Methods</td>
  </tr>
  <tr>
    <td>PROPT TOMLAB</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Pseudospectral Methods</td>
  </tr>
  <tr>
    <td>GPOPS2</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Pseudospectral Methods</td>
  </tr>
</tbody></table>



# NLP solver 
Add https://plato.asu.edu/sub/nlores.html#general Section General nonlinear constraints, sparse linear algebra for high dimensional problems or other section?

<style type="text/css">

</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Name</span>   </th>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Link</span>   </th>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Method</span>   </th>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Interface</span>   </th>
    <th class="tg-0lax">   <br><span style="font-weight:bold">License</span>   </th>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Comment</span>   </th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br><span style="font-weight:bold">Interior Point Methods</span>&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>IPOPT   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>sparsity   exploiting, good for multiple shooting and collocation   </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>LOQO   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>KNITRO   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br><span style="font-weight:bold">SQP Methods</span>&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>SNOPT   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>general,   good for single shooting   </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>WORHP   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>fmincon   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>NLPQL   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>RFSQP   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>filterSQP   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>NPSOL   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>CONOPT<br>   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>HQP   </td>
    <td class="tg-0lax">   <br><a href="https://hqp.sourceforge.net/">https://hqp.sourceforge.net/</a>   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>good   for multiple shooting   </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>BOCOP3   </td>
    <td class="tg-0lax">   <br><a href="https://github.com/control-toolbox/bocop">https://github.com/control-toolbox/bocop</a>   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br> good for collocation   </td>
  </tr>
</tbody></table>

# QP solver 
<style type="text/css">
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Name</span>   </th>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Link</span>   </th>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Comment</span>   </th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br><span style="font-weight:bold">Sparsity Exploitation</span>&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>qpOASES   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>Combined   with FORCES   </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>qpDUNES   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>HPMPC   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>Combined   with BLASFEO   </td>
  </tr>
  <tr>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br><span style="font-weight:bold">Other</span>&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>CPLEX   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>quadprog   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>MOSEK   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>CVX,   CVXGEN   </td>
    <td class="tg-0lax">   <br><a href="https://cvxgen.com/docs/index.html">https://cvxgen.com/docs/index.html</a>   </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>Gurobi   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
</tbody></table>

# Numerical integration solver
<style type="text/css">

</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Name</span>   </th>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Link</span>   </th>
    <th class="tg-0lax">   <br><span style="font-weight:bold">Comment</span>   </th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br><span style="font-weight:bold">IVP</span>&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>DASSL   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>DASPK2.0   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>CVODE   </td>
    <td class="tg-0lax">   <br><a href="https://computing.llnl.gov/projects/sundials">https://computing.llnl.gov/projects/sundials</a>   </td>
    <td class="tg-0lax">   <br>IVP ODE   </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>IDA   </td>
    <td class="tg-0lax">   <br><a href="https://computing.llnl.gov/projects/sundials">https://computing.llnl.gov/projects/sundials</a>   </td>
    <td class="tg-0lax">   <br>IVP DAE   </td>
  </tr>
  <tr>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br><span style="font-weight:bold">Sensitivity Analysis</span>&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td class="tg-7dil">&nbsp;&nbsp;&nbsp;<br>&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>DSL48S   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>DASPK3.0   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>CVODES   </td>
    <td class="tg-0lax">   <br><a href="https://computing.llnl.gov/projects/sundials">https://computing.llnl.gov/projects/sundials</a>   </td>
    <td class="tg-0lax">   <br>IVP ODE   Sensitivity   </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>DASPKadjoint   </td>
    <td class="tg-0lax">   <br>    </td>
    <td class="tg-0lax">   <br>    </td>
  </tr>
  <tr>
    <td class="tg-0lax">   <br>IDAS   </td>
    <td class="tg-0lax">   <br><a href="https://computing.llnl.gov/projects/sundials">https://computing.llnl.gov/projects/sundials</a>   </td>
    <td class="tg-0lax">   <br>IVP DAE   Sensitivity   </td>
  </tr>
</tbody></table>
