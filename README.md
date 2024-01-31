# Instant3D: AI-Driven 3D Reconstruction

## Overview
Instant3D is an innovative approach to 3D reconstruction, offering a cost-effective and user-friendly solution. 

## Project Highlights
- **Structure from Motion (SfM):** We leverage SfM to merge different viewpoints for effective reconstruction.
- **Key Processes:** The project includes feature matching, determining fundamental and essential matrices, camera pose estimation, triangulation, perspective n-point problem solving, and bundle adjustment.
- **Testing:** Our methods were rigorously tested to ensure reliability and accuracy.

## Challenges and Solutions
- **Image Quality:** We noticed low-resolution images yield poor results. To counter this, we employed upscaling techniques to enhance image quality, significantly improving our reconstruction outcomes.
- **SfM Parameters:** Several factors influence SfM's effectiveness, including image quality, overlap, viewpoint diversity, feature density, lighting conditions, and more.

## Technical Innovation
- **HAT: Hybrid Attention Transformer:** We used HAT SR model for image restoration, which significantly enhances image resolution, vital for our reconstruction process.
- **NeRF Utilization:** NeRF (Neural Radiance Fields) was instrumental in producing novel views and dense 3D reconstructions with high geometric accuracy.

## Conclusion
Our project demonstrates the potential of AI in transforming this field. We've shown how high-resolution images and advanced computational techniques can lead to more accurate and detailed reconstructions.
