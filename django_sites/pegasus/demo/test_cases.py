from . import views


# Used to verify pytest is working
def test_tautology():
    assert 1 + 1 == 2


def test_user_creation(rf):
    request = rf.get('/demo/create_account')
    response = views.create_account(request)
    assert response.status_code == 200 # Verify page is up

