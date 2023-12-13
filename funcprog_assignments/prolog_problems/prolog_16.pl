
combinations(_, 0, []).
combinations(List, K, [Combination | Rest]) :-
    K > 0,
    K1 is K - 1,
    select(Combination, List, Remaining),
    combinations(Remaining, K1, Rest).

allCombinations(K, List, Combinations) :-
    findall(Combination, combinations(List, K, Combination), Combinations).
