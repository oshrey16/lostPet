import json

data = {
    "Words": [
        {
            "Email":
            {
                "Subject": u"למישהו יש חדש בנושא הדיווח!!",
                "body": {
                    "1": u"פרטים ליצירת קשר:",
                    "2": u"למחיקת הפרסום במידה והדיווח טופל:"
                }
            }
        },
        {
            "SMS": {
                "Subject": u"למישהו יש חדש בנושא הדיווח!!",
                "Con" : u"פרטים ליצירת קשר:",
            }
        }
    ]
}

save = json.dumps(data, ensure_ascii=False)
print(save)
with open('text_heb.json', 'wb') as outfile:
    outfile.write(save.encode('utf-8'))

print("\n\n")

with open('text_heb.json', 'rb') as json_file:
    v = json.load(json_file)
    print(v["Words"][0]["Email"]["Subject"])
