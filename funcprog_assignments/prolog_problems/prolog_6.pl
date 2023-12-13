
pair_sums([], (0, 0)).
pair_sums([(X, Y) | Rest], (SumX, SumY)) :-
    pair_sums(Rest, (RestSumX, RestSumY)),
    SumX is X + RestSumX,
    SumY is Y + RestSumY.
