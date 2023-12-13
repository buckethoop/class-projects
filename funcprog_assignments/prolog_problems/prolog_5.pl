
sum_pairs([], []).
sum_pairs([(X, Y) | Rest], [Sum | Result]) :-
    Sum is X + Y,
    sum_pairs(Rest, Result).
