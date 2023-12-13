
square(0, 0).
square(N, Result) :-
    N > 0,
    N1 is N - 1,
    square(N1, TempResult),
    Result is TempResult + N + N - 1.
