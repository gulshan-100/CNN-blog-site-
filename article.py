import streamlit as st

def main():
    st.title('Convolutional Neural Networks (CNNs)')

    st.header('Introduction:')
    st.write('Convolutional Neural Networks, or CNNs, are AI models primarily used for visual dataset analysis. When working with datasets in the form of images or videos, CNNs are efficient models for training.')

    st.header('Explanation:')
    st.write('The archtecture of CNN, composed of convolution layers, pooling layers and fully connected layers. Every layer in CNN arhtectrue plays a important role in the working of the CNN model. Various layers of CNN is exp;ained below:')
    
    st.header('Layers:')
    st.write('1. Convolution Layer: Convolution layer is the first layer of CNN applied on the input data. It consists of the convolution operations which is used to extract the fratures from the input data (images, etc), which then be used to build featyure maps. The output of this layer is the imporatnt features present in the input data')
    st.write('2. Pooling Layer: Second layer after convolution layer applied on the input data in CNN is pooling layer. It reduce the dimensions of the feature maps which include all the important features about the input data. Redcuing the dimensions of the feature map help in improving the efifcient of the CNN model')
    st.write('3. Fully Connected Layer: Fully connected layer is the final and most important layer of the CNN model. In this layer, each neuron gets connected to each and evert neuron on the others layers present in the network. This layer takes the responsibility of extracting the high level features from the input data which then helps in predicition and classification of the data. It is followed by the activation functions like softmax, sigmoid, relu activation function which brings non linearity in the model and imrpoves the efficieitny of the model')
    
    st.header('Applications:')
    st.write('1. Bone Fracture detection: CNN can be used in building the AI system for bone fracture detection. Here, the input is the X ray images of the patients. Using these X rays images, model predict the probability of the fracture in the bone, which then classify the x rays into fracture and non fracture.')
    st.write('2. Deepfake detection: CNN model can also be used in building deep fake detection system. Here the model is trained using the real and deep fake images. After training of the model, model will be able to predict where the input image is real of deep fake')
    
    st.header('Challenges:')
    st.write("1. Overfitting: Overfitting is the condition when the model's accuracy on the training data is more then the testing data. Overfitting condition is a big challenge in the CNN model. ")
    st.write('2. Simple architecture: The architecture of the CNN is quite simple which cannot be used to build the complex AI models. For complex model building, we normally use VGG16, ImageNET, and many more complex algorithm.')
    # Add more sections of your article using st.header() and st.write() for each section.

if __name__ == '__main__':
    main()
