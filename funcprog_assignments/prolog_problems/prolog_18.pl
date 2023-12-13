
merge([], List, List).
merge(List, [], List).
merge([X | Rest1], [Y | Rest2], [X | MergedRest]) :-
    X =< Y,
    merge(Rest1, [Y | Rest2], MergedRest).
merge([X | Rest1], [Y | Rest2], [Y | MergedRest]) :-
    X > Y,
    merge([X | Rest1], Rest2, MergedRest).

mergeSort([], []).
mergeSort([X], [X]).
mergeSort(List, Sorted) :-
    List = [_, _ | _],  % Ensure List has at least two elements
    split(List, Left, Right),
    mergeSort(Left, SortedLeft),
    mergeSort(Right, SortedRight),
    merge(SortedLeft, SortedRight, Sorted).

split(List, Left, Right) :-
    length(List, Length),
    Midpoint is Length // 2,
    length(Left, Midpoint),
    append(Left, Right, List).
