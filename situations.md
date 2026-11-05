### Assume the player claiming the role is player A
#### Assume that Townsfolk may possibly be evil

## Time
Time for day is a single number t, representing day t<br>
Time for night is a pair $(t, k)$: position $k$ in the night order of night $t$ (the First Night list for $t = 1$, the Other Nights list for $t > 1$). Day $t$ is written $(t, D)$; it comes after every position of night $t$ and before $(t + 1, 1)$. $k_R$ is the position of role $R$ in that night's order.

A state claim at $(t, k)$ is the state when the ability at position $k$ resolves, after every earlier position that night.

**Why:** abilities resolve one at a time in night order, and an earlier ability can change the state a later one reads in the same night (the Poisoner poisons before the Empath wakes, the Imp kills before the Empath counts alive neighbours, the Snake Charmer or Pit-Hag changes a character mid-night). Indexing by night alone cannot express a state that changes partway through a night; $(t, k)$ lets each ability read the state at the moment it acts.


#### For reference
| Symbol | Meaning |  
| :--- | :---: |
| $\neg $ A| Not A|
| A $\land $ B| A AND B|
| A $\lor $ B| A OR B|
| A $\oplus $ B| A XOR B|
| A $\rightarrow $ B| If A, then B|
|Count(C) | There are Count(C) instances of C|

|Claim|Meaning|
| :--- | :---: |
|Role(A, R, t)| Player A has role R at day t<br> **Note that $\text{Role}(A, R, t) \rightarrow \neg\text{Role}(B, R, t)$ for all B $\neq$ A**|
|Role(A, R, (t, k))| Player A has role R at night t immediately after night order k|
|Align(A, M, t)| Player A has alignment M at time t|
|Sober(A, t)| Player A is sober at time t|
|Chose(A, B, t) | Player A chose B at time t|
|Redherring(A, t)|Player A is the redherring at time t<br> **Note that redherring status can change.**<br>**Note that Redherring(A, t) $\rightarrow$ Align(A, Good, t).**|
|Registers(A, M, t)|Player A registers as alignment M to the ability resolving at time t<br>**Note that $(\text{Align}(A, \text{Evil}, t) \land \neg(\text{Role}(A, \text{Spy}, t) \land \text{Sober}(A, t))) \rightarrow \text{Registers}(A, \text{Evil}, t)$.**<br>**Note that $(\text{Align}(A, \text{Good}, t) \land \neg(\text{Role}(A, \text{Recluse}, t) \land \text{Sober}(A, t))) \rightarrow \neg\text{Registers}(A, \text{Evil}, t)$.**<br>**A sober Spy or Recluse may register as either alignment.**|
|Executed(A, t)| Player A was executed on day t|
|Night_Protected(A, (t, k)) | Player A is protected from death at night(Innkeeper) <br> **Note that Night_Protected(A, (t, k)) $\rightarrow$ Night_Protected(A, (t, k+1)), up until the role offering protection is killed, or modified**|
|Protected(A, t) | Player A is protected from death, period. (Tea Lady) <br> **Note that Protected(A, (t, k)) $\rightarrow$ Protected(A, (t, k+1)), up until the role offering protection is killed, or modified**|
|Exec_Protected(A, t) | Player A is protected from execution(Devil's advocate, Tea Lady) <br> **Note that Exec_Protected(A, (t, k)) $\rightarrow$ Exec_Protected(A, (t, k+1)), up until the role offering protection is killed, or modified**|
|Safe(A, (t, k)) | Player A is safe from all demon effects (Monk) <br> **Note that Safe(A, (t, k)) $\rightarrow$ Safe(A, (t, k+1)), up until the role offering protection is killed, or modified**|
|Townsfolk(A, t) | Player A is a townsfolk at time t|
|Outsider(A, t) | Player A is an outsider at time t|
|Minion(A, t) | Player A is a minion at time t|
|Demon (A, t) | Player A is a demon at time t|
|PlayerCount(N) | There are N players in the game|
|BaseCount(G, N) | The base number of players of type G (e.g. Townsfolk) is N|
|InPlay(R) | Role R is assigned to some player at setup (setup time is $=(1,0)$)|
|Mod(R, G, d) | Role R changes the setup count of type G by d <br> **Note that d can be negative, and every pair (R, G) has exactly one d (0 if R changes Nothing)**<br>**This rule is here due to some roles being able to change group counts by undetermined amounts (e.g. Godfather)**|


Refer to [nightorder.json](nightorder.json) for the night order

### Setup situations

**Setup Player Counts**
| Situation | Statement |
| :--- | :---: |
|There are 5 players|$\text{PlayerCount}(5) \land \text{BaseCount}(\text{Townsfolk}, 3)\land \text{BaseCount}(\text{Outsider}, 0)\land \text{BaseCount}(\text{Minion}, 1)\land \text{BaseCount}(\text{Demon}, 1)$|

**Setup Modifiers**
| Situation | Statement |
| :--- | :---: |
|Baron|$\text{InPlay}(\text{Baron}) \rightarrow \text{Mod}(\text{Baron}, \text{Outsider}, +2) \land \text{Mod}(\text{Baron}, \text{Townsfolk}, -2)$|
|Godfather|$\text{InPlay}(\text{Godfather}) \rightarrow (\text{Mod}(\text{Godfather}, \text{Outsider}, +1) \land \text{Mod}(\text{Godfather}, \text{Townsfolk}, -1)) \oplus (\text{Mod}(\text{Godfather}, \text{Outsider}, -1) \land \text{Mod}(\text{Godfather}, \text{Townsfolk}, +1))$|
|Fang Gu|$\text{InPlay}(\text{Fang Gu}) \rightarrow \text{Mod}(\text{Fang Gu}, \text{Outsider}, +1) \land \text{Mod}(\text{Fang Gu}, \text{Townsfolk}, -1)$|
|Vigormortis|$\text{InPlay}(\text{Vigormortis}) \rightarrow \text{Mod}(\text{Vigormortis}, \text{Outsider}, -1) \land \text{Mod}(\text{Vigormortis}, \text{Townsfolk}, +1)$|
|Balloonist|$\text{InPlay}(\text{Balloonist}) \rightarrow (\text{Mod}(\text{Balloonist}, \text{Outsider}, 0) \land \text{Mod}(\text{Balloonist}, \text{Townsfolk}, 0)) \oplus (\text{Mod}(\text{Balloonist}, \text{Outsider}, +1) \land \text{Mod}(\text{Balloonist}, \text{Townsfolk}, -1))$|

### Structural Invariants
These hold in every possible world, for all players $A$, $B$ and all times $t$ (day or $(t, k)$), unless a row says otherwise.<br>
Let $\mathcal{T}, \mathcal{O}, \mathcal{M}, \mathcal{D}$ be the sets of Townsfolk, Outsider, Minion and Demon characters on the script, and $\mathcal{P}$ the set of players.<br>
Setup time is $(1, 0)$: after the grimoire is built, before the first position of night 1.

| Invariant | Statement |
| :--- | :---: |
|Every player has exactly one role|$\bigvee_{R} \text{Role}(A, R, t) \land \left(\text{Role}(A, R_1, t) \land \text{Role}(A, R_2, t) \rightarrow R_1 = R_2\right)$|
|No two players share a role|$\text{Role}(A, R, t) \land \text{Role}(B, R, t) \rightarrow A = B$|
|Townsfolk defined by role|$\text{Townsfolk}(A, t) \leftrightarrow \bigvee_{R \in \mathcal{T}} \text{Role}(A, R, t)$|
|Outsider defined by role|$\text{Outsider}(A, t) \leftrightarrow \bigvee_{R \in \mathcal{O}} \text{Role}(A, R, t)$|
|Minion defined by role|$\text{Minion}(A, t) \leftrightarrow \bigvee_{R \in \mathcal{M}} \text{Role}(A, R, t)$|
|Demon defined by role|$\text{Demon}(A, t) \leftrightarrow \bigvee_{R \in \mathcal{D}} \text{Role}(A, R, t)$|
|Every player has exactly one type|$[\text{Townsfolk}(A, t)] + [\text{Outsider}(A, t)] + [\text{Minion}(A, t)] + [\text{Demon}(A, t)] = 1$ <br> **Follows from the rows above, since $\mathcal{T}, \mathcal{O}, \mathcal{M}, \mathcal{D}$ are disjoint; listed so a solver can use it directly.**|
|Every player has exactly one alignment|$\text{Align}(A, \text{Good}, t) \oplus \text{Align}(A, \text{Evil}, t)$|
|In play defined by setup|$\text{InPlay}(R) \leftrightarrow \bigvee_{A \in \mathcal{P}} \text{Role}(A, R, (1, 0))$ <br> **Only setup counts: a Baron created later (e.g. Pit-Hag) does not change type counts.**|
|One modifier per role and type|$\text{Mod}(R, G, d_1) \land \text{Mod}(R, G, d_2) \rightarrow d_1 = d_2$|
|Modifiers default to zero|$\neg\text{InPlay}(R) \rightarrow \text{Mod}(R, G, 0)$, and $\text{Mod}(R, G, 0)$ for every $R$ that has no Setup Modifier row|
|Modifiers preserve player count|$\sum_{G \in \mathcal{G}} \delta(R, G) = 0$ <br> **A check on the modifier rows: a modifier moves players between types, never adds or removes them.**|
|Setup type counts|$\text{BaseCount}(G, b) \rightarrow \text{Count}(\{A : G(A, (1, 0))\}) = b + \sum_{R} \delta(R, G)$|
|Base counts sum to the player count|$\text{PlayerCount}(N) \rightarrow \sum_{G \in \mathcal{G}} b_G = N = \lvert\mathcal{P}\rvert$, where $\text{BaseCount}(G, b_G)$|
|There must be nonnegative group sizes at all times||
|Starting alignment (Good)|$\left(\text{Townsfolk}(A, (1, 0)) \lor \text{Outsider}(A, (1, 0))\right) \rightarrow \text{Align}(A, \text{Good}, (1, 0))$|
|Starting alignment (Evil)|$\left(\text{Minion}(A, (1, 0)) \lor \text{Demon}(A, (1, 0))\right) \rightarrow \text{Align}(A, \text{Evil}, (1, 0))$ <br> **Alignment can change later (e.g. Snake Charmer, Goon); this only fixes it at setup.**|
|At most one Red Herring|$\text{Redherring}(A, t) \land \text{Redherring}(B, t) \rightarrow A = B$|
|Red Herring exists if a Fortune Teller is in play|$\left(\bigvee_{A \in \mathcal{P}} \text{Role}(A, \text{Fortune Teller}, (1, 0))\right) \rightarrow \bigvee_{B \in \mathcal{P}} \text{Redherring}(B, (1, 0))$|
|At most one execution per day|$\text{Executed}(A, t) \land \text{Executed}(B, t) \rightarrow A = B$|

### Role-Event situations
#### Note: 'A' claims ROLE means player 'A' is claming role ROLE
| Situation | Statement |
| :--- | :---: |
| A claims Washerwoman | $(\text{Sober}(A, (1, k_{\text{Washerwoman}})) \land \text{Align}(A, \text{Good}, (1, k_{\text{Washerwoman}}))) \rightarrow ((\text{Role}(B, R, (1, k_{\text{Washerwoman}})) \oplus \text{Role}(C, R, (1, k_{\text{Washerwoman}}))) \lor (\text{Role}(B, \text{Spy}, (1, k_{\text{Washerwoman}})) \land \text{Sober}(B, (1, k_{\text{Washerwoman}}))) \lor (\text{Role}(C, \text{Spy}, (1, k_{\text{Washerwoman}})) \land \text{Sober}(C, (1, k_{\text{Washerwoman}}))))$ <br>Note: $k_{\text{Washerwoman}}$ = 42, refer to [nightorder.json](nightorder.json)|
| A claims Librarian | $(\text{Sober}(A, (1, k_{\text{Librarian}})) \land \text{Align}(A, \text{Good}, (1, k_{\text{Librarian}}))) \rightarrow ((\text{Role}(B, R, (1, k_{\text{Librarian}})) \oplus \text{Role}(C, R, (1, k_{\text{Librarian}})))  \lor(\text{Role}(B, \text{Spy}, (1, k_{\text{Librarian}})) \land \text{Sober}(B, (1, k_{\text{Librarian}}))) \lor (\text{Role}(C, \text{Spy}, (1, k_{\text{Librarian}})) \land \text{Sober}(C, (1, k_{\text{Librarian}}))))$  |
| A claims Investigator | $(\text{Sober}(A, (1, k_{\text{Investigator}})) \land \text{Align}(A, \text{Good}, (1, k_{\text{Investigator}}))) \rightarrow ((\text{Role}(B, R, (1, k_{\text{Investigator}})) \oplus \text{Role}(C, R, (1, k_{\text{Investigator}}))) \lor (\text{Role}(B, \text{Recluse}, (1, k_{\text{Investigator}})) \land \text{Sober}(B, (1, k_{\text{Investigator}}))) \lor (\text{Role}(C, \text{Recluse}, (1, k_{\text{Investigator}})) \land \text{Sober}(C, (1, k_{\text{Investigator}}))))$ |
| A claims Chef, sees N | $(\text{Sober}(A, (1, k_{\text{Chef}})) \land \text{Align}(A, \text{Good}, (1, k_{\text{Chef}}))) \rightarrow$ A set of statements for all pairs of neighbours $(B, C)$ not including the chef:<br>$\text{Registers}(B, \text{Evil}, (1, k_{\text{Chef}})) \land \text{Registers}(C, \text{Evil}, (1, k_{\text{Chef}}))$ <br> where exactly N of these statements are true|
| A claims Empath, sees N| $(\text{Sober}(A, (t, k_{\text{Empath}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Empath}}))) \rightarrow \left([\text{Registers}(B, \text{Evil}, (t, k_{\text{Empath}}))] + [\text{Registers}(C, \text{Evil}, (t, k_{\text{Empath}}))] = N\right)$, where $B, C$ are $A$'s nearest alive neighbours at $(t, k_{\text{Empath}})$ |
| A claims Fortune Teller, chooses B and C, sees Yes | $(\text{Sober}(A, (t, k_{\text{Fortune Teller}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Fortune Teller}})))  \rightarrow (\text{Role}(B, \text{Demon}, (t, k_{\text{Fortune Teller}})) \lor \text{Role}(C, \text{Demon}, (t, k_{\text{Fortune Teller}})) \lor (\text{Role}(B, \text{Recluse}, (t, k_{\text{Fortune Teller}})) \land \text{Sober}(B, (t, k_{\text{Fortune Teller}}))) \lor (\text{Role}(C, \text{Recluse}, (t, k_{\text{Fortune Teller}})) \land \text{Sober}(C, (t, k_{\text{Fortune Teller}}))) \lor \text{Redherring}(B, (t, k_{\text{Fortune Teller}})) \lor \text{Redherring}(C, (t, k_{\text{Fortune Teller}})))$ |
| A claims Fortune Teller, chosses B and C, sees No | $(\text{Sober}(A, (t, k_{\text{Fortune Teller}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Fortune Teller}})))  \rightarrow (\neg\text{Role}(B, \text{Demon}, (t, k_{\text{Fortune Teller}})) \land \neg\text{Role}(C, \text{Demon}, (t, k_{\text{Fortune Teller}})) \land \neg\text{Redherring}(B, (t, k_{\text{Fortune Teller}})) \land \neg\text{Redherring}(C, (t, k_{\text{Fortune Teller}})))$ |
| A claims Undertaker, see's role R (Good) | check day t-1 to find Executed(B, t-1) and find player B<br>$(\text{Sober}(A, (t, k_{\text{Undertaker}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Undertaker}})))\rightarrow \text{Role}(B, R, t-1) \lor (\text{Role}(B, \text{Spy}, (t, k_{\text{Undertaker}})) \land \text{Role}(B, \text{Spy}, t-1)\land \text{Sober}(B, (t, k_{\text{Undertaker}})))$<br> Note: If a Spy gets executed and subsequently pithagged, the undertaker would see the Spy and thus not a Good role.|
| A claims Undertaker, see's role R (Evil), B was executed ysterday | $(\text{Sober}(A, (t, k_{\text{Undertaker}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Undertaker}})))\rightarrow\text{Role(B, R, t-1)}\lor(\text{Role}(B, \text{Recluse}, (t, k_{\text{Undertaker}})) \land \text{Role}(B, \text{Recluse}, t-1)\land \text{Sober}(B, (t, k_{\text{Undertaker}})))$|
| A claims Monk, chose B on night t| $(\text{Sober}(A, (t, k_{\text{Monk}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Monk}})))\rightarrow\text{Safe}(B, (t, k_{\text{Monk}}))$ <br> **Note: works regardless of alignment of B**|
| A claims Ravenkeeper, chose B on night t, and saw role R (Good)| $(\text{Sober}(A, (t, k_{\text{Ravenkeeper}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Ravenkeeper}})))\rightarrow\text{Role}(B, R,(t, k_{\text{Ravenkeeper}})) \lor(\text{Role}(B, \text{Spy}, (t, k_{\text{Ravenkeeper}})) \land \text{Sober}(B, (t, k_{\text{Ravenkeeper}}))) $|
| A claims Ravenkeeper, chose B on night t, and saw role R (Evil)| $(\text{Sober}(A, (t, k_{\text{Ravenkeeper}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Ravenkeeper}})))\rightarrow\text{Role}(B, R,(t, k_{\text{Ravenkeeper}})) \lor(\text{Role}(B, \text{Recluse}, (t, k_{\text{Ravenkeeper}})) \land \text{Sober}(B, (t, k_{\text{Ravenkeeper}}))) $|
| A claims Virgin, nominated by B on day t (Executed) | $(\text{Role}(A, \text{Virgin}, t)\land\text{Sober}(A, t)) \land(\text{Townsfolk}(B, t) \oplus (\text{Role}(B, Spy, t) \land \text{Sober}(B, t)))$|
| A claims Virgin, nominated by B on day t (Not Executed) | $(\text{Sober}(A, t) \land \text{Align}(A, \text{Good}, t)) \rightarrow\neg\text{Townsfolk}(B, t)$|
| A claims Slayer, shoots B on day t (B dies) | $\text{Role}(A, \text{Slayer}, t) \land \text{Sober}(A, t) \land (\text{Demon}(B, t) \oplus \text{Role}(B, \text{Recluse}, t))$|
| A claims Slayer, shoots B on day t (B lives) | $(\text{Sober}(A, t) \land \text{Align}(A, \text{Good}, t)) \rightarrow \neg\text{Demon}(B, t)$|
