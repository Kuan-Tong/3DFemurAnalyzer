import torch
def farthest_point_sample(xyz, npoint):
    """
    Input:
        xyz: pointcloud data, [B, N, C]
        npoint: number of samples
    Return:
        centroids: sampled pointcloud index, [B, npoint]
    """
    device = xyz.device
    B, N, C = xyz.shape
    centroids = torch.zeros(B, npoint, dtype=torch.long).to(device)
    distance = torch.ones(B, N).to(device) * 1e10
    farthest = torch.randint(0, N, (B,), dtype=torch.long).to(device)
    batch_indices = torch.arange(B, dtype=torch.long).to(device)
    for i in range(npoint):
        # Update the i-th farthest point
        centroids[:, i] = farthest
        # Get the xyz coordinates of this farthest point
        centroid = xyz[batch_indices, farthest, :].view(B, 1, 3)
        # Calculate the Euclidean distance from all points in the set to this farthest point
        dist = torch.sum((xyz - centroid) ** 2, -1)
        # Update distances to record the minimum distance of each point to any sampled point
        mask = dist < distance
        distance[mask] = dist[mask]
        # Find the farthest point from the updated distances matrix to use in the next iteration
        farthest = torch.max(distance, -1)[1]
    return centroids
