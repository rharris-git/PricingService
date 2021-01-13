

from dotenv import load_dotenv
from models.alert import Alert

load_dotenv()

alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_reached()

if not alerts:
    print("No alerts have been created. Add item and an alert to begin")

