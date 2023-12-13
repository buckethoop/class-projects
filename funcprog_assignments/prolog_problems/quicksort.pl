quicksort([], []).

quicksort([Piv|Rest], Sort) :-
    partition(Rest, Piv, Less, Greater),
    quicksort(Less, SortLess),
    quicksort(Greater, SortGreater),
    append(SortLess, [Piv|SortGreater], Sort).

    partition([], _, [], []).
    
partition([X|Rest], Piv, [X|Less], Greater) :-
    X =< Piv,
    partition(Rest, Piv, Less, Greater).
    
partition([X|Rest], Piv, Less, [X|Greater]) :-
    X > Piv,
    partition(Rest, Piv, Less, Greater).

