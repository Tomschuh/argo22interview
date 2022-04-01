# Installation
`python pip install -r requirements.txt`
# Start app 
`python manage.py runserver 8000`
# Upload request: /api/qrdocument/upload/
POST Request:
```
{
    "imageBase64" : "...",
}
```
Valid response (Status code 201):
```
{
    "imageBase64" : "...",
    "url" : ".../api/qrdocument/{id}/"
}
```
# QrDocument detail request: /api/qrdocument/{id}
GET Request:
Valid response (Status code 200):
```
{
    "process_state": "EXPIRED"
}
```
Process state enum:
* `PENDING` - čeká na zpracování nebo zpracování probíhá
* `EXPIRED` - nahraný doklad je po datu expirace (datum z QR kódu je menší než aktuální datum)
* `VALID` - nahraný doklad je validní (datum z QR kódu je větší než aktuální datum)
* `FRAUD` - dahraný doklad je podvrh (QR kód neobsahuje datum ve specifikovaném formátu)




