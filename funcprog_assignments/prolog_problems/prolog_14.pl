sublist([], _, _, []).
sublist(List, A, B, Sublist) :-
    length(List, Length),
    A > B,
    WrapA is A mod Length,
    sublist(List, WrapA, B, Sublist).
sublist(List, A, B, []) :-
    A > B,
    length(List, Length),
    A > Length.
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
