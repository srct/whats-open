until nc -z wopen_db 3306; do
    echo "waiting for database to start..."
    sleep 1
done


export WOPEN_SECRET_KEY=$(dd if=/dev/urandom count=100 | tr -dc "A-Za-z0-9" | fold -w 60 | head -n1 2>/dev/null)

python whats-open/manage.py flush --no-input
python whats-open/manage.py makemigrations
python whats-open/manage.py makemigrations api
python whats-open/manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(email='$WOPEN_SUPERUSER$WOPEN_EMAIL_DOMAIN').delete(); User.objects.create_superuser('$WOPEN_SUPERUSER$WOPEN_EMAIL_DOMAIN', '$WOPEN_SUPERUSER', 'admin')" | python whats-open/manage.py shell
python whats-open/manage.py runserver 0.0.0.0:8000
