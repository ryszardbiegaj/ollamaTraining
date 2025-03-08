# Local AI Infrastructure with Deepseek

This project demonstrates how to create a local AI infrastructure for processing and customizing advanced language models using computational resources available in a local network. It leverages the capabilities of Deepseek and Ollama.

## Key Features

- **Deepseek**: A language model for specialized tasks such as code generation and text analysis.
- **Ollama**: Software for managing AI models locally.
- **Security**: Full control over data with local processing.
- **Efficiency**: Fast data processing using local computational resources.
- **Customization**: Ability to tailor models to specific contexts and documents.

## Requirements

- A high-performance computer in the local network (minimum 48 GB RAM).
- SSH access to the target computer.
- Ollama software installed.
- Access to the Deepseek model.

## Installation

1. **Install Ollama**:
   - Download and install from [Ollama](https://ollama.ai/download).

2. **Configure SSH**:
   - Ensure you have SSH access to the target computer.

3. **Download Deepseek**:
   - Place the model on the target computer.

## Usage

1. **Connect via SSH**:
   ```bash
   ssh user@remote_host
2. **Run the Model**:
   ```bash
   ollama run deepseek-r1:14b

3. **Customize the Model**:
   - Adapt the model to specific documents and contexts.

## Examples
- **Code Generation**: Use the model to generate code for applications like Spring Boot 3.2.
- **Text Analysis**: Customize the model for analyzing specific text documents.
