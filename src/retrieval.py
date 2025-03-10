from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, json

model_name = "numind/NuExtract-1.5-smol"
device = "mps"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, trust_remote_code=True).to(
    device).eval()
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

def predict_NuExtract(prompt, template, model=model, tokenizer=tokenizer, max_length=10_000, max_new_tokens=4_000, do_sample=True, temperature=0.1):
    prompt = f"""<|input|>\n### Template:\n{template}\n###Text:\n{prompt}\n\n<|output|>"""
    with torch.no_grad():
        batch_encodings = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True, max_length=max_length).to(model.device)
        pred_ids = model.generate(**batch_encodings, max_new_tokens=max_new_tokens, do_sample=do_sample, temperature=temperature)
        output = tokenizer.batch_decode(pred_ids, skip_special_tokens=True)[0]

    return output.split("<|output|>")[1]

texts = {
    "text1": "Trova tutti gli articoli su rivista  pubblicati dal dipartimento di informatica nel 2024 che hanno tra le keyword Natural language processing",
    "text2": "Trova sono tutti i progetti finanziati dall'organizzazione unione europea vinti dal dipartimento di informatica nell’anno 2024",
    "text3": "Trova tutte le pubblicazioni di tipo conference proceedings pubblicate nell'ambito del progetto Talkidz",
    "text4": "Trova tutti i progetti finanziati dall'unione Europea",
    "Text5": "Quali sono tutte le pubblicazione del dipartimento di informatica in cui la prima autrice è una persona di genre femminile?",
    "text6": "Trova tutte le pubblicazioni di tipo articolo su rivista delle persone nel dipartimento di informatica che hanno ruolo di Professore Associato",
    "text7": "Trova tutte le pubblicazione di Rossana Damiano con keyword Emotions"
}

template = {
    "QuestionPronoun": "",
    "EntityTypes": {
        "Type": {
            "OrganizationType": [],
            "ProjectType": [],
            "WorkType": [],
            "PublicEngagementType": [],
        },
        "Topic": {
            "Keyword": [],
            "ERC Panel": [],
            "Tematic Area": []
        },
        "year": [],
        "Organization": {
            "University": "",
            "Department": "",
            "Other": ""
          },
        "Person": [],
        "Project": [],
        "Work": [],
        "Role": [],
        "Author": []
    }
}

predictions = {}
for key, text in texts.items():
    predictions[key] = predict_NuExtract(text, template)

for key, prediction in predictions.items():
    print(f"Prediction for {key}: {prediction}")
