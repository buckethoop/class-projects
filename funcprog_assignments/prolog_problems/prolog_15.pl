generate_list(A, B, List) :-
    A > B,
    List = [].
generate_list(A, A, [A]).
generate_list(A, B, [A | Rest]) :-
    A < B,
    Next is A + 1,
    generate_list(Next, B, Rest).
