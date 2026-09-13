# Programming concepts test

## MC

> [!IMPORTANT]
> Provide your answers by editing `quiz-answers.txt` similar to:
> ```txt
> 1,2
> 4
> 3,4
> ```
> Only use `0..9,` symbols.

Which of the **three core programming concepts** are used in the following processes?

```mermaid
flowchart LR
_(start)--> C{dexterity > 100}-- yes -->A[Attack] --> __(end)
C-- no -->B[Go home] --> D[Drink energy drink] -->  __
```

1. sequence
2. selection
3. repetition
4. condition
5. data

---

```mermaid
flowchart LR
_(start)--> C{altitude > 0}-- yes -->A[/Output "Landing"/]-->D[/Input altitude/]-->C
C-- no -->B[/Output "Landed"/] -->  __(end)
```

1. sequence
2. selection
3. repetition
4. condition
5. data

---

```mermaid
flowchart LR
A(Start) --> B[/Input n/] --> C[i = 0] --> D{i < n ?}-- yes -->F[Do something]-->G[add 1 to i] --> D 
D-- no -->E(End)
```

1. sequence
2. selection
3. repetition
4. condition
5. data
   
## Open ended

How can the three core programming concepts support you in writing software? Provide your answer in `free-response.txt`. 2-3 sentences are plenty.

## Guess my number

You have the following process which describes the game.

```mermaid
flowchart TD
    _(start) --> init[attempts = 0] --> init2[my_number = random number between 1, 100] --> input_pre[/Input guess/] --> check{attempts < 5 AND guess != correct_number?} -- true --> gt_or_lt{guess > my_number?} -- true --> ogt[/Output "Too high"/] --> add_attempts[attempts += 1] --> input_post[/Input guess/] --> check
    check -- false --> check2{guess == my_number?} -- true --> oc[/Output "You got it!"/] --> __(end)
    gt_or_lt -- false --> olt[/Output "Too low"/] --> add_attempts

    check2 -- false --> X[/Output "Out of tries — the number was "/] --> X[/Output my_number/] -->__(end)
```

Implement this process in [guess-my-number.py](guess-my-number.py). The file has **most** of the code lines you need. You only have to arrange them and write some additional code. Use Code Runner and do not forget to save your solution here.
