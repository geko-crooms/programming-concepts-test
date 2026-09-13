# Programming concepts test

(15 min)

You may **not use any help** unless stated in the text.

## MC

> [!IMPORTANT]
> Provide your answers by editing [`quiz-answers.txt`](quiz-answers.txt) similar to:
> ```txt
> 1,2
> 4
> 3,4
> ```
> Only use `0..9,` symbols.

Which of the **three core programming concepts** are used in the following process?

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

Same question.

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

Same question.

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

---

Does the text description correspond to the flowchart?


> Calculate `n!`. `!` stands for [factorial](https://simple.wikipedia.org/wiki/Factorial). (0! = 1)

```mermaid
flowchart LR
A(Start) --> B[/Input n/] --> C[fact = 1] --> D{is n < 2?}-- yes --> o[/Output fact/] --> E(End)
D-- no -->F[fact = fact * n] --> G[n = n -1] --> C
```

1. Yes
2. No

   
## Open ended

How can the three core programming concepts support you in writing software? Provide your answer in [`free-response.txt`](free-response.txt). 2-3 sentences are plenty.
