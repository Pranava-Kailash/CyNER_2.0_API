
# CyNER 2.0: Named Entity Recognizer

CyNER 2.0 is an advanced Named Entity Recognition (NER) application designed to identify and categorize named entities in text, such as organizations, locations, malware, and more. The application is built with Python, using FastAPI for serving the NER model as an API. The model was developed as part of my MSc Data Science dissertation at the University of Surrey.

The project utilizes state-of-the-art pre-trained transformer models, including DeBERTa, BERT, BioBERT, DarkBERT, and SpaCy. After rigorous testing and evaluation, DeBERTa emerged as the top-performing model with an F1 score of over 91%, making it the core model for CyNER 2.0.

## Project Structure

```
Depolyment/
├── __init__.py
├── database.py
├── main.py
├── model.py
├── ner_data.db
├── Ner_tags_finder.ipynb
├── routers/
│   ├── __init__.py
│   └── ner.py
└── schemas.py
```
## Key Features
**Advanced NER for Cybersecurity**: CyNER 2.0 is specifically fine-tuned to recognize cybersecurity-specific entities such as malware, vulnerabilities, threat actors, systems, and organizations.

**Model Evaluation**: Multiple pre-trained transformer models were tested, and DeBERTa was selected as the best-performing model based on precision, recall, and F1 scores.

**API Deployment**: The project is deployed as an API using FastAPI, making it easy to integrate the NER model into various cybersecurity platforms or applications.

**Dataset Annotation**: The Annotated Dataset used for training and evaluation was created with The Annotator, a custom-built tool that facilitated the annotation of over 11,000 rows of cybersecurity data.

## Testing & Model Evaluation
### Models Tested:
- **BERT**: A widely-used transformer model effective in general-purpose NER tasks.
- **DeBERTa**: Achieved the highest performance on the cybersecurity dataset with an F1 score of over 91%.
- **BioBERT**: Specialized for biomedical data but showed promising results in cybersecurity tasks due to the structured nature of its output.
- **DarkBERT**: Trained on dark web datasets, useful in identifying threat actors and malware.
- **SpaCy NER**: A fast, lightweight model that offers practical usage with moderate performance.

## Testing Results:
### Original Dataset Performance:
- DeBERTa F1 score: 91.30%
- BERT F1 score: 88.50%
- DarkBERT F1 score: 87.10%

### Augmented Dataset Performance:
- DeBERTa F1 score: 91.88%
- BERT F1 score: 89.23%
- DarkBERT F1 score: 88.30%

These results indicate that DeBERTa consistently outperforms the other models, both on the original and augmented datasets.

## Statistical Testing:
Wilcoxon Signed-Rank Test and Bootstrap Resampling were applied to assess the statistical significance of the performance differences between the models.

DeBERTa outperformed the other models with a statistically significant difference. DeBERTa was chosen as the model for Endpoint development

Model uploaded @ [Hugging Face](https://huggingface.co/PranavaKailash/CyNER-2.0-DeBERTa-v3-base)

### Files Description

- `__init__.py`: Indicates that the directory is a Python package.
- `database.py`: Handles database connections and interactions.
- `main.py`: The main entry point of the application, responsible for starting the FastAPI server.
- `model.py`: Contains Base for SQLalchemy
- `ner_data.db`: SQLite database containing the data saved after running NER.
- `Ner_tags_finder.ipynb`: Jupyter Notebook used for testing the API endpoints.
- `routers/ner.py`: Contains the model definitions and logic for NER.
- `schemas.py`: Contains Pydantic models used for data validation and serialization.

## Requirements

To run this project, you need to have the following dependencies installed:

- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn
- SQLite (included by default with Python)
- Jupyter (optional, for running the notebook)

You can install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

## Setting Up the Project

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository_url>
   cd Depolyment
   ```
2. **Install Dependencies**: Install the required Python packages.

   ```bash
   pip install -r requirements.txt
   ```
3. **Running the Application**: Start the FastAPI server using Uvicorn.

   ```bash
   python main.py
   ```
4. **Run Jupyter Notebook**: After starting the server, run the `Ner_tags_finder.ipynb` notebook.

   ```bash
   jupyter notebook Ner_tags_finder.ipynb
   ```

   Follow the steps inside the notebook to test the NER model using the API.

## Usage Example

Once the server is running, you can test the API with the following example:

1. **Example Request**: The input text is provided in the notebook as follows:

   ```python
   data = {
       "text": "For about a week now there have been repeated posts on the BleepingComputer and Malwarebytes forums regarding a BITSADMIN 3.0 command prompt that repeatedly opens on its own and downloads files"
   }
   ```
2. **Example Response**: The API will return the following recognized entities:

   ```json
   {
     "entities": [
       {
         "entity": "BITSADMIN 3.0",
         "label": "B-System"
       },
       {
         "entity": "BleepingComputer",
         "label": "B-Organization"
       },
       {
         "entity": "Malwarebytes",
         "label": "B-Organization"
       }
     ]
   }
   ```
3. **Visualizing Results**: The notebook contains code to visualize the labeled entities in the text with different colors based on the entity type.

## Expected Output

The main output of the project is the API response that includes identified entities in the input text along with their corresponding labels (e.g., B-System, B-Organization) and a tagged sentence with its corresponding tags.

## Additional Notes

- **Database**: If you need to persist more data, consider expanding the schema in `schemas.py`.
- **Performance**: For deployment in a production environment, consider using a more robust database like PostgreSQL and deploying the application using a WSGI server.

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.
