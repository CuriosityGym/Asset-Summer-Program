cd /home/pi
export GIT_SSL_NO_VERIFY=1
git clone https://github.com/korylprince/pygvoicelib.git
python get_auth.py
vi text.py

!/usr/bin/python
import pygvoicelib
number = raw_input(‘number:’)
txtmsg = raw_input(‘message:’)
client = pygvoicelib.GoogleVoice(username,apppass,auth_token,rnr_se)
client.sms(number,txtmsg)
!/usr/bin/python
import pygvoicelib
client = pygvoicelib.GoogleVoice(‘tanthakkar@gmail.com’,'asdfahrwsthjtrh’,’4k3EozF_Qmrg3tD2_m56nQtFHCVSaTdUxb7HvcaN6g3PV929VH0eH4GGVOVpbVK2O6EaGFzMDYA6PhPjaEHr0ZGjO1GQN3RGhQLXqePWfglbXnA2n7XpUophOk5qztQyv2fYM7eYgtVCYeO6txTqbDQAAANsAAABZ7d0GTL2pJsUauPkH4Z3cpbJFqjfLZYfhok1b11pIMDnEOypZgIcOVdPEt8jEMx7oY9hHJeJoDQZYndDJDu8uoDbDWgxl87GMy990snKWR8iy8VIB17769eVWboa3224U8DLZLUWMpP0d4hfsDK5MQ’,'L6tph126BjmNjDcfTZGaWYeb+sk=’)
python text.py

