# Astra Blog Platform 
### Developed as a project for the course of MAD-1



### How To Install Locally
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
flask shell
from blog.models import User
u = User(username="admin", email="email@provider.com")
u.set_password_hash("yourpass")
db.session.add(u)
db.session.commit()
quit()
flask run
```