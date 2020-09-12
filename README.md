# ct-denoising-redcnn

Abstract: In this study, an in-house residual encoder-decoder convolutional neural network (RED-CNN)-based algorithm was composed and trained using simulated noisy cylindrical polymethyl-methacrylate (PMMA) CT phantom images with a diameter of 26 cm at different noise levels. The model was tested on simulated noisy 21 × 26 cm elliptical PMMA CT phantom images to evaluate its denoising capability using signal to noise ratio (SNR), comparative peak signal-to-noise ratio (cPSNR), structural similarity (SSIM) index, modulation transfer function frequencies (MTF 10%) and noise power spectra (NPS) values as parameters. Evaluation of a possible decrease of image quality was also performed by testing the model using homogenous water phantom and wire phantom images acquired using different mAs values. Results show that the model was able to consistently increase SNR, cPSNR, SSIM values, and the measured noise spectra. However, the noise level on either training or testing data affects the model’s final denoising performance. The lower noise level on testing data images tends to result in oversmoothed images, as indicated by the shift of the NPS curves. In contrast, higher one tends to result in more unsatisfactory denoising performance, as indicated by lower SNR, cPSNR, and SSIM values. Meanwhile, the higher noise level on training data images tends to produce denoised images with reduced sharpness, as indicated by the decrease of the MTF 10% values.

================================================================================

This project is based on RED-CNN paper by Chen et al. (2017) (DOI:10.1109/TMI.2017.2715284). This project has an objective to denoise CT phantom images. CT phantom images are used, rather than the usual anatomical images of patients' body, to evaluate properties including noise texture and image sharpness which are easier to measure in phantom images due to their homogeneity. The main code involving the deep learning model is divided into two parts: model training and the denoising part using the trained model. Most of the training and the prediction part use patches extracted from the original images.
