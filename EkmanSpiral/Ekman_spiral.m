%% written by KSchroder 
%% Program to plot Ekman spiral and save it is a png & eps
%% Input section
clear all; close all;
i=sqrt(-1)                   % To make sure i is the complex i
h=63;                        % Water depth
nut=.02;                     % (constant) turbulence viscosity
phi=32                       % Latitude (deg.)
rho=1028;                    % Water density
tauwx=0;                     % Wind shear stress x-direction
tauwy=0.03;                  % Wind shear stress y-direction
tau=tauwx+tauwy*i;           % Shear stress vector 
                             % in complex notation
f=2*7.29e-5*sin(phi*pi/180); % Coriolis coefficient
dek=31.01                    % Ekman depth
dz=5;                        % Vertical step size
zek=[-h:dz:0];               % Vertical coordinate
%% Define some additional matrices for plotting purposes
xek=zeros(size(zek));        
yek=zeros(size(zek));
taux=zeros(size(zek));
tauy=zeros(size(zek));
taux(end)=tauwx;
tauy(end)=tauwy;
%% Solution of Ekman spiral
s=tau*dek/rho/(1+i)/nut*exp((1+i)/dek*zek);
uek=real(s);
vek=imag(s);
%% Plot results
figure(1);
quiver3(xek,yek,zek,uek,vek,zeros(size(vek)),'linewidth',2);
hold on
quiver3(xek,yek,zek,taux,tauy,zeros(size(tauy)),'r','linewidth',2);
title('Ekman spiral')
xlabel('u');ylabel('v');
zlabel('z')
print('-dpng','ekman.png')
print('-depsc','ekman.eps')