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

|Claim|Meaning|
| :--- | :---: |
|Role(A, R, t)| Player A has role R at day t<br> **Note that $\text{Role}(A, R, t) \rightarrow \neg\text{Role}(B, R, t)$ for all B $\neq$ A**|
|Role(A, R, (t, k))| Player A has role R at night t immediately after night order k|
|Align(A, M, t)| Player A has alignment M at time t|
|Sober(A, t)| Player A is sober at time t|
|Chose(A, B, t) | Player A chose B at time t|
|Redherring(A, t)|Player A is the redherring at time t<br> **Note that redherring status can change.**<br>**Note that Redherring(A, t) $\rightarrow$ Align(A, Good, t).**|
|Registers(A, M, t)|Player A registers as alignment M to the ability resolving at time t<br>**Note that $(\text{Align}(A, \text{Evil}, t) \land \neg\text{Role}(A, \text{Spy}, t)) \rightarrow \text{Registers}(A, \text{Evil}, t)$.**<br>**Note that $(\text{Align}(A, \text{Good}, t) \land \neg\text{Role}(A, \text{Recluse}, t)) \rightarrow \neg\text{Registers}(A, \text{Evil}, t)$.**<br>**The Spy and Recluse may register as either alignment.**|
|Executed(A, t)| Player A was executed on day t


Refer to [nightorder.json](nightorder.json) for the night order
#### Note: 'A' claims ROLE means player 'A' is claming role ROLE
| Situation | Statement |
| :--- | :---: |
|B is executed on day t|$\text{Executed}(B, t)$|
| A claims Washerwoman | $(\text{Sober}(A, (1, k_{\text{Washerwoman}})) \land \text{Align}(A, \text{Good}, (1, k_{\text{Washerwoman}}))) \rightarrow ((\text{Role}(B, R, (1, k_{\text{Washerwoman}})) \oplus \text{Role}(C, R, (1, k_{\text{Washerwoman}}))) \lor \text{Role}(B, \text{Spy}, (1, k_{\text{Washerwoman}})) \lor \text{Role}(C, \text{Spy}, (1, k_{\text{Washerwoman}})))$ <br>Note: $k_{\text{Washerwoman}}$ = 42, refer to [nightorder.json](nightorder.json)|
| A claims Librarian | $(\text{Sober}(A, (1, k_{\text{Librarian}})) \land \text{Align}(A, \text{Good}, (1, k_{\text{Librarian}}))) \rightarrow ((\text{Role}(B, R, (1, k_{\text{Librarian}})) \oplus \text{Role}(C, R, (1, k_{\text{Librarian}})))  \lor\text{Role}(B, \text{Spy}, (1, k_{\text{Librarian}})) \lor \text{Role}(C, \text{Spy}, (1, k_{\text{Librarian}})))$  |
| A claims Investigator | $(\text{Sober}(A, (1, k_{\text{Investigator}})) \land \text{Align}(A, \text{Good}, (1, k_{\text{Investigator}}))) \rightarrow ((\text{Role}(B, R, (1, k_{\text{Investigator}})) \oplus \text{Role}(C, R, (1, k_{\text{Investigator}}))) \lor \text{Role}(B, \text{Recluse}, (1, k_{\text{Investigator}})) \lor \text{Role}(C, \text{Recluse}, (1, k_{\text{Investigator}})))$ |
| A claims Chef, sees N | $(\text{Sober}(A, (1, k_{\text{Chef}})) \land \text{Align}(A, \text{Good}, (1, k_{\text{Chef}}))) \rightarrow$ A set of statements for all pairs of neighbours $(B, C)$ not including the chef:<br>$\text{Registers}(B, \text{Evil}, (1, k_{\text{Chef}})) \land \text{Registers}(C, \text{Evil}, (1, k_{\text{Chef}}))$ <br> where exactly N of these statements are true|
| A claims Empath, sees N| $(\text{Sober}(A, (t, k_{\text{Empath}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Empath}}))) \rightarrow \left([\text{Registers}(B, \text{Evil}, (t, k_{\text{Empath}}))] + [\text{Registers}(C, \text{Evil}, (t, k_{\text{Empath}}))] = N\right)$, where $B, C$ are $A$'s nearest alive neighbours at $(t, k_{\text{Empath}})$ |
| A claims Fortune Teller, chooses B and C, sees Yes | $(\text{Sober}(A, (t, k_{\text{Fortune Teller}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Fortune Teller}})))  \rightarrow (\text{Role}(B, \text{Demon}, (t, k_{\text{Fortune Teller}})) \lor \text{Role}(C, \text{Demon}, (t, k_{\text{Fortune Teller}})) \lor \text{Role}(B, \text{Recluse}, (t, k_{\text{Fortune Teller}})) \lor \text{Role}(C, \text{Recluse}, (t, k_{\text{Fortune Teller}})) \lor \text{Redherring}(B, (t, k_{\text{Fortune Teller}})) \lor \text{Redherring}(C, (t, k_{\text{Fortune Teller}})))$ |
| A claims Fortune Teller, chosses B and C, sees No | $(\text{Sober}(A, (t, k_{\text{Fortune Teller}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Fortune Teller}})))  \rightarrow (\neg\text{Role}(B, \text{Demon}, (t, k_{\text{Fortune Teller}})) \land \neg\text{Role}(C, \text{Demon}, (t, k_{\text{Fortune Teller}})) \land \neg\text{Redherring}(B, (t, k_{\text{Fortune Teller}})) \land \neg\text{Redherring}(C, (t, k_{\text{Fortune Teller}})))$ |
| A claims Undertaker, see's role R (Good) | check day t-1 to find Executed(B, t-1) and find player B<br>$(\text{Sober}(A, (t, k_{\text{Undertaker}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Undertaker}})))\rightarrow \text{Role}(B, R, t-1) \lor \text{Role}(B, \text{Spy}, t-1)$<br> Note: the undertaker sees the role immediately after execution, the information the undertaker receives is not affected by roles like pithag or barber.|
| A claims Undertaker, see's role R (Evil), B was executed ysterday | $(\text{Sober}(A, (t, k_{\text{Undertaker}})) \land \text{Align}(A, \text{Good}, (t, k_{\text{Undertaker}})))\rightarrow\text{Role(B, R, t-1)}\lor\text{Role}(B, \text{Recluse}, t-1)$|
