# Botc Solver Design Doc

### Goal
1. Given a set of inputs, narrow down all worlds sets down to a set of worlds that all satisfy the set of inputs.
2. Provide an intuitive and reasonably efficient method for a user to input the set of inputs
3. Provide an intuitive and ergonomic way to tell the aggregate data of possible worlds to the user, as well as a method for the user to view specific, distinct worlds


### Assumptions
1. All players of good alignment are honest. In a normal game, this means that it is the last day.
2. As an extension of 1. There is no Politician in play, or there is a politician who aims to work for Good.
3. As an extension of 1. There is no Damsel in play, or there is a Damsel in play but all minions are dead/skeptical.
4. No travelers, Lorics, Fabled, etc.

### Implementation

The solver should have 2 components, a user-interface where the user can input the statements, and a solver in the background that receives the input and sends its computed info to back to the UI for the user to view

### User Interface

* Probably done with PyQT or if you guys want to do a web based one that's fine too
* I'll add a diagram of what I think is most intuitive later


### Statement model

This solver will condense all (and I mean ALL) roles into sets of 'statements'. For now this solver will work with the following statements, and we can add more later if we cannot describe a situation using them:

| Statement | Explanation| 
| -------- | -------- | 
| Role(p, r, t) | Player 'p' has role 'r' at time 't' | 
| Align(p, a, t)  | Player 'p' has alignment 'a' at time 't' where alignment is Good or Evil |
| Sober(p, t) | Player 'p' is free from drunkeness & poison at time 't'
| Died(p, t) | Player 'p' died on night 't'
| Executed(p, t) | Player 'p' was execute on day 't'
| Chose(p, x, t) | Player 'p' chose player 'x' at time 't'
| Count(p) = N| There are N cases of condition p

Time 't' is a pair (night, night-order position); see the Time section of situations.md.

We need more, for roles like Spy and Recluse registering different information, as well as Fortune Teller red herring, and vortox absolute false.

Examples:

>If player 'p' claims slayer and shoots player 'q' on day 't', and nothing happens, then we insert this statement to the statement set:

$$
\neg\text{Sober(p, t)}\ \lor\ \text{Align(p, Evil, t)}\ \lor\ \neg\text{Role(q, Demon, t)}
$$

>Meaning: Player 'p' is not sober OR player 'p' is evil OR player 'q' is not the demon

>If player 'p' claims washerwoman and see's player 'q' and 'r' as the Chef, then we insert this statement to the statement set:

$$
(\text{Align(p, Good, 1)}\ \land \ \text{Sober(p, 1)})\rightarrow (\text{Role(q, Chef, 1)} \oplus \ \text{Role(r, Chef, 1)})
$$
>Meaning: If 'p' is good AND sober, THEN q is the Chef XOR r is the Chef.  
>(Note: I used XOR here because only one of them can be the chef, and we don't assume pope is in play)

### Solver Model
TBD, I am thinking of using the CP-SAT Solver library provided by Google.   
link: https://developers.google.com/optimization/cp/cp_solver
