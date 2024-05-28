
from starlette.testclient import TestClient
from api.main import app
from api.db import get_db
client = TestClient(app)
def temp_db(f):
    def func(SessionLocal, *args, **kwargs):
        # テスト用のDBに接続するためのsessionmaker instanse
        #  (SessionLocal) をfixtureから受け取る

        def override_get_db():
            try:
                db = SessionLocal()
                yield db
            finally:
                db.close()

        # fixtureから受け取るSessionLocalを使うようにget_dbを強制的に変更
        app.dependency_overrides[get_db] = override_get_db
        # Run tests
        f(*args, **kwargs)
        # get_dbを元に戻す
        app.dependency_overrides[get_db] = get_db
    return func

@temp_db
def test_create_user():
    response = client.post(
        "/tasks", json={"title": "test", "description": "test", "status": "todo"}
    )
    assert response.status_code == 200