![](https://raw.githubusercontent.com/aaronroman/semantic-search/master/images/bing_ai_header.png)

## Usage

To ensure compatibility, please utilize Python version 3.10 or a similar version, and proceed to install any necessary dependencies.
```
pip install -r requirements.txt
```

To set up your OpenAI API, simply navigate to your `.env` file and add your API credentials. Once that's done, you can run the main script to begin using the API.
```
python3 semantic-search/main.py
```

## Scripts
To explore additional PDF files, utilize the extractor located within the scripts folder.

```
python extract_pdf.py --input_file_path ../data/20221224_mensaje_navidad_esp_rey_felipe.pdf --output_file_path ../data/20221224_mensaje_navidad_esp_rey_felipe.txt
```

## Example

![](https://raw.githubusercontent.com/aaronroman/semantic-search/master/images/semantic_search_execution.png)