
evaluate_polynomial([], _, 0).
evaluate_polynomial([Coeff | Rest], X0, Result) :-
    length([Coeff | Rest], Degree),
    power(X0, Degree, X0RaisedToDegree),
    TermResult is Coeff * X0RaisedToDegree,
    evaluate_polynomial(Rest, X0, RestResult),
    Result is TermResult + RestResult.
