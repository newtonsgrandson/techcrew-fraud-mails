﻿# techcrew-fraud-mails

This repository hosts the TechCrew Fraud Mails Project, an innovative exploration into the use of advanced AI for cybersecurity. Leveraging the power of OpenAI's GPT-3.5, the project focuses on fine-tuning the model using a dataset of fraudulent emails. The objective is to generate realistic synthetic fraud email examples, enhancing the understanding and detection of digital fraud. This initiative serves as a hands-on application of transfer learning techniques and contributes to the broader conversation around AI's role in cybersecurity.

## Description of preprocessing.py
This Python script is designed for processing and transforming a dataset of fraudulent emails into a structured format suitable for analysis and machine learning applications. The script performs several key functions:

### Features:
Reading Text Files: It reads raw email data from a .txt file, extracting the content as a string for further processing.

Data Preprocessing: Utilizes custom functions to split the raw email text into individual emails based on specific delimiters, preparing the data for feature extraction.

Feature Extraction: Analyzes each email to extract key features such as sender, recipient, date, subject, and the email body. The extraction process identifies and separates these features from the raw email text, organizing them into a structured format.

Writing to JSONL: The processed emails are then written to a .jsonl file, where each line contains a JSON object representing an email with its extracted features. This format is particularly useful for machine learning models and further data analysis tasks.

Tabular Transformation: Finally, the script converts the structured email data into a tabular format (DataFrame), which is then exported as a .csv file for easy use in data analysis and machine learning applications.

### Usage:
This script is an essential tool for researchers and data scientists working on email fraud detection, offering a streamlined process for converting unstructured email data into a clean, structured format. By automating the preprocessing and feature extraction steps, it significantly reduces the time and effort required for data preparation, allowing for more focus on analysis and model development.

## Description of main.py
This Python script is an integral part of a larger project aimed at generating synthetic data for email fraud detection research. It leverages the OpenAI API to fine-tune and generate synthetic fraudulent emails based on real-world examples. The script encompasses several critical phases in the data processing and model fine-tuning pipeline:

### Key Functionalities:
Data Preprocessing: Initially, the script reads a dataset of fraudulent emails from a .txt file, processes the content to extract key features from each email, and organizes the data into a structured pandas DataFrame. This structured data is then saved as a .csv file for further analysis and processing.

Interactive Data Labeling: The script prompts the user to input content that simulates interaction with an AI model. It displays an email, and the user is asked to provide a response. This interaction is formatted as a conversation and saved in a .jsonl file, preparing the data for the next stage of fine-tuning the model.

Model Fine-Tuning: Utilizing the OpenAI API, the script takes the prepared .jsonl file as input for fine-tuning a model. This step is crucial for adapting the model to generate synthetic fraudulent emails that closely mimic the characteristics of the dataset.

Usage and References:
The script is designed for researchers and developers working on AI-based solutions for detecting email fraud. It demonstrates a practical application of transfer learning with OpenAI's GPT models, specifically tailored for cybersecurity purposes.

References for further understanding and documentation on using the OpenAI API and model fine-tuning techniques are included within the script, pointing to OpenAI's official platform and cookbook, as well as the fraudulent email corpus hosted on Kaggle.

### Workflow:
The process begins with the extraction of data from a .txt file, followed by preprocessing and structuring the data.
The user interacts with the script to label data, simulating a real-world application scenario.
The labeled data is used to fine-tune a model with the OpenAI API, enhancing its ability to generate synthetic fraudulent emails.
This script is a showcase of applying advanced AI techniques for social good, specifically in the realm of cybersecurity and fraud detection.

## Description of use_your_fine_tuned_model.py
This script is designed to interact with a fine-tuned GPT-3.5 model to generate synthetic data for academic research on email fraud detection. The script automates the process of querying a fine-tuned model with user-input questions and synthesizing responses that simulate fraudulent email content. The generated synthetic data is structured for easy integration into further research and analysis workflows.

### Key Features:
User Interaction: It prompts the user to input questions to be asked to the fine-tuned model. This interactive approach allows for tailored queries that can generate diverse synthetic responses based on the model's training.

Integration with OpenAI API: Utilizes the OpenAI API to send requests to a fine-tuned GPT-3.5 model, facilitating the generation of synthetic responses. The script is set up to handle API interactions efficiently, managing authentication and request formatting seamlessly.

Data Structuring: The responses from the model are structured into a predefined JSON format, capturing the system's prompt, user's query, and the model's synthetic response. This structured data is pivotal for consistency in data handling and analysis.

Saving Synthetic Data: Finally, the generated conversations are saved into a .jsonl file. This format is chosen for its flexibility and compatibility with various data processing and machine learning tools, making it ideal for further analysis or training purposes.

### Usage:
This script is a valuable tool for researchers and practitioners in the field of cybersecurity, particularly those focusing on the detection and analysis of email fraud. By generating synthetic data, it provides a scalable way to enhance datasets for training more robust detection algorithms.

## Description of train_your_fine_tuned_model.py
The fit_fine_tuned class is designed to streamline the process of fine-tuning OpenAI's GPT models using custom datasets. This class provides a structured approach to preparing and submitting datasets for fine-tuning through the OpenAI API, facilitating the development of more specialized and accurate AI models based on specific training data.

### Features and Functionalities:
Initialization with API Key: The class constructor requires an OpenAI API key for authentication, ensuring secure access to OpenAI services.

Model Fine-Tuning: Implements a method to submit .jsonl formatted data to OpenAI for fine-tuning. This method handles the upload of the dataset file, sets it up for fine-tuning, and initiates the fine-tuning job with a specified base model (e.g., gpt-3.5-turbo).

### Usage:
This class is particularly useful for researchers and developers looking to customize the behavior of GPT models for specific tasks, such as text generation, content creation, or any domain-specific application requiring a tailored model. By automating the fine-tuning process, it significantly simplifies the development workflow, enabling users to focus on creating and refining their datasets for optimal model performance.
