%-------------------------------------------------------------
% Facts
employee(john).
employee(franklin).
employee(alicia).
employee(jennifer).
employee(ramesh).
employee(joyce).
employee(ahmad).
employee(james).

salary(john, 30000).
salary(franklin, 40001).
salary(alicia, 25000).
salary(jennifer, 43000).
salary(ramesh, 38000).
salary(joyce, 25000).
salary(ahmad, 25000).
salary(james, 55000).

department(john, research).
department(franklin, research).
department(alicia, administration).
department(jennifer, administration).
department(ramesh, research).
department(joyce, research).
department(ahmad, administration).
department(james, headquarters).

supervise(franklin, john).
supervise(franklin, ramesh).
supervise(franklin, joyce).
supervise(jennifer, alicia).
supervise(jennifer, ahmad).
supervise(james, franklin).
supervise(james, jennifer).

female(alicia).
female(jennifer).
female(joyce).

male(john).
male(franklin).
male(ramesh).
male(ahmad).
male(james).

project(productx).
project(producty).
project(productz).
project(computerization).
project(reorganization).
project(newbenefits).

works_on(john, productx, 32).
works_on(john, producty, 8).
works_on(ramesh, productz, 40).
works_on(joyce, productx, 20).
works_on(joyce, producty, 20).
works_on(franklin, producty, 10).
works_on(franklin, productz, 10).
works_on(franklin, computerization, 10).
works_on(franklin, reorganization, 10).
works_on(alicia, newbenefits, 30).
works_on(alicia, computerization, 10).
works_on(ahmad, computerization, 35).
works_on(ahmad, newbenefits, 5).
works_on(jennifer, newbenefits, 20).
works_on(jennifer, reorganization, 15).
works_on(james, reorganization, 10).

%-------------------------------------------------------------
% Rules
superior(X,Y) :- supervise(X,Y).

subordinate(X,Y) :- superior(Y,X).

% Should you need to write new rules, please enter them here.

%-------------------------------------------------------------
% Queries
% Write your queries here .



