```mermaid
graph TD;
    A[HUMAN_INPUT]
    B[AI_EVAULATION]
    C[AI_ASK_AGAIN]
    D[EXECUTE_TOOL]
    A-->B;
    B-->|UNCLEAR|C;
    C-->A;
    B-->|CLEAR|D;
```
