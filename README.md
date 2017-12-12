# Wizard-Party
CS 170

Orderings Solver for a NP-Complete Problem.

Because Wizards are weird people, when they go to parties they don't like to announce their ages. Instead, Wizard A will say that he/she is not between the ages of Wizard B and Wizard C. Given these constraints, this project solves for the ordering of the Wizards based on their hidden ages!

This problem reduces to a SAT (Boolean Satisfiability or Propositional Satisfiability) Problem and so the solver uses the SAT solver provided by [MiniSAT](http://macappstore.org/minisat/) and a Python interface for setting up SAT problems provided by [SATisPy](https://github.com/netom/satispy). We then used a graph to model the dependencies between Wizards and run a topological sort to yield the final ordering.

For this project, I partnered up with [Kevin Vo](https://github.com/kevin-vo) and [Aleem Zaki](https://github.com/aleemzaki).
