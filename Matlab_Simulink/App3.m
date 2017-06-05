clc
clear all;
close all;
hold on;

axis([-2 16 -2 12]);

%% variables
g = -5;
frame = 1/48;
rayon = 1.5;

A = [0 1 0 0; 0 0 0 0; 0 0 0 1; 0 0 0 0];
B = [0;0;0;g];
C = [1 0 0 0; 0 0 1 0];
D = [0;0;];

%% 1rst curve
x = 0;
xdot = 1.5;
y = 10;
ydot = -5;
init = [x;xdot;y;ydot];
sol = 1.2;
sim('LaboAPP3');
plot(out.data(:,1), out.data(:,2));
circle(x,y,rayon);

%% 2nd curve
tmp = out.data(:,1);
x = tmp(end);
xdot = 1.5;
tmp = out.data(:,2);
y = tmp(end);
ydot = (out.time(end)*g - 5)*(-0.9);
init = [x;xdot;y;ydot];
sol = 1.0;
sim('LaboAPP3');
plot(out.data(:,1), out.data(:,2));
circle(x,y,rayon);

%% 3rd curve
tmp = out.data(:,1);
x = tmp(end);
xdot = 1.5;
tmp = out.data(:,2);
y = tmp(end);
ydot = (out.time(end)*g + ydot)*(-0.8);
init = [x;xdot;y;ydot];
sol = 1.5;
sim('LaboAPP3');
plot(out.data(:,1), out.data(:,2));
circle(x,y,rayon);

%% 4th curve
tmp = out.data(:,1);
x = tmp(end);
xdot = 1.5;
tmp = out.data(:,2);
y = tmp(end);
ydot = (out.time(end)*g + ydot)*(-0.7);
init = [x;xdot;y;ydot];
sol = 1;
sim('LaboAPP3');
plot(out.data(:,1), out.data(:,2));
circle(x,y,rayon);

tmp = out.data(:,1);
x = tmp(end);
xdot = 1.5;
tmp = out.data(:,2);
y = tmp(end);
circle(x,y,rayon);
%% Sol
line([0 1], [0 0]);
line([1 1], [0 1.2]);
line([1 4], [1.2 1.2]);
line([4 4], [1.2 1]);
line([4 8], [1 1]);
line([8 8], [1 1.5]);
line([8 11],[1.5 1.5]);
line([11 11], [1.5 1]);
line([11 15],[1 1]);

%% Cercles
function h = circle(x,y,rayon)
th = 0:pi/15:2*pi;
xunit = rayon * cos(th) + x;
yunit = rayon * sin(th) + y;
plot(xunit,yunit,'g.');
end