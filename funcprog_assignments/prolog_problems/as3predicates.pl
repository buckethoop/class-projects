% A
is_member(X, [X|_]).

is_member(X, [H|T]) :- H \= X,
    is_member(X, T).


% B
is_subset([], _) :- !.

is_subset([H|T], L2) :- 
    is_member(H, L2), 
    is_subset(T, L2).

% C
    
is_union([], L, L).
    is_union([H|T], L, LR) :- is_member(H, L),
    !,
    is_union(T, L, LR).

is_union([H|T], L, [H|LR]) :- is_union(T, L, LR).
    
% D
    
is_intersect([], _, []) :- !.

is_intersect([H|T], L2, [H|LR]) :- 
    is_member(H, L2), 
    is_intersect(T, L2, LR).

is_intersect([H|T], L2, LR) :- 
    \+ is_member(H, L2),
    is_intersect(T, L2, LR).


% E
    
is_power([], [[]]).
is_power([X|Xs], Pow) :-
    is_power(Xs, RPow),
    add_each(X, RPow, WX),
    append(RPow, WX, Pow).

add_each(_, [], []).
add_each(X, [Set|Sets], NSets) :-
    NSet = [X| Set],
    add_each(X, Sets, RSets),
    NSets = [NSet | RSets].



