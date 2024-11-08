function plot_3d_3( data1, data2 )

    %data1 = data1;
    %x1 = data1(:, 1);
    %y1 = data1(:, 2);
    %z1 = data1(:, 3);
    pc1 = pointCloud(data1(:,1:3));

    %data2 =data2;
    %x2 = data2(:, 1);
    %y2 = data2(:, 2);
    %z2 = data2(:, 3);
    pc2 = pointCloud(data2(:,1:3));
    
    figure();
    %scatter3(x1, y1, z1, '.','b');
    %hold on;
    %scatter3(x2, y2, z2,'.', 'r');
    pcshowpair(pc1,pc2,'VerticalAxis','Y','VerticalAxisDir','Down');
    hold off;
    axis equal;
    title('Align the first two point clouds');
    xlabel('X');
    ylabel('Y');
    zlabel('Z');
end