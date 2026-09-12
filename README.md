# Programming concepts test

## MC

> [!IMPORTANT]
> Provide your answers by editing `quiz-answers.txt` as follows:
> ```txt
> 1,2
> 4
> 3,4
> ```

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
C-- no -->B[/Output "Landed"/] -->  __
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
   
