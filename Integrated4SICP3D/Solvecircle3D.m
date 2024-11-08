% Iteratively update R, S, T
function c = Solvecircle3D(s, R, T, I, X, Y, Yo)
global intervalz;

pointx = length(X(1,:)); % pointx is the number of columns in X, representing the number of points in point set X
% pointy = length(Y(1,:));
Xo = diag(s) * R * X + repmat(T, [1 pointx]);
% diag: Place the diagonal elements into a column vector
% repmat: Stack a matrix to extend it into a larger matrix; tile T into [1, pointx], replicating T into pointx columns
% Xo = SRX + T
k = dsearchn(Y', Yo, Xo'); % Yo is the triangulated matrix of Y', finding the closest point in Y' to each point in Xo', e.g., if they are the 1st, 6th, and 8th points, then k = 1, 6, 8
Z = Y(:, k); % Z is the set of all nearest neighbor points, reordering points in TARGET point to match the nearest neighbors of Xo'

% for s = 1:10
%     z = s * intervalz;
%     posy = find(Y(3,:) == z);
%     posx = find(Xo(3,:) == z);
%     k = dsearchn(Y(:, posy)', Xo(:, posx)');
%     Z(:, posx) = Y(:, posy(k));
% end

en = computeE(s, R, T, X, Z);
% xc, zc are the row means of X and Z, i.e., the centroids of the two point sets
xc = mean(X, 2); 
zc = mean(Z, 2);
% H = zeros(3,3);
% Center both point sets
Xi = X - repmat(xc, [1 pointx]);
Zi = Z - repmat(zc, [1 pointx]);

% Use the centered point sets Xi and Zi to compute the rotation matrix Rn
Rn = computeR(s, Xi, Zi);
sn = computeS(I, Rn, Xi, Zi);
Tn = computeT(zc, sn, Rn, xc);
fn = computeE(sn, Rn, Tn, X, Z);
c = cell({Rn; Tn; sn; en; fn});
end
 
% Compute R(k+1) using singular value decomposition
function Rn = computeR(s, Xi, Zi)
% Xi = Xi(1:2,:);
% Zi = Zi(1:2,:);
% H = [0 0 0; 0 0 0; 0 0 0];
% for i = 1:length(Xi)
% H = (diag(s) * Xi(:, i) * (Zi(:, i))') + H;  
% end
% H = H / length(Xi);
H = (diag(s) * Xi * Zi') ./ length(Xi);
% H = Xi * Zi'; % SJTang - compute H for the centered point cloud arrays
[U, S, V] = svd(H);

if round(det(V * U')) == 1 % Round off |V * U'|
    Rn = V * U';
elseif round(det(V * U')) == -1
    x = [1 0 0; 0 1 0; 0 0 -1];
    Rn = V * x * U';
end

% if Rn(3,3) < 0
%     Rn(3,3) = -Rn(3,3);
% end
% Rn(3,3) = 1;
end

% Compute s(k+1)
function sn = computeS(I, Rn, Xi, Zi) % I is the scaling limit
% sn = sum(dot(Rn * Xi, Zi)) / sum(dot(Xi, Xi));

sn = dot(Rn * Xi, Zi, 2) ./ dot(Xi, Xi, 2); % dot( , , 2) does a row-wise dot product
% sn = [1; 1; 1];
%
%
% if sn <= I(1)
%     sn = I(1);
% elseif sn >= I(2)
%     sn = I(2);    
% end

% I(1) <= sn <= I(2)
sn = max(sn, I(1));
sn = min(sn, I(2));

% sn = repmat(mean(sn(1:2)), 3, 1); 

% sn = max(repmat(mean(sn), 3, 1), I(1));
% sn = min(repmat(mean(sn), 3, 1), I(2));
end

% Compute T(k+1)
function Tn = computeT(zc, sn, Rn, xc)
% Tn = zc - sn * Rn * xc;
Tn = zc - diag(sn) * Rn * xc;
% Tn = [Tn(1:2)
%     0];
end

function e = computeE(s, R, T, X, Z) 
pointx = length(X(1,:));
% c = s .* (R * X) + repmat(T, [1 pointx]) - Z;
c = diag(s) * (R * X) + repmat(T, [1 pointx]) - Z;
e = sum(dot(c, c)); % dot: column vector dot product, [(R1S1x1 + T1 - z1)^2 + (R2S2x2 + T2 - z2)^2 + ... }
end
