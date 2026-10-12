# Task 2.2 - CNN Image Classifier

## Objective
Prepare an image dataset and train a convolutional neural network (CNN) to classify
images using PyTorch.

## Tools Used
- Python
- PyTorch
- torchvision
- NumPy
- Matplotlib
- Jupyter Notebook

## Dataset
Fashion-MNIST (built into torchvision) — 28x28 grayscale images of clothing items
across 10 categories (60,000 training images, 10,000 test images).

## Work Completed
1. Loaded and inspected the Fashion-MNIST dataset with sample image visualization
2. Built DataLoaders for batched training and testing
3. Defined a CNN architecture: 2 convolutional layers (16, 32 filters) with ReLU
   and max pooling, followed by 2 fully connected layers
4. Trained the model for 10 epochs using CrossEntropyLoss and the Adam optimizer
5. Evaluated on the test set and compared train vs test accuracy
6. Visualized training loss/accuracy curves
7. Displayed sample predictions with correct/incorrect labeling
8. Saved the trained model as a .pth file

## Results
- Final training accuracy: ~95.5%
- Test accuracy: ~91.6%
- Test loss: ~0.26
- Small, expected gap between train and test performance — model generalizes well

## Deliverables
- CNN training notebook: `notebooks/cnn_classifier.ipynb`
- Trained model file: `models/cnn_fashion_mnist.pth`
- Screenshots: `screenshots/Rakshitha_Week2_Task2.2_SampleImages.png`,
  `screenshots/Rakshitha_Week2_Task2.2_TrainingCurves.png`,
  `screenshots/Rakshitha_Week2_Task2.2_SamplePredictions.png`

## Key Learnings
- How convolution and pooling layers extract and compress spatial features from images
- Why image tensors use a (batch, channels, height, width) shape, unlike flat tabular data
- The role of CrossEntropyLoss for multi-class classification vs MSE for regression
- How to track and interpret both loss and accuracy during training
- How to save and reload a trained PyTorch model using state_dict()

## Submission Status
Status: Completed
Submitted On: 27 September 2026
