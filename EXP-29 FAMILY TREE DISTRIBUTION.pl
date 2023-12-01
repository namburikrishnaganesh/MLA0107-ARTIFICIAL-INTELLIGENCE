father(john, lisa).
mother(mary, lisa).
mother(mary, mike).
father(tom, mary).
father(mike, emma).
mother(emma, olivia).
parent(X, Y) :- father(X, Y); mother(X, Y).
sister(X, Y) :- female(X), parent(Z, X), parent(Z, Y), X \= Y.
grandfather(X, Y) :- father(X, Z), parent(Z, Y).
grandmother(X, Y) :- mother(X, Z), parent(Z, Y).
