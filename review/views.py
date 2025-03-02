from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

HUGGING_FACE_API_KEY = "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"

def home(request):
    return render(request, "review/code_submit.html")

def get_live_ai_suggestions(files, pasted_code, language):
    model_name = "bigcode/starcoder"
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}

    suggestions = []

    # Process uploaded files
    for file in files:
        if "content" not in file:
            continue  # Skip invalid files
        response = requests.post(api_url, headers=headers, json={"inputs": f"Review this {language} code:\n\n{file['content']}"})
        if response.status_code == 200:
            suggestions.append({"file": file["name"], "feedback": response.json()[0].get('generated_text', 'No feedback available')})
        else:
            suggestions.append({"file": file["name"], "feedback": "Error in AI response"})

    # Process pasted code
    if pasted_code:
        response = requests.post(api_url, headers=headers, json={"inputs": f"Review this {language} code:\n\n{pasted_code}"})
        if response.status_code == 200:
            suggestions.append({"file": "Pasted Code", "feedback": response.json()[0].get('generated_text', 'No feedback available')})
        else:
            suggestions.append({"file": "Pasted Code", "feedback": "Error in AI response"})

    return suggestions
@csrf_exempt
def live_code_review(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            print("📥 Received Data:", json.dumps(data, indent=2))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

        files = data.get("files", [])
        pasted_code = data.get("pasted_code", "").strip()
        language = data.get("language", "python")

        if not files and not pasted_code:
            return JsonResponse({"error": "No input provided."}, status=400)

        suggestions = get_live_ai_suggestions(files, pasted_code, language)

        return JsonResponse({"message": "Success", "suggestions": suggestions})

    return JsonResponse({"error": "Invalid request method."}, status=400)
