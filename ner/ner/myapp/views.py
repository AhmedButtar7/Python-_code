# API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
# API_HEADERS = {"Authorization": "Bearer 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"}
API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
API_HEADERS = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json",
}
from django.shortcuts import render
import requests


def format_api_response(response_data):
    # Create table header
    table_header = "{:<20} {:<20} {:<10} {:<15} {:<15}".format(
        "Text", "Entity Group", "Score", "Start Index", "End Index"
    )
    table_separator = "-" * len(table_header)

    # Build table rows
    table_rows = []
    for entity in response_data:
        table_rows.append(
            "{:<20} {:<20} {:.4f} {:>15} {:>15}".format(
                entity["word"],
                entity["entity_group"],
                entity["score"],
                entity["start"],
                entity["end"],
            )
        )

    # Combine header, separator, and rows
    formatted_table = "\n".join([table_header, table_separator] + table_rows)
    return formatted_table


def query(request):
    context = {}  # Create an empty context dictionary initially

    if request.method == 'POST':
        text_data = request.POST.get('field1')  # Assuming text field name is 'field1'

        payload = {"inputs": text_data}

        try:
            response = requests.post(API_URL, headers=API_HEADERS, json=payload)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            api_data = response.json()
            formatted_response = format_api_response(api_data)  # Format API data
            context['formatted_response'] = formatted_response
        except requests.exceptions.RequestException as e:
            error_message = f"API request failed: {e}"
            context['error_message'] = error_message

    return render(request, 'myapp/query.html', context)
