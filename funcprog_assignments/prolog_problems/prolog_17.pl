
partition([], _, [], []).
partition([H | T], Pivot, [H | Lesser], Greater) :-
    H =< Pivot,
    partition(T, Pivot, Lesser, Greater).
partition([H | T], Pivot, Lesser, [H | Greater]) :-
    H > Pivot,
    partition(T, Pivot, Lesser, Greater).

splitList(List, (Lesser, Greater)) :-
    List = [Pivot | _],
    partition(List, Pivot, Lesser, Greater).
