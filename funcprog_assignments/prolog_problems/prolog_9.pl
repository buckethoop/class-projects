
pack([], []).
pack([X], [[X]]).
pack([X, X | Rest], [[X | Packed] | PackedRest]) :-
    pack([X | Rest], [Packed | PackedRest]).
pack([X, Y | Rest], [[X] | PackedRest]) :-
    X \= Y,
    pack([Y | Rest], PackedRest).
