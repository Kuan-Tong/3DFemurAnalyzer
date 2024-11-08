function [data_target] = fSICP3D(data_source, data_target) % Create the function fSICP for the fused image, with inputs data_source and data_target
global s R T
[s, R, T, e, it] = reg3D(data_source', data_target'); % Create the function reg3D for s, R, T, e, it
% plot_3d_3(data_source, data_target);

for i = 1:3
    data_target(:, i) = data_target(:, i) - T(i); % Translate target data by T
    data_target(:, i) = data_target(:, i) / s(i); % Scale target data by s
end
data_target = data_target * R; % Rotate target data by R

% Alternative transformations (commented out):
% data_target = data_target * R;
% for i = 1:3
%     data_target(:, i) = data_target(:, i) / s(i); % Scale target data by s
% end
% for i = 1:3
%     data_target(:, i) = data_target(:, i) - T(i); % Translate target data by T
% end
% data_target = data_target * R^-1; % Apply the inverse rotation
% plot_3d_3(data_source, data_target); 
