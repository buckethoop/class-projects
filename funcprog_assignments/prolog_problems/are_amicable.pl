divSum(X,Y):- div(X,1,Y).

div(X,Y,0):- Y > X/2,
    !.

div(X,Z,Y):- 0 is X mod Z,
    !,
    Z1 is Z+1,
    div(X,Z1,Y1),
    Y is Y1+Z.

div(X,Z,Y):- Z1 is Z+1,
    div(X,Z1,Y).


amicable_num(X,Y):-
    divSum(X,SumA),
    divSum(Y,SumB),
    SumA=:=Y,
    SumB=:=X.


