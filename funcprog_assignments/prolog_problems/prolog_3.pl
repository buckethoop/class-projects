

pair(X, Y) :-
    X =< Y.
order_pairs([], []).
order_pairs([(X, Y) | Rest], [(Min, Max) | OrderedRest]) :-
    pair(X, Y),
    (   X =< Y ->
        Min = X, Max = Y
      ;  Min = Y, Max = X
    ),
    order_pairs(Rest, OrderedRest).
