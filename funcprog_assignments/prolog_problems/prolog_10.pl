fullPack([],[]).
fullPack([E|T],Result) :- headPackAndRem(E,[E|T],[],[],res(Pack,NL)),
                          fullPack(NL,R1),
                          Result = [Pack|R1].
headPackAndRem(_,[],Acc1,Acc2,Result) :- reverse(Acc2,R1),
                                         Result = res(Acc1,R1).
headPackAndRem(E,[H|T],Acc1,Acc2,Result) :- E = H ->  
                                headPackAndRem(E,T,[E|Acc1],Acc2,Result);
                                headPackAndRem(E,T,Acc1,[H|Acc2],Result).
