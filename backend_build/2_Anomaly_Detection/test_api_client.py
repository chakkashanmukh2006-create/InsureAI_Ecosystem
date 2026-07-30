from fastapi.testclient import TestClient
from app.main import app

app.dependency_overrides = {}
def override_get_current_user():
    from app.models.user import User
    return User(id=1, username="admin")

from app.auth.dependencies import get_current_user
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)
res = client.get("/leads/top20")
print("Leads STATUS:", res.status_code)
if res.status_code == 200: print("Leads Count:", len(res.json()))

res2 = client.get("/customers/high-risk")
print("Customers STATUS:", res2.status_code)
if res2.status_code == 200: print("Customers Count:", len(res2.json()))

