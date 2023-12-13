sums([], 0, 0).
sums([X], X, 0).
sums([X,Y|Rest], EvenSum, OddSum) :-
    sums(Rest, RestEvenSum, RestOddSum),
    EvenSum is X + RestEvenSum,
    OddSum is Y + RestOddSum.
