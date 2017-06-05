%% Laboratoire 2 Activité 1
clc
close all;
hold on;

g = 9.81;
frame = 1/30;
sol = 10;

x = 0;
xdot = 2;
y = 15;
ydot = -3;

init = [x;xdot;y;ydot];

A = [0 1 0 0; 0 0 0 0; 0 0 0 1; 0 0 0 0];
B = [0;0;0;g];
C = [1 0 0 0; 0 0 1 0];
D = [0;0;];

sim('LaboApp3');
plot(out.data(:,1), out.data(:,2))
axis([0 5 0 20]);