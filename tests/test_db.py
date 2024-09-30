from sqlalchemy import select

from estudofastapi.models import User


def test_create_user(session):
    user = User(
        username='Jorge', email='Jorge@jorge.com.br', password='senha-do_jorge'
    )
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'Jorge@jorge.com.br')
    )
    assert result.username == 'Jorge'
