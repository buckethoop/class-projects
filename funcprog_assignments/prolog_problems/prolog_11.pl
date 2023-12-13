encode_length([], []).
encode_length([X | Rest], Encoded) :-
    encode_length(Rest, EncodedRest),
    encode_length_helper([X | Rest], EncodedRest, Encoded).
encode_length_helper([], [], []).
encode_length_helper([X | Rest], [], [(1, X)]) :-
    encode_length_helper(Rest, [], []).
encode_length_helper([X | Rest], [(Count, X) | EncodedRest], [(NewCount, X) | EncodedRest]) :-
    NewCount is Count + 1.
encode_length_helper([X | Rest], [(Count, Y) | EncodedRest], [(1, X), (Count, Y) | EncodedRest]) :-
    X \= Y.
