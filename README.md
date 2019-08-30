# Desafio Técnico - LuizaLabs/Magalu

# how to run tests?

```bash
pip3 install pytest
pytest 
```



# how to setup?

```bash
source .env # get .env from master
python3 setup.py install 
```

# how to run?

```bash
gunicorn --workers=2 --bind :8080 produtos_favoritos_magalu:app
```

# API DOCS
 Before run enter on [/apidocs](http://localhost:8080/apidocs)
