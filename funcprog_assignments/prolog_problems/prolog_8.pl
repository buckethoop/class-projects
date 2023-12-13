
eliminate_duplicates([], []).
eliminate_duplicates([X | Rest], Result) :-
    member(X, Rest),    % X is already in the rest of the list
    eliminate_duplicates(Rest, Result).
eliminate_duplicates([X | Rest], [X | Result]) :-
    \+ member(X, Rest), % X is not in the rest of the list
    eliminate_duplicates(Rest, Result).
