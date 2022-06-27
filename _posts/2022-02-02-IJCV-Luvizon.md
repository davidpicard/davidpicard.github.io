---
layout: post
title: "Consensus-based optimization for 3D human pose estimation in camera coordinates "
categories: publications
authors: Diogo C Luvizon, David Picard, Hedi Tabia
venue: "International Journal of Computer Vision"
arxiv: https://arxiv.org/abs/1911.09245
code: https://github.com/dluvizon/3d-pose-consensus
doi: https://doi.org/10.1007/s11263-021-01570-9
image: /images/3dconsensus.jpg
---

3D human pose estimation is frequently seen as the task of estimating 3D poses relative to the root body joint. Alternatively, we propose a 3D human pose estimation method in camera coordinates, which allows effective combination of 2D annotated data and 3D poses and a straightforward multi-view generalization. To that end, we cast the problem as a view frustum space pose estimation, where absolute depth prediction and joint relative depth estimations are disentangled. Final 3D predictions are obtained in camera coordinates by the inverse camera projection. Based on this, we also present a consensus-based optimization algorithm for multi-view predictions from uncalibrated images, which requires a single monocular training procedure. 
