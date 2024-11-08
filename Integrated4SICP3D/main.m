% close all
% clear all
% clc
global s R T
%% Read point cloud data of healthy patients.
% D = dir('');
% for i = 1 : length(D)
%     load(['' D(i).name]);
% end
%% 
% load M1;
% M1 = health_mean;
M1 = health_mean;
% load M2;
M2 = health123;
% M2 = fracture104;
plot_3d_3(M1, M2);
M3=fSICP3D(M1, M2);
plot_3d_3(M1, M3);

%M3=M2()
% R = R.';


