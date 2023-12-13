
decode_length([], []).
decode_length([(1, X) | Rest], [X | DecodedRest]) :-
    decode_length(Rest, DecodedRest).
decode_length([(Count, X) | Rest], [X | DecodedRest]) :-
    Count > 1,
    NewCount is Count - 1,
    decode_length([(NewCount, X) | Rest], DecodedRest).
