removeElement([], _, []).
removeElement([X | Xs], Element, NewList) :-
    X = Element,
    removeElement(Xs, Element, NewList).
removeElement([X | Xs], Element, [X | NewList]) :-
    X \= Element,
    removeElement(Xs, Element, NewList).
