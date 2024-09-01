
# CyNER 2.0: Named Entity Recognizer

CyNER 2.0 is an advanced Named Entity Recognition (NER) application designed to identify and categorize named entities in text, such as organizations, locations, malware, and more. The application is built with Python, using FastAPI for serving the NER model as an API.

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

### Files Description

- `__init__.py`: Indicates that the directory is a Python package.
- `database.py`: Handles database connections and interactions.
- `main.py`: The main entry point of the application, responsible for starting the FastAPI server.
- `model.py`: Contains the model definitions and business logic for NER.
- `ner_data.db`: SQLite database containing the data for NER.
- `Ner_tags_finder.ipynb`: Jupyter Notebook used for testing and developing the NER models.
- `routers/ner.py`: Contains the API routes related to NER functionalities.
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

The main output of the project is the API response that includes identified entities in the input text along with their corresponding labels (e.g., B-System, B-Organization).

## Additional Notes

- **Customization**: You can modify the NER model and retrain it as per your needs by modifying the `model.py` and using the `Ner_tags_finder.ipynb` for experimentation.
- **Database**: If you need to persist more data, consider expanding the schema in `ner_data.db`.
- **Performance**: For deployment in a production environment, consider using a more robust database like PostgreSQL and deploying the application using a WSGI server.

## License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.
