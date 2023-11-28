import csv
from django.conf import settings
# # Set the Django settings module in the environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reboot_App.settings')

# Configure the Django settings
from models import User_data

if __name__ == '__main__':
    csv_file_path = './csvfile.csv'

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            User_data.objects.create(
                date=row['date'],
                amount=float(row['amount']),
                balance=float(row['balance']),
                third_party_name=row['third_party_name'],
                category=row['category']
            )
