minMax([], _, Min, Max) :-
    Min = Max.
minMax([X | Xs], First, Min, Max) :-
    (X < Min ->
        NewMin = X
    ;
        NewMin = Min
    ),
    (X > Max ->
        NewMax = X
    ;
        NewMax = Max
    ),
    minMax(Xs, First, NewMin, NewMax).

listMinMax([X | Xs], (Min, Max)) :-
    minMax(Xs, X, Min, Max).
