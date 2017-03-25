python whats_open/manage.py flush --no-input
python whats_open/manage.py makemigrations
python whats_open/manage.py makemigrations website
python whats_open/manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(email='$superuser$email_domain').delete(); User.objects.create_superuser('$superuser$email_domain', '$superuser', 'admin')" | python whats_open/manage.py shell
python whats_open/manage.py runserver 0.0.0.0:8000
