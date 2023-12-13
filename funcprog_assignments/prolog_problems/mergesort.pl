mergesort([], []).

mergesort([X], [X]).

mergesort(List, Sort) :-
    List = [_|_], 
    split(List, L, R),
    mergesort(L, SortL),
    mergesort(R, SortR),
    merge(SortL, SortR, Sort).

split(List, L, R) :-
    length(List, Len),
    HalfLen is Len // 2,
    length(L, HalfLen),
    append(L, R, List).

merge([], Sort, Sort).

merge(Sort, [], Sort).

merge([X|RestA], [Y|RestB], [X|Rest]) :-
    X =< Y,
    merge(RestA, [Y|RestB], Rest).

merge([X|RestA], [Y|RestB], [Y|Rest]) :-
    X > Y,
    merge([X|RestA], RestB, Rest).
