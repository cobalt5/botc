### Example of a game, with statements, and solving the possible worlds

#### Players: 5 (BaseCount: 3 Townsfolk, 0 Outsiders, 1 Minion, 1 Demon)
#### Script: Trouble Brewing
#### Seating (clockwise): A, B, C, D, E, then back to A

| Player | Claim| Actions|
| -------- | -------- |--------|
| A | Investigator| Sees players E and D, one of them is the Scarlet Woman, night 1|
| B | Chef | Sees 0 pairs, night 1|
| C | Ravenkeeper| Dies night 2, chooses E, sees Empath|
| D | Soldier| Does nothing, executed day 1|
| E | Empath| Sees 1 evil neighbour night 1, sees 2 evil neighbours night 2|

Day 2: players A (Investigator), B (Chef) and E (Empath) are alive.

### Timeline
Positions come from [nightorder.json](nightorder.json).

| Time | Event |
| :--- | :--- |
| $(1, 0)$ | Setup |
| $(1, 44)$ | Investigator (A) |
| $(1, 45)$ | Chef (B) |
| $(1, 46)$ | Empath (E) |
| $(1, D)$ | D is executed |
| $(2, 30)$ | Imp kills C |
| $(2, 64)$ | Ravenkeeper (C) chooses E |
| $(2, 65)$ | Empath (E) |

### Statements

#### Setup
| Condition | Statement|
| -------- | --------- |
|5 players | $\text{PlayerCount}(5) \land \text{BaseCount}(\text{Townsfolk}, 3)\land \text{BaseCount}(\text{Outsider}, 0)\land \text{BaseCount}(\text{Minion}, 1)\land \text{BaseCount}(\text{Demon}, 1)$|

#### Setup Modifiers
The Baron is the only setup modifier on Trouble Brewing. Every other role $R$ on the script has $\text{Mod}(R, G, 0)$ from "Modifiers default to zero".

| Condition | Statement|
| -------- | --------- |
|Baron | $\text{InPlay}(\text{Baron}) \rightarrow \text{Mod}(\text{Baron}, \text{Outsider}, +2) \land \text{Mod}(\text{Baron}, \text{Townsfolk}, -2)$|
|Baron not in play | $\neg\text{InPlay}(\text{Baron}) \rightarrow \text{Mod}(\text{Baron}, \text{Outsider}, 0) \land \text{Mod}(\text{Baron}, \text{Townsfolk}, 0)$|

#### Structural Invariants
Every row of Structural Invariants in [situations.md](situations.md) applies. Filled in for this game, the setup ones give:

| Invariant | Statement|
| -------- | --------- |
|In play defined by setup | $\text{InPlay}(\text{Baron}) \leftrightarrow \bigvee_{X \in \{A, B, C, D, E\}} \text{Role}(X, \text{Baron}, (1, 0))$|
|Setup type counts | $\text{Count}(\{X : \text{Townsfolk}(X, (1, 0))\}) = 3 + \delta(\text{Baron}, \text{Townsfolk})$ <br> $\text{Count}(\{X : \text{Outsider}(X, (1, 0))\}) = 0 + \delta(\text{Baron}, \text{Outsider})$ <br> $\text{Count}(\{X : \text{Minion}(X, (1, 0))\}) = 1$ <br> $\text{Count}(\{X : \text{Demon}(X, (1, 0))\}) = 1$|
|Base counts sum to the player count | $3 + 0 + 1 + 1 = 5 = \lvert\{A, B, C, D, E\}\rvert$|

So there are two possible setups:
- Baron not in play: 3 Townsfolk, 0 Outsiders, 1 Minion, 1 Demon.
- Baron in play: 1 Townsfolk, 2 Outsiders, 1 Minion (the Baron), 1 Demon.

#### Game facts
| Condition | Statement|
| -------- | --------- |
|D executed day 1 | $\text{Executed}(D, 1)$|
|C chose E night 2 | $\text{Chose}(C, E, (2, 64))$|

#### Claims
| Condition | Statement|
| -------- | --------- |
|A claims Investigator, sees E and D as the Scarlet Woman | $(\text{Sober}(A, (1, 44)) \land \text{Align}(A, \text{Good}, (1, 44))) \rightarrow ((\text{Role}(E, \text{Scarlet Woman}, (1, 44)) \oplus \text{Role}(D, \text{Scarlet Woman}, (1, 44))) \lor (\text{Role}(E, \text{Recluse}, (1, 44)) \land \text{Sober}(E, (1, 44))) \lor (\text{Role}(D, \text{Recluse}, (1, 44)) \land \text{Sober}(D, (1, 44))))$|
|B claims Chef, sees 0 | $(\text{Sober}(B, (1, 45)) \land \text{Align}(B, \text{Good}, (1, 45))) \rightarrow \neg(\text{Registers}(C, \text{Evil}, (1, 45)) \land \text{Registers}(D, \text{Evil}, (1, 45))) \land \neg(\text{Registers}(D, \text{Evil}, (1, 45)) \land \text{Registers}(E, \text{Evil}, (1, 45))) \land \neg(\text{Registers}(E, \text{Evil}, (1, 45)) \land \text{Registers}(A, \text{Evil}, (1, 45)))$ <br> **Pairs not including the Chef: (C, D), (D, E), (E, A).**|
|E claims Empath, sees 1 on night 1 | $(\text{Sober}(E, (1, 46)) \land \text{Align}(E, \text{Good}, (1, 46))) \rightarrow [\text{Registers}(D, \text{Evil}, (1, 46))] + [\text{Registers}(A, \text{Evil}, (1, 46))] = 1$ <br> **Everyone is alive, so E's neighbours are D and A.**|
|C claims Ravenkeeper, chose E, sees Empath (Good) | $(\text{Sober}(C, (2, 64)) \land \text{Align}(C, \text{Good}, (2, 64))) \rightarrow \text{Role}(E, \text{Empath}, (2, 64)) \lor (\text{Role}(E, \text{Spy}, (2, 64)) \land \text{Sober}(E, (2, 64)))$|
|E claims Empath, sees 2 on night 2 | $(\text{Sober}(E, (2, 65)) \land \text{Align}(E, \text{Good}, (2, 65))) \rightarrow [\text{Registers}(A, \text{Evil}, (2, 65))] + [\text{Registers}(B, \text{Evil}, (2, 65))] = 2$ <br> **D was executed on day 1 and C was killed at $(2, 30)$, so E's nearest alive neighbours are A and B.**|
|D claims Soldier | No statement: the Soldier gets no information.|

### Solving

#### With the current rules only
Nothing in [situations.md](situations.md) constrains $\text{Sober}$. Every claim row starts with $\text{Sober}(X, \cdot) \land \dots \rightarrow$, so in every world each claim can be switched off by making its player not sober. The setup rows are the only ones that always apply. On their own they allow any 5 players to fill the two setups above, so the claims rule nothing out yet.

#### With the extra assumptions below
These are not in [situations.md](situations.md) yet (see [todo/urgent/](todo/urgent/): sobriety, truthful-claims, role-persistence and alive-dead). They are added here so the example can be solved.

1. **Sobriety:** a player is sober unless they are the Drunk or the Poisoner chose them that night (the Poisoner acts at $(t, 8)$ on later nights). The Drunk believes they are a Townsfolk that is not in play.
2. **Good players claim truthfully:** a Good player claims their own role. A Drunk claims the Townsfolk they believe they are.
3. **Roles do not change:** $\text{Role}(X, R, (1, 0)) \rightarrow \text{Role}(X, R, \tau)$ for every later time $\tau$ (the same for alignment). This ignores the Imp passing to a Minion and the Scarlet Woman becoming the Imp.
4. **The game continued after day 1:** D is not the Imp, and D is not a sober Saint.
5. **C died at night:** the Imp killed C at $(2, 30)$. So C is not the Imp and not the Soldier, and the Imp was not poisoned on night 2.

#### Result
Checked by enumerating every role assignment: **13 possible worlds**.

| Conclusion | Why |
| :--- | :--- |
| The Baron is not in play | It would add 2 Outsiders. All 5 players claim Townsfolk, and the Drunk is the only Good Outsider who can do that, so there is no second Outsider. |
| D is Good and really is the Soldier | If D were evil, E's night 2 reading needs both A and B to be evil, leaving no room for D. E can't be poisoned on night 2 either, because a dead D can't poison. |
| The Demon is A, B or E | A in 6 worlds, B in 4, E in 3 |
| The Minion is the Poisoner, the Spy or the Scarlet Woman | Poisoner in 8 worlds, Spy in 3, Scarlet Woman in 2 |
| The most likely evil pair is A and B | A and B in 6 worlds, A and E in 3, B and E in 2, A and C in 1, C and E in 1 |

Why A and B: if E is sober and Good on night 2, both A and B must register as evil. Every world without that needs E to be evil, or to have been poisoned on night 2.
