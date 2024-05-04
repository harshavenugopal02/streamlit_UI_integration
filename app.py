import streamlit as st
from PIL import Image

accuracy_values = {
    "LRCN Entropy Based": 0.8934,
    "ConvLSTM Sequence Based": 0.7869,
    "ConvLSTM Entropy Based": 0.8197
}

loss_values = {
    "LRCN Entropy Based": 0.4609,
    "ConvLSTM Sequence Based": 0.55,
    "ConvLSTM Entropy Based": 0.31
}

graph_files = {
    "LRCN Entropy Based": ["Acc_LE.png", "Loss_LE.png"],
    "ConvLSTM Sequence Based": ["Acc_CS.png", "Loss_CS.png"],
    "ConvLSTM Entropy Based": ["Acc_CE.png", "Loss_CE.png"]
}

st.title('Model Performance Dashboard')
st.markdown("---")

selected_model = st.selectbox('Select Model', list(accuracy_values.keys()))

st.header(f'{selected_model} Performance Overview')
st.write(f'**Accuracy:** {accuracy_values[selected_model]:.2%}')
st.write(f'**Loss:** {loss_values[selected_model]:.2%}')

# Display accuracy and loss plots for the selected model
st.header(f'{selected_model} Accuracy and Loss Plots')
st.write("*Hover over the images to view details*")
st.markdown("---")

# Load and display accuracy plot
accuracy_img = Image.open(graph_files[selected_model][0])
st.image(accuracy_img, use_column_width=True, caption=f"{selected_model} Accuracy")

# Load and display loss plot
loss_img = Image.open(graph_files[selected_model][1])
st.image(loss_img, use_column_width=True, caption=f"{selected_model} Loss")
