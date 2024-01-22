# SAT Competition 2022: Call for Solvers and Benchmarks

The 2022 SAT Competition is a competitive event for solvers of the Boolean Satisfiability (SAT) problem. It is organized as a satellite event to the 25th International Conference on Theory and Applications of Satisfiability Testing and stands in the tradition of the annual SAT Competitions and Races. The deadline for *submitting benchmarks and solvers* is April 1, 2022 (23:59 GMT -12). We leave a margin for *updating solver sources* until April 15, 2022 (23:59 GMT -12). Both deadlines are firm in that you may not upload any new submissions after April 1, and no further updates are possible after April 15. Visit the competition website at https://satcompetition.github.io/2022/ for details.

The area of SAT solving has seen tremendous progress over the last years. Many problems in applications such as hardware and software verification that seemed to be completely out of reach a decade ago can now be handled routinely. Besides new algorithms and better heuristics, refined implementation techniques turned out to be vital for this success.

To keep up the driving force in improving SAT solvers, we want to motivate developers to present their work to a broader audience and to compare it with that of others.

The 2022 SAT Competition will consist of the following tracks:

* Main Track (with CaDiCaL Hack subtrack, and No Limits evaluation)

* 20 Years Special: Anniversary Track

* Parallel Track

* Cloud Track


## Anniversary Track: 20 Years of SAT Competition

International competitions for SAT solvers have a long tradition.
The first events took place in the 1990s (Paderborn 1992, DIMACS 1993, and Beijing 1996).
In 2002, Edward A. Hirsch, Daniel Le Berre, and Laurent Simon initiated a series of regularly scheduled competitions: the SAT Competition as we know it.
Today, we can look back on 20 years of exciting public evaluations and award ceremonies; 20 years of SAT competitions that testify to the tremendous scientific progress made in SAT solving.

We celebrate the 20th anniversary of this event series in the form of a special Anniversary track.
The benchmarks for this track will be comprised of *all benchmark instances* which have been used in Application, Crafted, and Main Tracks of previous SAT competitions.

There will be three categories of this track, one each for Main track, Parallel track and Cloud track solvers.
Participants can submit a maximum of two solvers to the Main category of this track, and one solver for each of the Parallel and Cloud categories.
We particularly welcome you to also submit solvers or configurations which are tailored to specific instance types.

All submissions to the Anniversary track have to be open source.
Solvers which contain code which could be perceived as instance-specific branching or a result-lookup table will be disqualified.
If you are unsure whether your solver meets these requirements, please feel free to contact us.


## New This Year

**CaDiCaL 1.4.1 in Hack Track**

In 2022 SAT Competition, we will use the newer CaDiCaL version 1.4.1 (available at https://github.com/arminbiere/cadical/tree/rel-1.4.1). Participants of the Main track will qualify as a CaDiCaL Hack if the diff between the original and the modified sources of CaDiCaL 1.4.1 is less than 1000 non-space characters.

**Portfolios Allowed in Cloud Track**

In 2022 SAT Competition, the portfolio rule will *not* apply to the Cloud track.


## Other Aspects to Highlight

**Special Innovation Price**

In the Main track, all participating solvers which do not receive an award for their average overall performance are eligible for receiving the special innovation price which is given for best contributions to portfolio performance.

**Bring Your Own Benchmarks (BYOB)**

Each Main track participant (team) is required to submit 20 new benchmark instances (not seen in previous competitions). At least 10 of those benchmarks should be "interesting": not too easy (i.e., not solved by MiniSat within one minute on modern hardware) or not too hard (unsolvable by the participant's own solver within one hour on a computer similar to the nodes of the StarExec cluster).

**PAR-2 Scoring Scheme**

The solvers will be ranked based on their penalized average runtime (PAR-2). The PAR-2 score of a solver is defined to be its average runtime over all instances, whereby unsolved instances contribute twice the time limit.

**Cloud track**

Amazon Web Services is enabling and sponsoring a "cloud track" for the SAT Competition in 2022. The solvers in this track will run on 100 16-core computers each with 64GB RAM that can communicate using standard protocols (ssh, MPI) with a timeout of 1000 seconds (wall-clock time) per benchmark problem. Amazon Web Services will provide AWS credits for building and evaluating solvers, which should be more than enough for development and testing purposes.
