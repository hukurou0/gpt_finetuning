import openai
import secret
import sys

openai.api_key = secret.api_key

def get_fine_tune_status(fine_tune_id):
    # Retrieve the fine-tuning process details using the OpenAI package
    fine_tune = openai.FineTune.retrieve(fine_tune_id)

    # Check if the status field exists in the response
    if 'status' not in fine_tune:
        print(f"Error: {fine_tune}")
        return None

    # Return the status and the fine-tuned model ID (if available)
    return fine_tune['status'], fine_tune.get('fine_tuned_model', None)

# Call the function to get the fine-tuning status and model ID
fine_tune_id = sys.argv[1]
status, fine_tuned_model_id = get_fine_tune_status(fine_tune_id)
print(f"Fine-tune status: {status}")
print(f"Fine-tuned model ID: {fine_tuned_model_id}")