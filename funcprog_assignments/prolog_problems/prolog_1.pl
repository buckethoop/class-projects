

power(_, 0, 1).
power(X, Y, Result) :-
    Y > 0,
    Y1 is Y - 1,
    power(X, Y1, TempResult),
    Result is X * TempResult.
