% Initialization
function result = init3D(data1, data2)
pointx = data1{1}; % pointx is the number of points in point set 1, data1{1} represents the first cell of data1
X0 = data1{2}; % X0 is the second cell of data1, representing the initial data
X = X0; % (1:2,:)
pointy = data2{1}; % pointy is the number of points in point set 2, data2{1} represents the first cell of data2
Y0 = data2{2}; % Y0 is the second cell of data2, representing the initial data
Y = Y0; % (1:2,:)

xc = mean(X, 2);
yc = mean(Y, 2); % Calculate the mean of each point set; X has three rows for xyz, and the mean is calculated for each row.
% Remove centroid
x1 = X - repmat(xc, [1 pointx]);
Mx = (x1 * x1'); % The original formula is x'*x, but x1 is a 3*n vector, equivalent to x'; x1' is an n*3 vector, equivalent to x

y1 = Y - repmat(yc, [1 pointy]);
My = (y1 * y1');

[Vx, Dx] = eig(Mx, 'nobalance'); % Calculate eigenvalues and eigenvectors
[Vy, Dy] = eig(My, 'nobalance');

% s
sq = sum(sqrt(Dy / Dx));

s = sq;
% s1 = [sq(1), sq(2)];
% s = [s1, 1];
I = [min(s), max(s)];
% I = [min(sq), max(sq)]; % I is the scaling matrix limit
% I = [min(s1), max(s1)];
% s = [1; 1; 1]; % Isotropic scaling
[~, index1] = sort(Dx);
[~, index2] = sort(Dy);
Vx = Vx(:, index1);
Vy = Vy(:, index2);
p1 = Vx(:, 1);
p2 = Vx(:, 2);
p3 = Vx(:, 3);
q1 = Vy(:, 1);
q2 = Vy(:, 2);
q3 = Vy(:, 3);
f = 0.8;  
% if dot(p1, q1) < f
%     p1 = -p1;
% end
% if dot(p2, q2) < f
%    p2 = -p2;
% end
% p3 = cross(p1, p2);
% R = [q1, q2, q3] * inv([p1, p2, p3]);
R = [1 0 0; 0 1 0; 0 0 1];
% R = [1 1 1; 1 1 1; 1 1 1];
% R = [q1, q2, [0; 0; 1]] * inv([p1, p2, [0; 0; 1]]);
% R(3, 3) = 1;

yc = mean(Y0, 2);
% T = (yc - xc);
% xc2 = mean(s * R * X, 2);
xc2 = mean(diag(s) * R * X0, 2);
T = (yc - xc2);
% T = [T(1:2)
result = cell({R; T; s; I});
