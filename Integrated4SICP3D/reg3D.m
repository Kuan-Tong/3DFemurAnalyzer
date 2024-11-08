function [s, R, T, e, it] = reg3D(file1, file2)
% data1 = ascread(file1); % 40097 points
% data2 = ascread(file2); % 40256 points
[row1, col1] = size(file1); data1{1} = col1; data1{2} = file1;
[row2, col2] = size(file2); data2{1} = col2; data2{2} = file2;

X = data1{2};
Y = data2{2};

initD = init3D(data1, data2);
R0 = initD{1};
T0 = initD{2};
s0 = initD{3};
I = initD{4};
% I = [0.8 1.2];
o = 10^-6; % 0.001;
Yo = delaunayn(Y'); % Triangulate the point set corresponding to the transpose of Y
% tic;
c0 = Solvecircle3D(s0, R0, T0, I, X, Y, Yo); % Substitute the initialized variables into the model function to get new outputs Rn, Tn, sn, etemp
Rn = c0{1};
Tn = c0{2};
sn = c0{3};
etemp = c0{5}; % Used to calculate accuracy and decide whether to stop the iteration
q = 1; % q is the cancellation indicator for the iteration, initialize q
flag = 2; % Label, indicates that when flag = 2, iteration starts
% Etemp = etemp;

while (q > 0)
    c = Solvecircle3D(sn, Rn, Tn, I, X, Y, Yo);
    Rn = c{1};
    Tn = c{2};
    sn = c{3};
    en = c{5};
    q = 1 - (en / etemp); % q is the iteration condition; as accuracy increases, when q = 1 - en / etemp is met, iteration stops
    etemp = en;
%     Etemp(end + 1) = etemp;
    flag = flag + 1; 
end 
s = sn;
% s = [1; 1; 1];
R = Rn;
T = Tn;
e = en;
it = flag - 1; % Update count

% toc 
% figure;
% plot(Etemp, 'bo-');
% axis tight;
end
