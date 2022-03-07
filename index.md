## Welcome to LASOR

### LASOR: Learning Accurate 3D Human Pose and Shape Via Synthetic Occlusion-Aware Data and Neural Mesh Rendering 
[Paper](https://arxiv.org/abs/2108.00351) [Code](https://github.com/iGame-Lab/LASOR) 

### Abstract

A key challenge in the task of human pose and shape estimation is occlusion, including self-occlusions, object-human occlusions, and inter-person occlusions. The lack of diverse and accurate pose and shape training data becomes a major bottleneck, especially for scenes with occlusions in the wild. In this paper, we focus on the estimation of human pose and shape in the case of inter-person occlusions, while also handling object-human occlusions and self-occlusion. We propose a novel framework that synthesizes occlusion-aware silhouette and 2D keypoints data and directly regress to the SMPL pose and shape parameters. A neural 3D mesh renderer is exploited to enable silhouette supervision on the fly, which contributes to great improvements in shape estimation. In addition, keypoints-and-silhouette-driven training data in panoramic viewpoints are synthesized to compensate for the lack of viewpoint diversity in any existing dataset. Experimental results show that we are among the state-of-the-art on the 3DPW and 3DPW-Crowd datasets in terms of pose estimation accuracy. The proposed method evidently outperforms Mesh Transformer, 3DCrowdNet and ROMP in terms of shape estimation. Top performance is also achieved on SSP-3D in terms of shape prediction accuracy. 


### Performance

<center>
      <iframe width="560" height="315" src="https://www.youtube.com/embed/9lc7dYCxskQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</center>




### BibTeX

```latex
@ARTICLE{9709705,  
  author={Yang, Kaibing and Gu, Renshu and Wang, Maoyu and Toyoura, Masahiro and Xu, Gang},  
  journal={IEEE Transactions on Image Processing},   
  title={LASOR: Learning Accurate 3D Human Pose and Shape via Synthetic Occlusion-Aware Data and Neural Mesh Rendering},   
  year={2022},  
  volume={31},  
  number={},  
  pages={1938-1948},  
  doi={10.1109/TIP.2022.3149229}
}
```



### Support or Contact

Having trouble with LASOR? Check out our [documentation](https://github.com/iGame-Lab/LASOR/) we’ll help you sort it out.
