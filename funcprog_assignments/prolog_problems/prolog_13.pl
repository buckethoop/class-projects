sublist([], _, _, []).
sublist(_, A, B, []) :- A > B.
sublist([X | Rest], A, B, [X | SublistRest]) :-
    A =< B,
    A > 1,
    NewA is A - 1,
    NewB is B - 1,
    sublist(Rest, NewA, NewB, SublistRest).
sublist([_ | Rest], A, B, Sublist) :-
    A > 1,
    NewA is A - 1,
    sublist(Rest, NewA, B, Sublist).
